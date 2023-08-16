import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.6743e-11 # m^(3) kg^(-1) s^(-2)
c = 299792458 # m^(1) s^(-1)
pi = 3.14159265358979 # Dimensionless
I_zz = 10e38 # kg^(1) m^(2)
Birthrate = 0.01 # 1 per 100 Yr
Ti = 0 # Yr
Tf = 100e6 # Yr
N = Birthrate * Tf # Number of gravitars
R_E = 8.25 # kpc (Galactic-Earth distance)

# Conversions
kpc = 3.08567758128e19 # m
Yr = 31556926 # s

# Bounds
ri_min = 0 * kpc # m
ri_max = 15 * kpc # m
zi_min = 0 * kpc # m
zi_max = 15 * kpc # m
Pi_min = 0 # s
Pi_avg = 0.1 # s
Pi_max = float('inf') # s
age_min = 0 * Yr # s
age_max = Tf * Yr # s
ellipticity_min = 10e-9 # Dimensionless
ellipticity_avg = 10e-8 # Dimensionless
ellipticity_max = 10e-5 # Dimensionless


import numpy as np
import matplotlib.pyplot as plt

class Gravitar:
    
    def pdf_r(self, ri):
        # Define your PDF for radial displacement ri
        # Example: return some_probability_density_function_for_r

    def pdf_z(self, zi):
        # Define your PDF for vertical displacement zi
        # Example: return some_probability_density_function_for_z

    def pdf_P(self, Pi):
        # Define your PDF for initial period of rotation Pi
        # Example: return some_probability_density_function_for_Pi

    def pdf_age(self, age):
        return 1 / Tf

    def pdf_ellipticity(self, ellipticity):
        # Define your PDF for ellipticity
        # Example: return some_probability_density_function_for_ellipticity
        
    def intrinsic_strain(self, ri, zi, Pi, age, ellipticity):
        # Define your function to calculate intrinsic strain amplitude
        # Example: return some_calculation_function_for_intrinsic_strain

    def decide_detectability(self, h_0, threshold):
        if h_0 >= threshold:
            return 1
        else:
            return 0

    def simulate(self, N):
        results = {'ri': [], 'zi': [], 'Pi': [], 'age': [], 'ellipticity': [], 'detectability': []}
        for _ in range(N):
            ri = np.random.choice(np.linspace(ri_min, ri_max, N), p=self.pdf_r(np.linspace(ri_min, ri_max, N)))
            zi = np.random.choice(np.linspace(zi_min, zi_max, N), p=self.pdf_z(np.linspace(zi_min, zi_max, N)))
            Pi = np.random.choice(np.linspace(Pi_min, Pi_max, N), p=self.pdf_P(np.linspace(Pi_min, Pi_max, N)))
            age = np.random.choice(np.linspace(age_min, age_max, N), p=self.pdf_age(np.linspace(age_min, age_max, N)))
            ellipticity = np.random.choice(np.linspace(ellipticity_min, ellipticity_max, N), p=self.pdf_ellipticity(np.linspace(ellipticity_min, ellipticity_max, N)))
            
            h_0 = self.intrinsic_strain(ri, zi, Pi, age, ellipticity)
            detectability = self.decide_detectability(h_0, threshold)
            
            results['ri'].append(ri)
            results['zi'].append(zi)
            results['Pi'].append(Pi)
            results['age'].append(age)
            results['ellipticity'].append(ellipticity)
            results['detectability'].append(detectability)
        
        return results

# Create an instance of the Gravitar class
simulator = Gravitar()

# Simulate gravitars with N
simulation_results = simulator.simulate(N)

# Plot the results
variables = ['ri', 'zi', 'Pi', 'age', 'ellipticity']
plt.figure(figsize=(12, 8))
for var in variables:
    plt.hist(simulation_results[var], bins=30, alpha=0.5, label=var)
plt.xlabel('Variable Value')
plt.ylabel('Number of Stars')
plt.legend()
plt.show()
