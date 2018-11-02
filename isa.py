import numpy as np


def isa (fobj, bounds, dimensions, alpha=0.2, popsize=10, its=1000):
    #init the population
    init_pop = np.random.rand(popsize, dimensions)
    Lb, Ub = np.asarray(bounds).T
    diff = np.fabs(Lb - Ub)
    pop = Lb + init_pop * diff
    #find fitnesses
    fitnesses = np.asarray([fobj(ind) for ind in pop])
    #find the best
    x_gb_idx = np.argmin(fitnesses)
    print(x_gb_idx)
    gb=pop[x_gb_idx]
    for i in range(its):
        for j in range(popsize):
            if j == x_gb_idx:
                #global best - do some random walk
                r_1 = np.random.rand(1, 1)
            else:
                if np.random.rand(1, 1) < alpha:
                    #mirror group
                    print(r_1)
                else:
                    #compositon group

isa(lambda x: sum(x**2)/len(x),[(-5, 5)],10)