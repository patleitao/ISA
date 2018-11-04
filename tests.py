from isa import isa_runner


#ISA Test Runs
isa_runner(lambda x: ((10**5)*x[0]**2) + x[1]**2 - (x[0]**2+x[1]**2)**2 + 10**-5*(x[0]**2 + x[1]**2)**4, 'Dekkers and Aarts', [(-20, 20)]*2, its=30, alpha=0.2, popsize=50, evals=1000)