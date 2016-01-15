#Hello World
#author: Nagabhushan S B

from myhdl import *

def ClockGenerator(clk, T = 20):
    Tby2 = int(T/2)
    interval = delay(10)

    @always(interval)
    def genClock():
        clk.next = not clk

    return genClock

def HelloWorld(clk):

    @instance
    def sayHello():
        while True:
            yield clk.posedge
            print("Hello World at {}".format(now()))

    return sayHello

def simulate():
    clk = Signal(0)
    gen1 = ClockGenerator(clk)
    gen2 = HelloWorld(clk)
    return instances()


toVerilog(simulate)