import json
import numpy as np
import time
from utils import recording_intervals

'''
This implementation assumes (not explicit in paper):
1. velocity control (clamping)
2. bound handling method: randomly assign new location for each dimension that violated boundaries
3. global best is best ever, not best of current evaluation
One could consider adding constriction factor
'''


def pso(fobj, bounds, alpha1=2, alpha2=2, w_ranges=[0.9], v_max_perc=20 / 100, popsize=20, evals=1000):
    # recording intervals
    start_time = time.time()
    print("PSO: popsize: %s, evals: %s" % (popsize, evals))
    results = []
    record_intervals = recording_intervals(evals)

    # init the population (assuming bounds are same for all dimensions)
    dimensions = len(bounds)
    LB = bounds[0][0]
    UB = bounds[0][1]
    pop = np.random.uniform(low=LB, high=UB, size=(popsize, dimensions))
    v = np.zeros(pop.shape)
    v_max = v_max_perc * (UB - LB)
    gb_fit = np.inf
    pb_fit = np.full(popsize, np.inf)
    gb = np.zeros(dimensions)
    pb = np.array(pop)

    # run algorithm loop
    for i in range(evals):
        w = w_ranges[-1] if i > len(w_ranges) - 1 else w_ranges[i]
        pop_fit = np.apply_along_axis(fobj, 1, pop)
        for j in range(len(pop)):
            if pop_fit[j] < pb_fit[j]:
                pb_fit[j] = pop_fit[j]
                pb[j] = pop[j]
        current_best_fit = np.amin(pb_fit)
        if current_best_fit < gb_fit:
            gb_fit = current_best_fit
            gb = pop[np.argmin(pb_fit)]

        if i + 1 in record_intervals:
            result = {
                'eval': i + 1,
                'best': gb_fit,
                'std_dev': np.std(pop_fit),
                'w': w
            }
            print(result)
            results.append(result)

        # assign new velocities
        r1 = np.random.rand(dimensions)
        r2 = np.random.rand(dimensions)
        v = w * v + alpha1 * r1 * (pb - pop) + alpha2 * r2 * (gb - pop)
        # apply velocity control
        # v[v > v_max] = v_max
        # v[v < -v_max] = -v_max
        pop = pop + v
        # apply bound handling method
        pop[pop < LB] = np.random.uniform(low=LB, high=UB, size=1)
        pop[pop > UB] = np.random.uniform(low=LB, high=UB, size=1)

    # return the best fitness and std devs. at the record_intervals
    return {'popsize': popsize, 'evaluations': results, 'execution_time': time.time() - start_time}



def pso_runner(fobj, label, bounds, its=30, w_ranges=[0.9], popsize=20, evals=1000):
    # generate a timestamp
    start_time = time.time()
    filename = 'PSO_%s_%s_%s_%s_%s.json' % ('-'.join(label.split()), its, popsize, evals, int(start_time))
    results = []
    print('-' * 100)
    print("Running PSO on %s with: popsize=%s, iterations=%s, evals per iteration=%s" % (label, popsize, its, evals))
    # fitnesses
    iter_fitnesses = []
    total_time = 0
    for i in range(its):
        print("Iteration: %s" % (i + 1))
        result = pso(fobj, bounds, w_ranges=w_ranges, popsize=popsize, evals=evals)
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
        'start_w': w_ranges[0],
        'end_w': w_ranges[-1],
        'popsize': popsize,
        'num_of_evaluations': evals,
        'total_execution_time': total_time,
        'avg_execution_time': total_time/its,
        'dimensions': len(bounds)
    }
    print(result)
    print("Writing Results to File %s" % filename)
    result['iteration_results'] = results
    with open(filename, 'w') as result_file:
        result_file.write(json.dumps(result, indent=4))
    print('-' * 100)
