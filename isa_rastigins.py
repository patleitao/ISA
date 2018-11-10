import random
from isa import isa_runner
from benchmark_functions import *

# increasing alpha
isa_runner(lambda x: rastigins(x), 'Rastigins', [(-5.12, 5.12)]*10, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/10000)), popsize=50, evals=10000)

