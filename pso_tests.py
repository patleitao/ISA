from pso import pso_runner
from benchmark_functions import *

# constant w
pso_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, popsize=25, evals=1000)
# decreasing w (as in paper)
pso_runner(lambda x: easom(x[0],x[1]), 'Easom', [(-10, 10)]*2, its=30, w_ranges=[1.1 - (w * (1.0/1000)) for w in range(1000)], popsize=25, evals=1000)

# constant w
pso_runner(lambda x: kowalik(x[0],x[1],x[2],x[3]), 'Kowalik', [(-5, 5)]*4, its=30, popsize=25, evals=1000)
# decreasing w
pso_runner(lambda x: kowalik(x[0],x[1],x[2],x[3]), 'Kowalik', [(-5, 5)]*4, its=30, w_ranges=[1.1 - (w * (1.0/1000)) for w in range(1000)], popsize=25, evals=1000)

# constant w
pso_runner(lambda x: rastigins(x), 'Rastigins', [(-5.12, 5.12)]*10, its=30, popsize=50, evals=10000)
# decreasing w
pso_runner(lambda x: rastigins(x), 'Rastigins', [(-5.12, 5.12)]*10, its=30, w_ranges=[1.1 - (w * (1.0/1000)) for w in range(1000)], popsize=50, evals=10000)

# constant w
pso_runner(lambda x: ackley(x), 'Ackley', [(-32, 32)]*10, its=30, popsize=50, evals=10000)
# decreasing w
pso_runner(lambda x: ackley(x), 'Ackley', [(-32, 32)]*10, its=30, w_ranges=[1.1 - (w * (1.0/1000)) for w in range(1000)], popsize=50, evals=10000)

# constant w
pso_runner(lambda x: sphere(x), 'Sphere', [(-100, 100)]*20, its=30, popsize=50, evals=10000)
# decreasing w
pso_runner(lambda x: sphere(x), 'Sphere', [(-100, 100)]*20, its=30, w_ranges=[1.1 - (w * (1.0/1000)) for w in range(1000)], popsize=50, evals=10000)