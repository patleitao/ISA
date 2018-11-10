import random
from isa import isa_runner
from benchmark_functions import *

isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, popsize=25, evals=1000)
# random alpha
isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, f_alpha=lambda i: random.uniform(0.1, 0.2), popsize=25, evals=1000)
# increasing alpha
isa_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/1000)), popsize=25, evals=1000)

# constant alpha
isa_runner(lambda x: kowalik(x[0],x[1],x[2],x[3]), 'Kowalik', [(-5, 5)]*4, its=30, popsize=25, evals=1000)
# random alpha
isa_runner(lambda x: kowalik(x[0],x[1],x[2],x[3]), 'Kowalik', [(-5, 5)]*4, its=30, f_alpha=lambda i: random.uniform(0.1, 0.2), popsize=25, evals=1000)
# increasing alpha
isa_runner(lambda x: kowalik(x[0],x[1],x[2],x[3]), 'Kowalik', [(-5, 5)]*4, its=30, f_alpha=lambda i: 0.1+ (i * (0.2/1000)), popsize=25, evals=1000)

