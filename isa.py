from datetime import datetime
import json
import numpy as np
import time
from utils import recording_intervals

def isa(fobj, bounds, f_alpha=lambda i: 0.2, popsize=20, evals=1000):
    #recording intervals
    start_time = time.time()
    print("ISA: popsize: %s, evals: %s" % (popsize, evals))
    results = []
    record_intervals = recording_intervals(evals)
    #init the population
    dimensions=len(bounds)
    init_pop = np.random.rand(popsize, dimensions)
    Lb, Ub = np.asarray(bounds).T
    gb_lam = (Ub - Lb) * 0.01;
    diff = np.fabs(Lb - Ub)
    pop = Lb + init_pop * diff
    #find fitnesses
    fit = np.asarray([fobj(ind) for ind in pop])
    for j in range(evals):
        alpha = f_alpha(j)
        # find the best
        x_gb_idx = np.argmin(fit)
        gb = pop[x_gb_idx]
        pop_new = np.zeros((popsize, dimensions))
        fit_new = np.zeros(popsize)
        # find the minimal and maxima of each dimension
        Lb_j = pop.min(axis=0)
        Ub_j = pop.max(axis=0)
        for i in range(popsize):
            if i == x_gb_idx:
                # global best - do some random walk
                pop_new[i] = pop[i]+(np.random.normal(size=dimensions) * gb_lam)
            else:
                if np.random.rand(1, 1) < alpha:
                    # mirror group
                    r_3 = np.random.rand(1, 1)[0][0]
                    xm_i_j = pop[i]*r_3 + ((1 -r_3)*gb)
                    pop_new[i] = (2 * xm_i_j) - pop[i]
                else:
                    # composition group
                    pop_new[i] = Lb_j + (Ub_j-Lb_j)*np.random.rand(1,dimensions )
            # apply the evolutionary bounding constraint scheme to the new point
            is_lower = np.argwhere(pop_new[i] < Lb)
            is_greater = np.argwhere(pop_new[i] > Ub)
            if len(is_lower) > 0:
                # apply the lower bound constraint
                # assumption - we use the same random number on all violations
                a = np.random.rand(1, 1)
                pop_new[i][is_lower]= (a * Lb[is_lower]) + ((1-a)*gb[is_lower])
            if len(is_greater) > 0:
                # apply the upper bound constraint
                # assumption - we use the same random number on all violations
                b = np.random.rand(1, 1)
                pop_new[i][is_greater] = (b * Ub[is_greater]) + (1 - b) * gb[is_greater]
            # calculate new fitness
            fit_new[i] = fobj(pop_new[i])
        for i in range(popsize):
            # determine points to keep
            # we could do this inline above?
            if fit_new[i] < fit[i]:
                fit[i] = fit_new[i]
                pop[i] = pop_new[i]
        # record stats if needed
        if j+1 in record_intervals:
            result = {
                'eval':j+1,
                'best': np.amin(fit),
                'std_dev': np.std(fit),
                'alpha': alpha
            }
            print(result)
            results.append(result)
    # return the best fitness and std devs. at the record_intervals
    return { 'popsize': popsize, 'evaluations': results, 'execution_time': time.time() - start_time }

def isa_runner(fobj, label, bounds, its=30, f_alpha=lambda i: 0.2, popsize=20, evals=1000):
    # generate a timestamp
    start_time = time.time()

    filename = 'ISA_%s_%s_%s_%s_%s.json'%('-'.join(label.split()), its, popsize, evals, int(start_time))
    results = []
    print('-'*100)
    print("Running ISA on %s with: popsize=%s, iterations=%s, evals per iteration=%s" % (label, popsize, its, evals))
    #fitnesses
    iter_fitnesses = []
    total_time = 0
    for i in range(its):
        print("Iteration: %s" % (i+1))
        result = isa(fobj, bounds, f_alpha=f_alpha, popsize=popsize, evals=evals)
        # last eval represents our results
        iter_fitnesses.append(result['evaluations'][-1]['best'])
        total_time+=result['execution_time']
        results.append(result)
    result = {
        'best': np.amin(iter_fitnesses),
        'median': np.median(iter_fitnesses),
        'mean': np.mean(iter_fitnesses),
        'std_dev': np.std(iter_fitnesses),
        'fitnesses': iter_fitnesses,
        'label': label,
        'iterations': its,
        'start_alpha': f_alpha(0),
        'end_alpha': f_alpha(evals-1),
        'popsize': popsize,
        'num_of_evaluations': evals,
        'total_execution_time': total_time,
        'avg_execution_time': total_time/its,
        "dimensions": len(bounds)
    }
    print(result)
    print("Writing Results to File %s"%filename)
    result['iteration_results'] = results
    with open(filename,'w') as result_file:
        result_file.write(json.dumps(result, indent=4))
    print('-' * 100)