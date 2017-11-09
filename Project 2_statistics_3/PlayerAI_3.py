from random import randint
from BaseAI_3 import BaseAI
from Grid_3 import Grid
from Heuristics_op import Heuristics    ##################################################################
from Node import Node
from MiniMaxTree_op import MiniMax     ##################################################################
from SearchTree import SearchTree

################################ ERASE THAT LATER
class PlayerAI2(BaseAI):

    def __init__(self):
        self.h = Heuristics()

    def getMove(self, grid):
        node1 = Node(grid, 0)
        my_tree = SearchTree(node1)
        my_tree.build_tree(3)
        strategy = MiniMax(node1)
        alpha_beta = strategy.alpha_beta(3)

        return alpha_beta

        # moves = grid.getAvailableMoves()
        # return moves[randint(0, len(moves) - 1)] if moves else None

class PlayerAI(BaseAI):

    def __init__(self, parameters):
        self.parameters = parameters

    def getMove(self, grid):
        node1 = Node(grid, 0)
        strategy = MiniMax(node1, self.parameters)
        alpha_beta = strategy.alpha_beta(3)

        return alpha_beta

        # moves = grid.getAvailableMoves()
        # return moves[randint(0, len(moves) - 1)] if moves else None
