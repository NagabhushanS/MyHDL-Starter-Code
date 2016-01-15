# 3 bit binaryCounter
#author: Nagabhushan S B

from myhdl import *

def clock(clk, reset):

    @instance
    def clockLogic():
        for i in range(16):
            yield delay(10)
            clk.next = not clk
            if i==8:
                reset.next = 0
                yield delay(10)
                reset.next = 1


    return clockLogic

def counter(binNum, clk, reset):

    @always(clk.posedge, reset.negedge)
    def counterLogic():
        if reset == 0:
            binNum.next = 0
            print("%d at %s" % (binNum, now()))
        else:
            binNum.next = binNum+1
            print("%d at %s" % (binNum, now()))

    return counterLogic

def simulate():
    binNum, clk = [Signal(intbv(0)) for i in range(2)]
    reset = Signal(intbv(1))
    gen1, gen2 = clock(clk, reset), counter(binNum, clk, reset)
    return instances()

inst = traceSignals(simulate)
sim = Simulation(inst)
sim.run()

