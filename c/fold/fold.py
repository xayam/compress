from c.fold import *

class Fold:
    dataset = []
    state = []

    def __init__(self, width):
        self.width = width

    def init(self, data):
        self.dataset = [int(d) for d in data]

    def encode(self, data):
        self.init(data=data)
        # print(self.dataset)
        self.state.append(self.dataset)
        for y in range(1, self.width):
            x = []
            for i in range(self.width - y):
                x.append(self.state[-1][i + 1] - self.state[-1][i])
            self.state.append(x)
        return self.dataset[0], self.state[-1][0]

    def decode(self, data):
        start, data = data
        # print(f"start={start}, data={data}")
        if data != 0:
            data = self.recovery(start=start, data=[data])
        return data

    def recovery(self, start, data, depth=1):
        # print(f"depth={depth}, data={data}")
        if len(data) == self.width:
            if data[0] != start:
                # print(False)
                return False
            for value in data:
                if value not in self.choice_list:
                    # print(False)
                    return False
            # print(True)
            # print(data)
            return data
        size = abs(data[0])
        # print(f"size={size}")
        for x in range(-size, size + 1):
            # print(f"x={x}")
            variants = [x]
            for level in range(len(data)):
                y = data[level] + variants[-1]
                variants.append(y)
            # print(variants)
            result = self.recovery(start=start, data=variants, depth=depth + 1)
            if result:
                return result
        return None

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
        self.choice_list = [0, 1]  # list(range(2 ** 8))
        for i in range(self.width):
            value = rand.choice(self.choice_list)
            yield value

    def get_all(self):
        self.choice_list = [0, 1]
        for j in range(2 ** self.width):
            value = bin(j)[2:].zfill(self.width)
            # print(value)
            yield value


def main():
    f = Fold(width=3)
    dataset = f.get_all()
    while True:
        try:
            data = dataset.__next__()
            compress = f.encode(data=data)
            decompress = f.decode(data=compress)
            print(f.dataset == decompress, f" | f.dataset={f.dataset} | decompress={decompress}")
        except StopIteration:
            break

if __name__ == "__main__":
    main()
