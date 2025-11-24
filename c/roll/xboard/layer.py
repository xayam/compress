from state import State


class Layer(State):

    def __init__(self, name: str):
        self.name = name
        self.groups = None

        State.__init__(self)

        self.start()
        self.init(groups=self.groups)

    def start(self):
        pass