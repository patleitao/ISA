import numpy as np


def isa (fobj, bounds, dimensions, alpha=0.2, popsize=20, its=1000):
    #init the population
    init_pop = np.random.rand(popsize, dimensions)
    Lb, Ub = np.asarray(bounds).T
    gb_lam = (Ub - Lb) * 0.01;
    diff = np.fabs(Lb - Ub)
    pop = Lb + init_pop * diff
    #find fitnesses
    fit = np.asarray([fobj(ind) for ind in pop])
    #find the best
    x_gb_idx = np.argmin(fit)
    gb=pop[x_gb_idx]
    for j in range(its):
        pop_new = np.zeros((popsize, dimensions))
        fit_new = np.zeros(popsize)
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
                    pop_new[i] = Lb_j + (Ub_j-Lb_j)*r_2
            # calculate new fitness
            fit_new[i] = fobj(pop_new[i])
            # apply the evolutionary bounding constraint scheme to the new point


        for i in range(popsize):
            # determine points to keep
            # we could do this inline above?
            if fit_new[i] < fit[i]:
                fit[i] = fit_new[i]
                pop[i] = pop_new[i]
    return fit, pop

print(isa(lambda x: sum(x**2),[(-5, 5)],10))