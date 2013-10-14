from models.move import Move
from models.board import Board
from models.players.minimax_player import MinimaxPlayer

# Bate como uma menininha!
class HitGirlPlayer(MinimaxPlayer):
  def __init__(self, color):
    self.color = color
    self.max_depth = 5
    self.initial_corner_value = 3

  # Testando alternativas.
  def evaluation(self, board):
    # score parcial
    score = board.score()
    partial_score = 0
    if self.color == Board.WHITE:
      partial_score = score[0] - score[1]
    else:
      partial_score = score[1] - score[0]
    # score de mobilidade
    mobility_score = board.valid_moves(self.color).__len__() - board.valid_moves(self.opponents_color()).__len__()
    # score de escanteio :P
    total_moves = score[0] + score[1]
    corner_score = 0
    corners = [[1,1],[1,8], [8,1], [8,8]]
    for corner in corners:
      if board.board[corner[0]][corner[1]] == self.color:             corner_score += 1
      if board.board[corner[0]][corner[1]] == self.opponents_color(): corner_score -= 1
    corner_value = (total_moves*(1-self.initial_corner_value)/64.0) + self.inicial_corner_value
    corner_score *= corner_value
    # score total
    return partial_score + mobility_score + corner_score

	#f(x) = ax + b
	#a0 + b = i
	#a64 + b = 1
	#b = i
	#a = (1-i)/64