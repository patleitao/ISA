import math
import random

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

from isa import isa_runner
from pso import pso_runner


#ISA Test Runs
# Constant alpha - 0.2, 5 iterations, 50 pop size, 1000 evals per iteration
#isa_runner(lambda x: ((10**5)*x[0]**2) + x[1]**2 - (x[0]**2+x[1]**2)**2 + 10**-5*(x[0]**2 + x[1]**2)**4, 'Dekkers and Aarts',
#         [(-20, 20)]*2, its=5, alpha_ranges=[0.2], popsize=50, evals=1000)

# Linearly increasing alpha - 0.1 to 0.3, 5 iterations, 50 pop size, 1000 evals per iteration
#isa_runner(lambda x: ((10**5)*x[0]**2) + x[1]**2 - (x[0]**2+x[1]**2)**2 + 10**-5*(x[0]**2 + x[1]**2)**4, 'Dekkers and Aarts',
#          [(-20, 20)]*2, its=5, alpha_ranges=[0.1+ (i * (0.2/1000)) for i in range(1000)], popsize=50, evals=1000)

# Constant w - 0.9, 5 iterations, 50 pop size, 1000 evals per iteration
#pso_runner(lambda x: ((10**5)*x[0]**2) + x[1]**2 - (x[0]**2+x[1]**2)**2 + 10**-5*(x[0]**2 + x[1]**2)**4, 'Dekkers and Aarts',
#           [(-20, 20)]*2, its=2, w_ranges=[0.9], popsize=50, evals=1000)

# Linearly decreasing w - 1.1 to 0.1 (as in paper), 5 iterations, 50 pop size, 1000 evals per iteration
#pso_runner(lambda x: ((10**5)*x[0]**2) + x[1]**2 - (x[0]**2+x[1]**2)**2 + 10**-5*(x[0]**2 + x[1]**2)**4, 'Dekkers and Aarts',
#           [(-20, 20)]*2, its=2, w_ranges=[1.1 - (i * (1.0/1000)) for i in range(1000)], popsize=50, evals=1000)



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

# ISA Easom Test Runs
def easom(x,y):
    return -np.cos(x) * np.cos(y) * np.exp( -np.power((x-np.pi),2) - np.power(y-np.pi,2) )


# constant alpha
isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, popsize=50, evals=1000)
# random alpha
isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, f_alpha=lambda i: random.uniform(0.1, 0.2), popsize=50, evals=1000)
# increasing alpha
isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/1000)), popsize=50, evals=1000)