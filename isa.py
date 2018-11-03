import numpy as np


def isa (fobj, bounds, dimensions, alpha=0.2, popsize=10, its=1000):
    #init the population
    init_pop = np.random.rand(popsize, dimensions)
    Lb, Ub = np.asarray(bounds).T
    gb_lam = (Ub - Lb) * 0.01;
    diff = np.fabs(Lb - Ub)
    pop = Lb + init_pop * diff
    #find fitnesses
    fitnesses = np.asarray([fobj(ind) for ind in pop])
    #find the best
    x_gb_idx = np.argmin(fitnesses)
    print(x_gb_idx)
    gb=pop[x_gb_idx]
    for j in range(its):
        pop_new = np.zeros((popsize, dimensions))
        # find the minimal and maxima of each dimension
        Lb_j = pop.min(axis=0)
        Ub_j = pop.max(axis=0)
        for i in range(popsize):
            if j == x_gb_idx:
                #global best - do some random walk
                pop_new[i] = pop[i]+(np.random.normal(size=dimensions) * gb_lam)
            else:
                if np.random.rand(1, 1) < alpha:
                    #mirror group
                    r_3 = np.random.rand(1, 1)[0][0]
                    xm_i_j = pop[i]*r_3 + ((1 -r_3)*gb)
                    pop_new[i] = (2 * xm_i_j) - pop[i]
                else:
                    # compositon group
                    r_2 = np.random.rand(1, 1)[0][0]
                    x_i_j = Lb_j + (Ub_j-Lb_j)*r_2
                    pop_new[i] = x_i_j
                    pass

isa(lambda x: sum(x**2)/len(x),[(-5, 5)],10)