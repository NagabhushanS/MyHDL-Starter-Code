# 2 x 1 Mux Implementation
#author: Nagabhushan S B

from  myhdl import *

def mux2x1(Y, A, B, S):

    @always_comb
    def muxLogic():
        if S==0:
            Y.next = A
            print("At {} Y is {}".format(now(), A))
        else:
            Y.next = B
            print("At {} Y is {}".format(now(), B))

    return muxLogic

def testBench(A, B, S):
    S.next = 0
    yield delay(2)
    A.next = 1
    yield delay(10)
    B.next = 1
    S.next = 1
    yield delay(10)

def simulate():
    Y, A, B, S = [Signal(0) for i in range(4)]
    inst = mux2x1(Y, A, B, S)
    test = testBench(A, B, S)
    sim = Simulation(inst, test)
    sim.run()

if __name__ == "__main__":
    simulate()
    print("Simulation end at {}".format(now()))
