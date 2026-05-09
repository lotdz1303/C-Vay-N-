from flask import Flask, render_template, request, jsonify, session
from game_logic import GoGame, BLACK, WHITE, BOARD_SIZE
from ai import MinimaxAI


app = Flask(__name__)
app.secret_key = "go-9x9-ai-secret-key"

WIN_SCORE = 140


def new_game():
    game = GoGame()

    session["board"] = game.board
    session["game_over"] = False
    session["result_effect"] = None
    session["message"] = "Bạn là X. AI là O. Bạn đi trước."


def get_game():
    return GoGame()


def get_board():
    if "board" not in session:
        new_game()

    return session["board"]


def save_board(board):
    session["board"] = board


def set_result(effect, black_score, white_score):
    session["game_over"] = True
    session["result_effect"] = effect

    if effect == "win":
        session["message"] = (
            f"🎉 BẠN ĐÃ THẮNG AI! Điểm bạn: {black_score} - Điểm AI: {white_score}"
        )
    elif effect == "lose":
        session["message"] = (
            f"💀 BẠN ĐÃ THUA AI! Điểm bạn: {black_score} - Điểm AI: {white_score}"
        )
    else:
        session["message"] = (
            f"🤝 HÒA! Điểm bạn: {black_score} - Điểm AI: {white_score}"
        )


def check_game_over(board, force_end=False):
    game = get_game()
    black_score, white_score = game.calculate_score(board)

    if black_score >= WIN_SCORE:
        set_result("win", black_score, white_score)
        return True

    if white_score >= WIN_SCORE:
        set_result("lose", black_score, white_score)
        return True

    if game.is_game_over(board) or force_end:
        winner, black_score, white_score = game.get_winner(board)

        if winner == BLACK:
            set_result("win", black_score, white_score)
        elif winner == WHITE:
            set_result("lose", black_score, white_score)
        else:
            set_result("draw", black_score, white_score)

        return True

    return False


def build_state():
    game = get_game()
    board = get_board()

    black_score, white_score = game.calculate_score(board)

    return {
        "board": board,
        "board_size": BOARD_SIZE,
        "black_score": black_score,
        "white_score": white_score,
        "win_score": WIN_SCORE,
        "game_over": session.get("game_over", False),
        "result_effect": session.get("result_effect"),
        "message": session.get("message", "Bạn là X. AI là O. Bạn đi trước.")
    }


@app.route("/")
def index():
    if "board" not in session:
        new_game()

    return render_template("index.html")


@app.route("/api/state", methods=["GET"])
def state():
    if "board" not in session:
        new_game()

    return jsonify(build_state())


@app.route("/api/move", methods=["POST"])
def move():
    if "board" not in session:
        new_game()

    if session.get("game_over", False):
        return jsonify(build_state())

    data = request.get_json()
    x = int(data.get("x"))
    y = int(data.get("y"))

    game = get_game()
    board = get_board()

    if not game.is_valid_move(board, x, y, BLACK):
        session["message"] = "Nước đi không hợp lệ. Hãy chọn vị trí khác."
        return jsonify(build_state())

    board = game.make_move(board, x, y, BLACK)
    save_board(board)

    if check_game_over(board):
        return jsonify(build_state())

    ai = MinimaxAI(game, depth=1)
    ai_move = ai.get_best_move(board)

    if ai_move is None:
        session["message"] = "AI không còn nước đi. Đang kiểm tra kết quả..."
        check_game_over(board, force_end=True)
        return jsonify(build_state())

    ai_x, ai_y = ai_move
    board = game.make_move(board, ai_x, ai_y, WHITE)
    save_board(board)

    session["message"] = f"AI vừa đánh tại dòng {ai_x}, cột {ai_y}. Đến lượt bạn."

    check_game_over(board)

    return jsonify(build_state())


@app.route("/api/reset", methods=["POST"])
def reset():
    new_game()
    return jsonify(build_state())


@app.route("/api/finish", methods=["POST"])
def finish():
    board = get_board()
    check_game_over(board, force_end=True)
    return jsonify(build_state())


if __name__ == "__main__":
    app.run(debug=True)
