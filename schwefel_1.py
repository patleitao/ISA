import random
from isa import isa_runner
from benchmark_functions import *

# constant alpha
isa_runner(lambda x: schwefel(x), 'Schwefel', [(-500, 500)]*20, its=30, popsize=50, evals=10000)

