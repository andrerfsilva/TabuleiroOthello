from models.move import Move
from models.board import Board

class MinimaxPlayer:
  def __init__(self, color):
    self.color = color
    self.max_depth = 5


  def play(self, board):
    return self.getBestMove(board)

  def getBestMove(self, board):
    bestMove = None
    bestValue = float('-inf')
    for move in board.valid_moves(self.color):
      new_board = board.get_clone()
      new_board.play(move, self.color)
      curr_value = self.value(new_board, self.color, 0)
      if curr_value > bestValue:
        bestValue = curr_value
        bestMove = move
    return bestMove

  def value(self, board, color, depth):
    retval = 0
    curr_score = board.score()
    if (curr_score[0] + curr_score[1] == 64) or (depth == self.max_depth):
      if self.color == Board.WHITE:
        retval = curr_score[0] - curr_score[1]
      else:
        retval = curr_score[1] - curr_score[0]
    else:
      if color == self.color:
        retval = self.max_value(board, depth)
      else:
        retval = self.min_value(board, depth)
    return retval
    
  def max_value(self, board, depth):
    v = float('-inf')
    if board.valid_moves(self.color).__len__() > 0:
      for move in board.valid_moves(self.color):
        new_board = board.get_clone()
        new_board.play(move, self.color)
        v = max(v, self.value(new_board, self.oponents_color(), depth+1))
    else:
      v = self.value(board.get_clone(), self.oponents_color(), depth+1)
    return v
    
  def min_value(self, board, depth):
    v = float('inf')
    if board.valid_moves(self.color).__len__() > 0:
      for move in board.valid_moves(self.oponents_color()):
        new_board = board.get_clone()
        new_board.play(move, self.oponents_color())
        v = min(v, self.value(new_board, self.color, depth+1))
    else:
      v = self.value(board.get_clone(), self.color, depth+1)
    return v

  def oponents_color(self):
    if self.color == Board.BLACK:
      return Board.WHITE
    return Board.BLACK