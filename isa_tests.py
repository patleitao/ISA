import math
import random

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

from isa import isa_runner
from pso import pso_runner


# ISA Easom Test Runs
def easom(x,y):
    return -np.cos(x) * np.cos(y) * np.exp( -np.power((x-np.pi),2) - np.power(y-np.pi,2) )


# constant alpha
isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, popsize=25, evals=1000)
# random alpha
isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, f_alpha=lambda i: random.uniform(0.1, 0.2), popsize=25, evals=1000)
# increasing alpha
isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/1000)), popsize=25, evals=1000)


kowalik_consts = [ [0.1957, 0.25],
                   [0.1947, 0.50],
                   [0.1735, 1.0],
                   [0.16, 2.0],
                   [0.0844, 4.0],
                   [0.0627, 6.0],
                   [0.0456, 8.0],
                   [0.0342, 10.0],
                   [0.0323, 12.0],
                   [0.0235, 14.0],
                   [0.0246, 16.0] ]

def kowalik(x1, x2, x3, x4):
    total = 0
    for i in range(1,11):
        a_i = kowalik_consts[i][0]
        b_i = kowalik_consts[i][1]
        val = np.power(a_i - ( (x1 * (1 + (x2 * b_i)))/( 1 + (x3 * b_i) + (x4 * np.power(b_i,2) )) ), 2)
        total += val
    return total

# constant alpha
isa_runner(lambda x: kowalik(x[0],x[1],x[2],x[3]), 'Kowalik', [(-5, 5)]*4, its=30, popsize=50, evals=1000)
# random alpha
isa_runner(lambda x: kowalik(x[0],x[1],x[2],x[3]), 'Kowalik', [(-5, 5)]*4, its=30, f_alpha=lambda i: random.uniform(0.1, 0.2), popsize=50, evals=1000)
# increasing alpha
isa_runner(lambda x: kowalik(x[0],x[1],x[2],x[3]), 'Kowalik', [(-5, 5)]*4, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/1000)), popsize=50, evals=1000)


def rastigins(x):
    total = 0
    for i in range(0,len(x)):
        val = np.power(x[i],2) + 10*np.cos(2*np.pi*x[i])
        total += val
    return 10*len(x) + total


# constant alpha
isa_runner(lambda x: rastigins(x), 'Rastigins', [(-5.12, 5.12)]*10, its=30, popsize=50, evals=10000)
# random alpha
isa_runner(lambda x: rastigins(x), 'Rastigins', [(-5.12, 5.12)]*10, its=30, f_alpha=lambda i: random.uniform(0.1, 0.2), popsize=50, evals=10000)
# increasing alpha
isa_runner(lambda x: rastigins(x), 'Rastigins', [(-5.12, 5.12)]*10, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/1000)), popsize=50, evals=10000)


def ackley(x):
    a = 20
    b = 0.2
    c = 2 * np.pi
    comp_x = 0
    comp_x2 = 0
    for i in range(0,len(x)):
        comp_x += np.power(x[i], 2)
        comp_x2 += np.cos(c*x[i])
    comp_x = comp_x/len(x)
    comp_x2 = comp_x2/len(x)
    comp_1 = -a * np.exp(-b * np.sqrt(comp_x))
    comp_2 = np.exp(comp_x2)
    return comp_1 - comp_2 + a + np.exp(1)


# constant alpha
isa_runner(lambda x: ackley(x), 'Ackley', [(-32, 32)]*10, its=30, popsize=50, evals=10000)
# random alpha
isa_runner(lambda x: ackley(x), 'Ackley', [(-32, 32)]*10, its=30, f_alpha=lambda i: random.uniform(0.1, 0.2), popsize=50, evals=10000)
# increasing alpha
isa_runner(lambda x: ackley(x), 'Ackley', [(-32, 32)]*10, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/1000)), popsize=50, evals=10000)
