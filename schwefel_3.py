import random
from isa import isa_runner
from benchmark_functions import *

# increasing alpha
isa_runner(lambda x: schwefel(x), 'Schwefel', [(-500, 500)]*20, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/1000)), popsize=50, evals=10000)

