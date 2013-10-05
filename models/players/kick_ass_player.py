from models.move import Move
from models.board import Board
from models.players.minimax_player import MinimaxPlayer

# Agente anti naive minimax!
class KickAssPlayer(MinimaxPlayer):
  def __init__(self, color):
    self.color = color
    self.max_depth = 5

  # Função de avaliação de um estado não final. Além do score parcial,
  # o agente leva em consideração a mobilidade do estado.
  def evaluation(self, board):
    score = board.score()
    mobility_score = board.valid_moves(self.color).__len__() - board.valid_moves(self.opponents_color()).__len__()
    if self.color == Board.WHITE: return (score[0] - score[1] + mobility_score)
    return (score[1] - score[0] + mobility_score)
