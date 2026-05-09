import math
from game_logic import BLACK, WHITE


class MinimaxAI:
    def __init__(self, game, depth=1):
        self.game = game
        self.depth = depth

    def minimax(self, board, depth, alpha, beta, maximizing):
        if self.game.is_game_over(board):
            black_score, white_score = self.game.calculate_score(board)
            return white_score - black_score, None

        if depth == 0:
            return self.game.evaluate_board(board), None

        player = WHITE if maximizing else BLACK
        valid_moves = self.game.get_valid_moves(board, player)

        if not valid_moves:
            return self.minimax(
                board,
                depth - 1,
                alpha,
                beta,
                not maximizing
            )

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
