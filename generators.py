#Generator intro
#author: Nagabhushan S B

import sys

def generatorFunc(x):
    for i in range(x):
        yield i

g = generatorFunc(5)
print(next(g))
print(next(g))