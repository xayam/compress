from state import State


class Layer(State):

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.groups = None
        State.__init__(self)
        self.start()

    def start(self):
        pass
        self.init(groups=self.groups)