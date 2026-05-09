import streamlit as st

from game_logic import GoGame, BOARD_SIZE, BLACK, WHITE
from ai import MinimaxAI


st.set_page_config(
    page_title="Cờ Vây 9x9 AI",
    page_icon="⚫",
    layout="centered"
)

WIN_SCORE = 140


def init_game():
    st.session_state.game = GoGame()
    st.session_state.ai = MinimaxAI(st.session_state.game, depth=1)
    st.session_state.board = st.session_state.game.board
    st.session_state.game_over = False
    st.session_state.message = "Bạn là X. AI là O. Bạn đi trước."
    st.session_state.result_effect = None
    st.session_state.effect_shown = False


if "game" not in st.session_state:
    init_game()

if "result_effect" not in st.session_state:
    st.session_state.result_effect = None

if "effect_shown" not in st.session_state:
    st.session_state.effect_shown = False


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


def draw_board_buttons():
    board = st.session_state.board

    st.markdown('<div class="board-wrap">', unsafe_allow_html=True)

    for i in range(BOARD_SIZE):
        cols = st.columns(BOARD_SIZE, gap="small")

        for j in range(BOARD_SIZE):
            cell = board[i][j]

            if cell == BLACK:
                label = "●"
                key = f"black_{i}_{j}"
            elif cell == WHITE:
                label = "○"
                key = f"white_{i}_{j}"
            else:
                label = "·"
                key = f"empty_{i}_{j}"

            with cols[j]:
                clicked = st.button(
                    label,
                    key=key,
                    use_container_width=True,
                    disabled=st.session_state.game_over or cell != "."
                )

                if clicked:
                    player_move(i, j)
                    st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


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

    .board-wrap {
        background: #d9a441;
        border: 10px solid #7c4a12;
        border-radius: 18px;
        padding: 18px;
        margin-top: 20px;
        box-shadow: 0 20px 45px rgba(0,0,0,0.55);
    }

    div[data-testid="column"] {
        padding: 0px !important;
    }

    div[data-testid="stButton"] > button {
        height: 46px !important;
        min-height: 46px !important;
        width: 46px !important;
        border-radius: 50% !important;
        font-size: 28px !important;
        font-weight: 900 !important;
        padding: 0px !important;
        margin: 2px auto !important;
        background: #c98f2e !important;
        color: #1f1305 !important;
        border: 2px solid #8a5a1f !important;
        transition: 0.08s ease-in-out !important;
    }

    div[data-testid="stButton"] > button:hover {
        transform: scale(1.08);
        border: 2px solid #facc15 !important;
        background: #e0a744 !important;
    }

    div[data-testid="stButton"] > button:disabled {
        opacity: 1 !important;
        transform: none !important;
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

draw_board_buttons()

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
