from models.move import Move
from models.board import Board


# Minimax with alpha-beta pruning.
class MinimaxPlayer:
  def __init__(self, color):
    self.color = color
    self.max_depth = 7


  def play(self, board):
    return self.getBestMove(board)

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

  def value(self, board, color, depth, alpha, beta):
    retval = 0
    curr_score = board.score()
    if (curr_score[0] + curr_score[1] == 64) or (depth == self.max_depth):
      if self.color == Board.WHITE:
        retval = curr_score[0] - curr_score[1]
      else:
        retval = curr_score[1] - curr_score[0]
    else:
      if color == self.color:
        retval = self.max_value(board, depth, alpha, beta)
      else:
        retval = self.min_value(board, depth, alpha, beta)
    return retval
    
  def max_value(self, board, depth, alpha, beta):
    v = float('-inf')
    if board.valid_moves(self.color).__len__() > 0:
      for move in board.valid_moves(self.color):
        new_board = board.get_clone()
        new_board.play(move, self.color)
        v = max(v, self.value(new_board, self.oponents_color(), depth+1, alpha, beta))
        if v >= beta: return v
        alpha = max(alpha, v)
    else:
      v = self.value(board.get_clone(), self.oponents_color(), depth+1, alpha, beta)
    return v
    
  def min_value(self, board, depth, alpha, beta):
    v = float('inf')
    if board.valid_moves(self.color).__len__() > 0:
      for move in board.valid_moves(self.oponents_color()):
        new_board = board.get_clone()
        new_board.play(move, self.oponents_color())
        v = min(v, self.value(new_board, self.color, depth+1, alpha, beta))
        if v <= alpha: return v
        beta = min(beta, v)
    else:
      v = self.value(board.get_clone(), self.color, depth+1, alpha, beta)
    return v

  def oponents_color(self):
    if self.color == Board.BLACK:
      return Board.WHITE
    return Board.BLACK