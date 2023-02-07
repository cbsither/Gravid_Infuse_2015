from poisson_ratio_test import _zstat_generic2, poisson_twosample
from species_class import Species
import matplotlib.pyplot as plt
import numpy as np


japonicus = Species(file_path='../data/MosqColGravidTrap_JohnSither_Final2.csv', species='japonicus')
japonicus.extract()

lambda_estimate_oak1, lambda_estimate_grass1 = japonicus.oak_total / japonicus.time_val, japonicus.grass_total / japonicus.time_val
emp_lambda_oak, emp_lambda_grass = np.sum(japonicus.oak_data) / japonicus.time_val, japonicus.grass_total / japonicus.time_val

rate_1 = np.random.poisson(lambda_estimate_oak1, 1000000)
rate_2 = np.random.poisson(lambda_estimate_grass1, 1000000)

bins = np.arange(0, 40)

plt.hist(japonicus.oak_by_date, bins=bins, color='blue', alpha=0.3, label=f'Oak Data', density=True)
plt.hist(rate_1, color='green', bins=bins, alpha=0.3, label=f'Simulated Oak Data, \u03BB={round(lambda_estimate_oak1, 2)}', density=True)
plt.axvline(lambda_estimate_oak1, color='blue', ymax=0.8)
plt.title("Aedes japonicus", style='italic')
plt.xlabel('Sample Counts')
plt.ylabel('Density')
plt.legend()
plt.savefig(f"../figs/japonicus/japonicus_poisson_histogram_emp_data_oak.png")
plt.clf()

plt.hist(japonicus.grass_by_date, bins=bins, color='blue', alpha=0.3, label=f'Grass Data', density=True)
plt.hist(rate_2, color='green', bins=bins, alpha=0.3, label=f'Simulated Grass Data, \u03BB={round(lambda_estimate_grass1, 2)}', density=True)
plt.axvline(lambda_estimate_grass1, color='blue', ymax=0.8)
plt.title("Aedes japonicus", style='italic')
plt.xlabel('Sample Counts')
plt.ylabel('Density')
plt.legend()
plt.savefig(f"../figs/japonicus/japonicus_poisson_histogram_emp_data_grass.png")
plt.clf()


plt.hist(rate_1, color='blue', alpha=0.3, label=f'Oak Infusion, \u03BB={round(lambda_estimate_grass1, 2)}', density=True)
plt.hist(rate_2, color='green', alpha=0.3, label=f'Grass Infusion, \u03BB={round(lambda_estimate_oak1, 2)}', density=True)
plt.axvline(lambda_estimate_grass1, color='green', ymax=0.8)
plt.axvline(lambda_estimate_oak1, color='blue', ymax=0.8)
plt.title("Aedes japonicus", style='italic')
plt.xlabel('Simulated Sample Counts')
plt.ylabel('Density')
plt.legend()
plt.savefig(f"../figs/japonicus/japonicus_poisson_histogram.png")
print(f"lambda Grass: {lambda_estimate_grass1} , lambda Oak: {lambda_estimate_oak1}")

#### Poisson Rate Test
print("Null Ratio = 1")
stats_dict = {}
s1, pv1 = poisson_twosample(japonicus.oak_total, japonicus.time_val, japonicus.grass_total, japonicus.time_val, method='wald', ratio_null=1, alternative='s')
stats_dict['wald'] = [s1, pv1, lambda_estimate_grass1, lambda_estimate_oak1]
print('wald', s1, pv1, '\n')
s1, pv1 = poisson_twosample(japonicus.oak_total, japonicus.time_val, japonicus.grass_total, japonicus.time_val, method='score', ratio_null=1, alternative='s')
stats_dict['score'] = [s1, pv1, lambda_estimate_grass1, lambda_estimate_oak1]
print('score', s1, pv1, '\n')
s1, pv1 = poisson_twosample(japonicus.oak_total, japonicus.time_val, japonicus.grass_total, japonicus.time_val, method='sqrt', ratio_null=1, alternative='s')
stats_dict['sqrt'] = [s1, pv1, lambda_estimate_grass1, lambda_estimate_oak1]
print('sqrt', s1, pv1, '\n')


with open('../tables/japonicus_test.csv', 'w') as ff:
    ff.write('test,oak_lambda,grass_lambda,stat,p_value\n')
    for i, j in stats_dict.items():
        ff.write(f'{i},{j[3]},{j[2]},{j[0]},{j[1]}\n')

    ff.close()


