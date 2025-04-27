from c.fold import *

class Fold:
    width = 3
    dataset = []
    state = []

    def __init__(self):
        pass

    def init(self, data):
        self.dataset = [d for d in data]

    def encode(self, data):
        self.init(data=data)
        print(self.dataset)
        self.state.append(self.dataset)
        for y in range(1, self.width):
            x = []
            for i in range(self.width - y):
                x.append(self.state[-1][i + 1] - self.state[-1][i])
            self.state.append(x)
        return self.state[-1][0]

    def decode(self, data):
        print(data)
        if data != 0:
            data = self.recovery(data=[[[data]]])
        return data

    def recovery(self, data, depth=1):
        size = abs(data[-1][0][0])
        print(f"size={size}")
        print(data)
        if depth > len(data):
            return data[-1]
        current = data[-1]
        variants = [current]
        for level in range(depth):
            variant = []
            for x in range(-size, size + 1):
                y = current[-1][level] + x
                variant.append([x, y])
            print(variant)
            for folder in variant:
                datas = current[:]
                datas.append(folder)
                variants.append(datas)
            print(variants)
        return self.recovery(data=variants, depth=depth + 1)

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
        choice_list = [0, 1, 2]  # list(range(2 ** 8))
        for i in range(self.width):
            value = rand.choice(choice_list)
            yield value


def main():
    f = Fold()
    compress = f.encode(data=f.get_random())
    decompress = f.decode(data=compress)
    # assert f.dataset == decompress

if __name__ == "__main__":
    main()
