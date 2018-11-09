import math


#def recording_intervals(evals):
#    max = int(math.ceil(math.log(evals) / math.log(2)))
#    max = max if max <= 10 else 10
#    intervals = [2 ** i for i in range(1,max)]
#    remain = int(math.ceil((evals - (2**max))/1000))
#    intervals.extend([i*1000 for i in range(1,remain+1)])
#    intervals.append(evals)
#    return intervals


def recording_intervals(evals):
    return [i*10 for i in range(1,math.ceil(evals/10)+1)]
