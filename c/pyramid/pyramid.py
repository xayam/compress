from c.pyramid import *

class Pyramid:
    width = 8
    dataset = []
    state = []
    recovery = []

    def __init__(self):
        pass

    def init(self, data):
        for level in range(self.width):
            row = []
            for i in range(self.width - level):
                if level == 0:
                    row.append(data[i])
                else:
                    row.append(data[i + 1] - data[i])
            self.state.append(row)

    def encode(self, data):
        self.init(data=data)
        return data

    def decode(self, data):
        return data

    def save(self, filename):
        pass

    def get_input(self, filename="input.txt"):
        with open(filename, mode="rb") as f:
            text = f.read()
        count = -1
        for byte in text:
            count += 1
            if count < self.width:
                yield byte
            else:
                break

    def get_random(self):
        choice_list = list(range(self.width))
        for _ in range(self.width):
            value = rand.choice(choice_list)
            yield value


def main():
    p = Pyramid()
    compress = p.encode(data=p.get_random())
    decompress = p.decode(data=compress)
    assert p.dataset == decompress

if __name__ == "__main__":
    main()
