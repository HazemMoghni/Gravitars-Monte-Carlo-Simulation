import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
G = 6.6743e-11  # m^(3) kg^(-1) s^(-2)
c = 299792458  # m^(1) s^(-1)
pi = 3.14159265358979  # Dimensionless
e = 2.718281828459  # Dimensionless
I_zz = 1e38  # kg^(1) m^(2)
Birthrate = 0.01  # 1 per 100 Yr
Ti = 0  # Yr
Tf = 100e6  # Yr
N = Birthrate * Tf  # Number of gravitars
R_E = 8.2 * kpc  # m (Galactic-Earth distance)
h_z = 0.075 * kpc  # m
R_exp = 4.5 * kpc  # m
a = 1.18285  # dimensionless
tau = -2.46493285798560e-28

# Conversions
kpc = 3.08567758128e19  # m
Yr = 31557600  # s

# Bounds
ri_min = 0 * kpc  # m
ri_max = 15 * kpc  # m
zi_min = 0 * kpc  # m
zi_max = float('inf')  # m
phi_min = 0  # rad
phi_max = pi  # rad
Pi_min = 0  # s
Pi_avg = 0.1  # s
Pi_std = 0.1  # s
Pi_max = float('inf')  # s
age_min = 0  # s
age_max = Tf * Yr  # s
ellipticity_min = 10e-9  # Dimensionless
ellipticity_avg = 10e-8  # Dimensionless
ellipticity_max = 10e-5  # Dimensionless


class Gravitar:
    def pdf_r(self, ri):
        return a * ri / math.pow(R_exp, 2) * math.exp(-ri / R_exp)

    def pdf_z(self, zi):
        return 1 / (2 * h_z) * math.exp(- zi / h_z)

    def pdf_phi(self, phi):
        return 1 / pi

    def pdf_P(self, Pi):
        return math.log(e, 10) / (Pi * Pi_avg * math.pow(2*pi, 0.5)) * math.exp(- math.pow(math.log(Pi, 10) - Pi_avg, 2) / (2 * math.pow(Pi_std, 2)))

    def pdf_age(self, age):
        return 1 / Tf

    def pdf_ellipticity(self, ellipticity):
        return math.exp(-ellipticity / tau) / (tau * (1 - math.exp(-ellipticity_max / tau)))

    def f_GW(self, Pi, ellipticity, age):
        return math.pow((math.pow(Pi, 4) / 16 + (128 * math.pow(pi, 4) * G * ellipticity**2 * I_zz * age) / (5 * math.pow(c, 5))), -1/4)

    def d(self, ri, zi, phi):
        return math.pow((zi**2 + (R_E - math.cos(phi) * ri)**2 + (math.sin(phi) * ri)**2), 0.5)

    def h_0(self, ri, zi, phi, Pi, age, ellipticity):
        return (4 * math.pow(pi, 2) * G * ellipticity * I_zz * self.f_GW(Pi, ellipticity, age)**2) / (math.pow(c, 4) * self.d(ri, zi, phi))

    def decide_detectability(self, h_0, threshold):
        if h_0 >= threshold:
            return 1
        else:
            return 0

    def simulate(self, N):
        results = {'ri': [], 'zi': [], 'phi': [], 'Pi': [], 'age': [], 'e': [], 'detectability': []}
        for _ in range(N):
            ri = np.random.choice(np.linspace(ri_min, ri_max, N), p=self.pdf_r(np.linspace(ri_min, ri_max, N)))
            zi = np.random.choice(np.linspace(zi_min, zi_max, N), p=self.pdf_z(np.linspace(zi_min, zi_max, N)))
            phi = np.random.choice(np.linspace(phi_min, phi_max, N), p=self.pdf_phi(np.linspace(phi_min, phi_max, N)))
            Pi = np.random.choice(np.linspace(Pi_min, Pi_max, N), p=self.pdf_P(np.linspace(Pi_min, Pi_max, N)))
            age = np.random.choice(np.linspace(age_min, age_max, N), p=self.pdf_age(np.linspace(age_min, age_max, N)))
            e = np.random.choice(np.linspace(ellipticity_min, ellipticity_max, N), p=self.pdf_ellipticity(np.linspace(ellipticity_min, ellipticity_max, N)))

            h_0 = self.h_0(ri, zi, phi, Pi, age, e)
            detectability = self.decide_detectability(h_0, threshold)  # You need to define threshold

            results['ri'].append(ri)
            results['zi'].append(zi)
            results['phi'].append(phi)
            results['Pi'].append(Pi)
            results['age'].append(age)
            results['ellipticity'].append(e)
            results['detectability'].append(detectability)

        return results


# Create an instance of the Gravitar class
simulator = Gravitar()

# Simulate gravitars with N
simulation_results = simulator.simulate(N)

# Plot the results
# variables = ['ri', 'zi', 'phi', 'Pi', 'age', 'ellipticity']
# plt.figure(figsize=(12, 8))
# for var in variables:
#     plt.hist(simulation_results[var], bins=30, alpha=0.5, label=var)
# plt.xlabel('Variable Value')
# plt.ylabel('Number of Stars')
# plt.legend()
# plt.show()

# Save the results to a CSV file
csv_filename = 'gravitar_simulation_results.csv'
with open(csv_filename, mode='w', newline='') as csvfile:
    fieldnames = ['ri', 'zi', 'phi', 'Pi', 'age', 'ellipticity', 'detectability']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(N):
        writer.writerow({
            'ri': simulation_results['ri'][i],
            'zi': simulation_results['zi'][i],
            'phi': simulation_results['phi'][i],
            'Pi': simulation_results['Pi'][i],
            'age': simulation_results['age'][i],
            'e': simulation_results['e'][i],
            'detectability': simulation_results['detectability'][i]
        })
