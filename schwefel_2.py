import random
from isa import isa_runner
from benchmark_functions import *

# random alpha
isa_runner(lambda x: schwefel(x), 'Schwefel', [(-500, 500)]*20, its=30, f_alpha=lambda i: random.uniform(0.1, 0.2), popsize=50, evals=10000)

