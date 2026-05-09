import streamlit as st
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates

from game_logic import GoGame, BOARD_SIZE, BLACK, WHITE
from ai import MinimaxAI


st.set_page_config(
    page_title="Cờ Vây 9x9 AI",
    page_icon="⚫",
    layout="centered"
)

CELL = 52
MARGIN = 42
BOARD_PIXELS = MARGIN * 2 + CELL * (BOARD_SIZE - 1)
WIN_SCORE = 140
CLICK_RADIUS = 28


def init_game():
    st.session_state.game = GoGame()
    st.session_state.ai = MinimaxAI(st.session_state.game, depth=1)
    st.session_state.board = st.session_state.game.board
    st.session_state.game_over = False
    st.session_state.message = "Bạn là X. AI là O. Bạn đi trước."
    st.session_state.board_key = st.session_state.get("board_key", 0) + 1
    st.session_state.last_click_id = None
    st.session_state.result_effect = None
    st.session_state.effect_shown = False


if "game" not in st.session_state:
    init_game()

if "result_effect" not in st.session_state:
    st.session_state.result_effect = None

if "effect_shown" not in st.session_state:
    st.session_state.effect_shown = False

if "last_click_id" not in st.session_state:
    st.session_state.last_click_id = None


def draw_board(board):
    img = Image.new("RGB", (BOARD_PIXELS, BOARD_PIXELS), "#d9a441")
    draw = ImageDraw.Draw(img)

    draw.rectangle(
        [8, 8, BOARD_PIXELS - 8, BOARD_PIXELS - 8],
        outline="#7c4a12",
        width=14
    )

    for i in range(BOARD_SIZE):
        pos = MARGIN + i * CELL

        draw.line(
            [(MARGIN, pos), (MARGIN + CELL * (BOARD_SIZE - 1), pos)],
            fill="#1f1305",
            width=2
        )

        draw.line(
            [(pos, MARGIN), (pos, MARGIN + CELL * (BOARD_SIZE - 1))],
            fill="#1f1305",
            width=2
        )

    star_points = [(2, 2), (2, 6), (4, 4), (6, 2), (6, 6)]

    for x, y in star_points:
        cx = MARGIN + y * CELL
        cy = MARGIN + x * CELL
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill="#1f1305")

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            cx = MARGIN + j * CELL
            cy = MARGIN + i * CELL

            if board[i][j] == BLACK:
                draw.ellipse(
                    [cx - 18, cy - 18, cx + 18, cy + 18],
                    fill="#111111",
                    outline="#000000",
                    width=2
                )

            elif board[i][j] == WHITE:
                draw.ellipse(
                    [cx - 18, cy - 18, cx + 18, cy + 18],
                    fill="#f8fafc",
                    outline="#9ca3af",
                    width=2
                )

    return img


def get_click_position(value):
    if value is None:
        return None

    click_x = value["x"]
    click_y = value["y"]

    nearest_row = None
    nearest_col = None
    min_distance = 999999

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            point_x = MARGIN + col * CELL
            point_y = MARGIN + row * CELL

            distance = ((click_x - point_x) ** 2 + (click_y - point_y) ** 2) ** 0.5

            if distance < min_distance:
                min_distance = distance
                nearest_row = row
                nearest_col = col

    if min_distance <= CLICK_RADIUS:
        return nearest_row, nearest_col

    return None


def set_result(effect, black_score, white_score):
    st.session_state.game_over = True
    st.session_state.result_effect = effect

    if effect == "win":
        st.session_state.message = (
            f"🎉 BẠN ĐÃ THẮNG AI! Điểm bạn: {black_score} - Điểm AI: {white_score}"
        )

    elif effect == "lose":
        st.session_state.message = (
            f"💀 BẠN ĐÃ THUA AI! Điểm bạn: {black_score} - Điểm AI: {white_score}"
        )

    else:
        st.session_state.message = (
            f"🤝 HÒA! Điểm bạn: {black_score} - Điểm AI: {white_score}"
        )


def check_game_over(force_end=False):
    game = st.session_state.game
    black_score, white_score = game.calculate_score(st.session_state.board)

    if black_score >= WIN_SCORE:
        set_result("win", black_score, white_score)
        return True

    if white_score >= WIN_SCORE:
        set_result("lose", black_score, white_score)
        return True

    if game.is_game_over(st.session_state.board) or force_end:
        winner, black_score, white_score = game.get_winner(st.session_state.board)

        if winner == BLACK:
            set_result("win", black_score, white_score)

        elif winner == WHITE:
            set_result("lose", black_score, white_score)

        else:
            set_result("draw", black_score, white_score)

        return True

    return False


def run_ai_move():
    game = st.session_state.game
    ai = st.session_state.ai

    move = ai.get_best_move(st.session_state.board)

    if move is None:
        st.session_state.message = "AI không còn nước đi. Đang kiểm tra kết quả..."
        check_game_over(force_end=True)
        return

    x, y = move
    st.session_state.board = game.make_move(st.session_state.board, x, y, WHITE)
    st.session_state.message = f"AI vừa đánh tại dòng {x}, cột {y}. Đến lượt bạn."


def player_move(x, y):
    game = st.session_state.game

    if st.session_state.game_over:
        return

    if not game.is_valid_move(st.session_state.board, x, y, BLACK):
        st.session_state.message = "Nước đi không hợp lệ. Hãy chọn vị trí khác."
        return

    st.session_state.board = game.make_move(st.session_state.board, x, y, BLACK)

    if check_game_over():
        return

    run_ai_move()
    check_game_over()


st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #1f2937 0%, #0f172a 50%, #020617 100%);
        color: #e5e7eb;
    }

    h1 {
        text-align: center;
        color: #f8fafc;
        font-weight: 900;
    }

    .sub-title {
        text-align: center;
        color: #cbd5e1;
        font-size: 18px;
        margin-bottom: 20px;
    }

    [data-testid="stMetric"] {
        background: #111827;
        border: 1px solid #334155;
        padding: 16px;
        border-radius: 14px;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"] {
        color: white !important;
    }

    div[data-testid="stAlert"] {
        background-color: #172554;
        color: #bfdbfe;
        border: 1px solid #2563eb;
        border-radius: 12px;
    }

    img {
        border-radius: 16px;
        box-shadow: 0 20px 45px rgba(0,0,0,0.55);
        user-select: none;
        -webkit-user-drag: none;
        cursor: pointer;
    }

    div[data-testid="stHorizontalBlock"] button[kind="secondary"] {
        height: 52px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        background: #1e293b !important;
        color: white !important;
        border: 1px solid #475569 !important;
    }

    div[data-testid="stHorizontalBlock"] button[kind="secondary"]:hover {
        background: #334155 !important;
        border: 1px solid #60a5fa !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("CỜ VÂY 9x9 - AI MINIMAX ALPHA-BETA")
st.markdown(
    '<div class="sub-title">Người chơi: <b>X</b> | AI: <b>O</b></div>',
    unsafe_allow_html=True
)

black_score, white_score = st.session_state.game.calculate_score(st.session_state.board)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Điểm người chơi", black_score)

with col2:
    st.metric("Điểm AI", white_score)

with col3:
    st.metric("Mốc thắng", WIN_SCORE)

st.info(st.session_state.message)

if st.session_state.game_over:
    if st.session_state.result_effect == "win":
        st.markdown(
            """
            <div style="
                background: linear-gradient(135deg, #16a34a, #22c55e);
                padding: 24px;
                border-radius: 18px;
                text-align: center;
                color: white;
                font-size: 30px;
                font-weight: 900;
                margin: 20px 0;
                box-shadow: 0 20px 45px rgba(34,197,94,0.35);
            ">
                🎉 BẠN ĐÃ THẮNG AI 🎉
            </div>
            """,
            unsafe_allow_html=True
        )

        if not st.session_state.effect_shown:
            st.balloons()
            st.session_state.effect_shown = True

    elif st.session_state.result_effect == "lose":
        st.markdown(
            """
            <div style="
                background: linear-gradient(135deg, #7f1d1d, #dc2626);
                padding: 24px;
                border-radius: 18px;
                text-align: center;
                color: white;
                font-size: 30px;
                font-weight: 900;
                margin: 20px 0;
                box-shadow: 0 20px 45px rgba(220,38,38,0.35);
            ">
                💀 BẠN ĐÃ THUA AI 💀
            </div>
            """,
            unsafe_allow_html=True
        )

        if not st.session_state.effect_shown:
            st.snow()
            st.session_state.effect_shown = True

    elif st.session_state.result_effect == "draw":
        st.markdown(
            """
            <div style="
                background: linear-gradient(135deg, #334155, #64748b);
                padding: 24px;
                border-radius: 18px;
                text-align: center;
                color: white;
                font-size: 30px;
                font-weight: 900;
                margin: 20px 0;
                box-shadow: 0 20px 45px rgba(100,116,139,0.35);
            ">
                🤝 HÒA 🤝
            </div>
            """,
            unsafe_allow_html=True
        )

board_image = draw_board(st.session_state.board)

value = streamlit_image_coordinates(
    board_image,
    key=f"go_board_{st.session_state.board_key}",
    width=BOARD_PIXELS
)

if value is not None and not st.session_state.game_over:
    click_id = f"{st.session_state.board_key}_{value['x']}_{value['y']}"

    if st.session_state.last_click_id != click_id:
        st.session_state.last_click_id = click_id
        position = get_click_position(value)

        if position is not None:
            x, y = position
            player_move(x, y)
            st.session_state.board_key += 1
            st.rerun()

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🔄 Chơi lại",
        key="reset_game_btn",
        use_container_width=True
    ):
        init_game()
        st.rerun()

with col2:
    if st.button(
        "🏁 Kết thúc & tính điểm",
        key="finish_game_btn",
        use_container_width=True
    ):
        check_game_over(force_end=True)
        st.session_state.board_key += 1
        st.rerun()


with st.expander("Giải thích thuật toán"):
    st.write(
        """
        AI sử dụng thuật toán **Minimax** để giả lập các nước đi có thể xảy ra.

        Trong quá trình tìm kiếm, chương trình dùng **Alpha-Beta Pruning**
        để loại bỏ những nhánh không cần xét, giúp AI tìm nước đi nhanh hơn.

        Hàm heuristic đánh giá trạng thái bàn cờ dựa trên:

        - Số quân trong nhóm
        - Số khí còn lại của nhóm quân
        - Chênh lệch điểm giữa AI và người chơi
        """
    )
