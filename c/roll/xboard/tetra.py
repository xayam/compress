from config import *

class Tetra:

    def __init__(self, north, east, south, west: int):
        self.dict_values = {NORTH: north, EAST: east, SOUTH: south, WEST: west}
        self.list_values = [north, east, south, west]
