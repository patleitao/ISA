import math
import numpy as np


def easom(x,y):
    return -np.cos(x) * np.cos(y) * np.exp( -np.power((x-np.pi),2) - np.power(y-np.pi,2) )


def rastigins(x):
    total = 0
    for i in range(0,len(x)):
        val = np.power(x[i],2) + 10*np.cos(2*np.pi*x[i])
        total += val
    return 10*len(x) + total

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