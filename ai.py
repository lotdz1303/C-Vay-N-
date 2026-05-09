import math
from game_logic import BLACK, WHITE, EMPTY, BOARD_SIZE


class MinimaxAI:
    def __init__(self, game, depth=1):
        self.game = game
        self.depth = depth
        self.max_candidates = 14

    def get_candidate_moves(self, board, player):
        candidates = set()
        has_stone = False

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] != EMPTY:
                    has_stone = True

                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            nx = i + dx
                            ny = j + dy

                            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                                if board[nx][ny] == EMPTY:
                                    candidates.add((nx, ny))

        if not has_stone:
            return [(BOARD_SIZE // 2, BOARD_SIZE // 2)]

        valid_moves = []

        for x, y in candidates:
            if self.game.is_valid_move(board, x, y, player):
                valid_moves.append((x, y))

        if not valid_moves:
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if board[i][j] == EMPTY and self.game.is_valid_move(board, i, j, player):
                        valid_moves.append((i, j))

        valid_moves.sort(
            key=lambda move: self.move_priority(board, move, player),
            reverse=True
        )

        return valid_moves[:self.max_candidates]

    def move_priority(self, board, move, player):
        x, y = move
        center = BOARD_SIZE // 2
        score = 0

        distance_to_center = abs(x - center) + abs(y - center)
        score += max(0, 8 - distance_to_center)

        opponent = BLACK if player == WHITE else WHITE

        for nx, ny in self.game.neighbors(x, y):
            if board[nx][ny] == player:
                score += 4
            elif board[nx][ny] == opponent:
                score += 3

        return score

    def minimax(self, board, depth, alpha, beta, maximizing):
        if depth == 0:
            return self.game.evaluate_board(board), None

        player = WHITE if maximizing else BLACK
        valid_moves = self.get_candidate_moves(board, player)

        if not valid_moves:
            return self.game.evaluate_board(board), None

        best_move = None

        if maximizing:
            max_eval = -math.inf

            for move in valid_moves:
                x, y = move
                new_board = self.game.make_move(board, x, y, WHITE)

                eval_score, _ = self.minimax(
                    new_board,
                    depth - 1,
                    alpha,
                    beta,
                    False
                )

                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move

                alpha = max(alpha, eval_score)

                if beta <= alpha:
                    break

            return max_eval, best_move

        min_eval = math.inf

        for move in valid_moves:
            x, y = move
            new_board = self.game.make_move(board, x, y, BLACK)

            eval_score, _ = self.minimax(
                new_board,
                depth - 1,
                alpha,
                beta,
                True
            )

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move

            beta = min(beta, eval_score)

            if beta <= alpha:
                break

        return min_eval, best_move

    def get_best_move(self, board):
        _, move = self.minimax(
            board,
            self.depth,
            -math.inf,
            math.inf,
            True
        )

        return move
