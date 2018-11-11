import numpy as np
import matplotlib.pyplot as plt
import json
from pprint import pprint

plt.style.use('ggplot')


# with open('results/pso/PSO_Ackley_30_50_10000_1541788326.json') as f:
#     pso_ackley_1 = json.load(f)
# with open('results/pso/PSO_Ackley_30_50_10000_1541789142.json') as f:
#     pso_ackley_2 = json.load(f)

easom = {}
rastigins = {}
ackley = {}
sphere = {}
schwefel = {}

def get_stds(file):
	stds = np.zeros(100)
	for iteration in file["iteration_results"]:
            for idx, evaluation in enumerate(iteration["evaluations"]):
    				stds[idx] += evaluation["std_dev"]
	stds = stds / 30.0
	return stds



# EASOM
with open('results/pso/PSO_Easom_30_25_1000_1541786688.json') as f:
    pso_easom = json.load(f)
easom['pso'] = get_stds(pso_easom)
with open('results/isa/ISA_Easom_30_25_1000_1541877064.json') as f:
    isa_easom_1 = json.load(f)
easom['isa_1'] = get_stds(isa_easom_1)
with open('results/isa/ISA_Easom_30_25_1000_1541877119.json') as f:
    isa_easom_3 = json.load(f)
easom['isa_3'] = get_stds(isa_easom_3)

# RASTIGINS
with open('results/pso/PSO_Rastigins_30_50_10000_1541881241.json') as f:
    pso_rastigins = json.load(f)
rastigins['pso'] = get_stds(pso_rastigins)
with open('results/isa/ISA_Rastigins_30_50_10000_1541876870.json') as f:
    isa_rastigins_1 = json.load(f)
rastigins['isa_1'] = get_stds(isa_rastigins_1)
with open('results/isa/ISA_Rastigins_30_50_10000_1541879572.json') as f:
    isa_rastigins_3 = json.load(f)
rastigins['isa_3'] = get_stds(isa_rastigins_3)


# ACKLEY
with open('results/pso/PSO_Ackley_30_50_10000_1541881170.json') as f:
    pso_ackley = json.load(f)
ackley['pso'] = get_stds(pso_ackley)
with open('results/isa/ISA_Ackley_30_50_10000_1541876955.json') as f:
    isa_ackley_1 = json.load(f)
ackley['isa_1'] = get_stds(isa_ackley_1)
with open('results/isa/ISA_Ackley_30_50_10000_1541879540.json') as f:
    isa_ackley_3 = json.load(f)
ackley['isa_3'] = get_stds(isa_ackley_3)

# SPHERE
with open('results/pso/PSO_Sphere_30_50_10000_1541880976.json') as f:
    pso_sphere = json.load(f)
sphere['pso'] = get_stds(pso_sphere)
with open('results/isa/ISA_Sphere_30_50_10000_1541877006.json') as f:
    isa_easom_1 = json.load(f)
sphere['isa_1'] = get_stds(isa_sphere_1)
with open('results/isa/ISA_Sphere_30_50_10000_1541879513.json') as f:
    isa_sphere_3 = json.load(f)
sphere['isa_3'] = get_stds(isa_sphere_3)


# SCHWEFEL
with open('results/pso/PSO_Schwefel_30_50_10000_1541880690.json') as f:
    pso_schwefel = json.load(f)
schwefel['pso'] = get_stds(pso_schwefel)
with open('results/isa/ISA_Schwefel_30_50_10000_1541876536.json') as f:
    isa_schwefel_1 = json.load(f)
schwefel['isa_1'] = get_stds(isa_schwefel_1)
with open('results/isa/ISA_Schwefel_30_50_10000_1541879742.json') as f:
    isa_schwefel_3 = json.load(f)
schwefel['isa_3'] = get_stds(isa_schwefel_3)



# with open('results/pso/PSO_Ackley_30_50_10000_1541788326.json') as f:
#     pso_ackley_1 = json.load(f)
# with open('results/pso/PSO_Ackley_30_50_10000_1541788326.json') as f:
#     pso_ackley_1 = json.load(f)
# with open('results/pso/PSO_Ackley_30_50_10000_1541788326.json') as f:
#     pso_ackley_1 = json.load(f)
# with open('results/pso/PSO_Ackley_30_50_10000_1541788326.json') as f:
#     pso_ackley_1 = json.load(f)
# with open('results/pso/PSO_Ackley_30_50_10000_1541788326.json') as f:
#     pso_ackley_1 = json.load(f)
# with open('results/pso/PSO_Ackley_30_50_10000_1541788326.json') as f:
#     pso_ackley_1 = json.load(f)

# PLOT EASOM

# fig = plt.figure(figsize=(8, 4))
# ax = fig.add_subplot(111)
# for k in ['pso_1', 'pso_2', 'isa_1', 'isa_2', 'isa_3']:
#     	plt.plot(np.arange(1, 101), easom[k], label=k)
# ax.legend(loc=0)
# ax.set_xlabel('Evaluations')
# plt.show()

fig1 = plt.figure(figsize=(8, 4))
ax1 = fig1.add_subplot(111)
plt.plot(np.arange(1, 11)*10, easom['pso'][0:10], label='pso')
plt.plot(np.arange(1, 11)*10, easom['isa_1'][0:10], label='isa_1')
plt.plot(np.arange(1, 11)*10, easom['isa_3'][0:10], label='isa_3')
ax1.legend(loc=0)
ax1.set_xlabel('Evaluations')
ax1.ylabel('Standard deviation of population fitness')
plt.show()

fig2 = plt.figure(figsize=(8, 4))
ax2 = fig2.add_subplot(111)
plt.plot(np.arange(1, 11)*10, rastigins['pso'][0:10], label='pso')
plt.plot(np.arange(1, 11)*10, rastigins['isa_1'][0:10], label='isa_1')
plt.plot(np.arange(1, 11)*10, rastigins['isa_3'][0:10], label='isa_3')
ax2.legend(loc=0)
ax2.set_xlabel('Evaluations')
ax2.ylabel('Standard deviation of population fitness')
plt.show()



