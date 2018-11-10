from pso import pso_runner
from benchmark_functions import *

# decreasing w
pso_runner(lambda x: schwefel(x), 'Schwefel', [(-500, 500)]*20, its=30, w_ranges=[1.1 - (w * (1.0/10000)) for w in range(10000)], popsize=50, evals=10000)
