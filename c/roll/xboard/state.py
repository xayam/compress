from config import *
from tetra import Tetra
from group import Group
from field import Field
from board import Board

class State:

    def __init__(self):
        self.size = SIZE

        self.board = Board(size=self.size)

    def init(self):
        pass
