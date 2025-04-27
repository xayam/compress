from c.pyramid import *

class Pyramid:
    width = 8 * 8

    def __init__(self):
        pass

    def init(self):
        pass

    def encode(self):
        self.init()
        return []

    def decode(self):
        self.init()
        return []

    def save(self, filename):
        pass

    def get_input(self, filename="input.txt"):
        with open(filename, mode="rb") as f:
            text = f.read()
        count = -1
        for byte in text:
            binary_str = bin(byte)[2:].zfill(8)
            for binary in binary_str:
                count += 1
                if count < self.width:
                    yield int(binary)
                else:
                    break

    def get_random(self):
        for i in range(self.width):
            value = rand.choice([0, 1])
            yield value


def main():
    p = Pyramid()
    compress = p.encode()
    decompress = p.decode()
    assert compress == decompress

if __name__ == "__main__":
    main()
