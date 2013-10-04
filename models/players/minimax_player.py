from models.move import Move
from models.board import Board

# Minimax with alpha-beta pruning.
class MinimaxPlayer:
  def __init__(self, color):
    self.color = color
    self.max_depth = 7

  def play(self, board):
    return self.getBestMove(board)

  # Escolhe a melhor jogada usando o algoritmo minimax.
  def getBestMove(self, board):
    bestMove = None
    bestValue = float('-inf')
    alpha = float("-inf")
    beta = float("inf")
    for move in board.valid_moves(self.color):
      new_board = board.get_clone()
      new_board.play(move, self.color)
      curr_value = self.value(new_board, self.color, 0, alpha, beta)
      if curr_value > bestValue:
        bestValue = curr_value
        bestMove = move
        alpha = bestValue
    return bestMove
  
  # Computa recursivamente o valor minimax de um dado estado.
  def value(self, board, color, depth, alpha, beta):
    if (is_final_state(board)): return self.utility(board)
    if (depth == self.max_depth): return self.evaluation(board)
    if color == self.color:
      return self.max_value(board, depth, alpha, beta)
    else:
      return self.min_value(board, depth, alpha, beta)
    
  def max_value(self, board, depth, alpha, beta):
    v = float('-inf')
    if board.valid_moves(self.color).__len__() > 0:
      for move in board.valid_moves(self.color):
        new_board = board.get_clone()
        new_board.play(move, self.color)
        v = max(v, self.value(new_board, self.opponents_color(), depth+1, alpha, beta))
        if v >= beta: return v
        alpha = max(alpha, v)
    else:
      v = self.value(board.get_clone(), self.opponents_color(), depth+1, alpha, beta)
    return v
    
  def min_value(self, board, depth, alpha, beta):
    v = float('inf')
    if board.valid_moves(self.opponents_color()).__len__() > 0:
      for move in board.valid_moves(self.opponents_color()):
        new_board = board.get_clone()
        new_board.play(move, self.opponents_color())
        v = min(v, self.value(new_board, self.color, depth+1, alpha, beta))
        if v <= alpha: return v
        beta = min(beta, v)
    else:
      v = self.value(board.get_clone(), self.color, depth+1, alpha, beta)
    return v

  # Retorna a utilidade de um estado final:
  # +infito para vitória
  # -infinito para derrota
  # zero para empate
  def utility(self, board):
    score = board.score()
    if self.color == Board.WHITE:
      if score[0] > score[1]: return float("inf")
      if score[0] < score[1]: return float("-inf")
      return 0
    else:
      if score[1] > score[0]: return float("inf")
      if score[1] < score[0]: return float("-inf")
      return 0
 
  # Função de avaliação de um estado não final.
  def evaluation(self, board):
    score = board.score()
    if self.color == Board.WHITE: return (score[0] - score[1])
    return (score[1] - score[0])
  
  # Retorna a cor do jogador adversário.
  def opponents_color(self):
    if self.color == Board.BLACK:
      return Board.WHITE
    return Board.BLACK

# Confere se é estado final.
def is_final_state(board):
  return (board.valid_moves(Board.BLACK).__len__() == 0) and (board.valid_moves(Board.WHITE).__len__() == 0)
