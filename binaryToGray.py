#Binary to Gray Code Converter
#author: Nagabhushan S B

from myhdl import *

def Binary2Gray(B, G, width):
    @always_comb
    def convert():
        for i in range(width):
            if i != width - 1:
                G.next[i] = B[i] ^ B[i + 1]
            else:
                G.next[i] = B[i]

    return convert


def Test_BinaryToGray(width):
    B = Signal(intbv(0))
    G = Signal(intbv(0))

    gen1 = Binary2Gray(B, G, width)

    @instance
    def changeB():
        for i in range(2 ** width):
            B.next = intbv(i)
            yield delay(10)
            print("When B is {}, G is {}".format(bin(B, width), bin(G, width)))

    return gen1, changeB


inst = Test_BinaryToGray(4)
sim = Simulation(inst)
sim.run()
