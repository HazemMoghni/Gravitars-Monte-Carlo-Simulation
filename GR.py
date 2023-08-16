import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.6743e-11 # m^(3) kg^(-1) s^(-2)
c = 299792458 # m^(1) s^(-1)
pi = 3.14159265358979 # Dimensionless
I_zz = 10e38 # kg^(1) m^(2)
Birthrate = 0.01 # Once per century
Ti = 0 # Yr
Tf = 100e6 # Yr
N = Birthrate*Tf # Number of gravitars
R_E = 8.25 # kpc (Galactic-Earth distance)

# Bounds
ri_min = 0 # kpc
ri_max = 15 # kpc
zi_min = 0 # kpc
zi_max = 1 # kpc
Pi_min = 0 # s
Pi_avg = 0.1 # s
Pi_max = float('inf') # s
age_min = 0 # Yr
age_max = Tf # Yr
ellipticity_min = 10e-9 # Dimensionless
ellipticity_avg = 10e-8 # Dimensionless
ellipticity_max = 10e-5 # Dimensionless



def pdf_r(ri):

def pdf_z(zi):

def pdf_P(Pi):

def pdf_age(age):
    return 1/Tf

def pdf_ellipticity(ellipticity):

def intrinsic_strain(ri, zi, Pi, age, ellipticity):

def detectability(h_0, threshold):
    if h_0 >= threshold:
        return 1
    else:
        return 0

results = {'ri': [], 'zi': [], 'Pi': [], 'age': [], 'ellipticity': [], 'detectability': []}
for _ in range(N):
    ri = np.random.choice(np.linspace(ri_min, ri_max, num_points), p=pdf_r(np.linspace(ri_min, ri_max, num_points)))  # Sample ri from PDF
    zi = np.random.choice(np.linspace(zi_min, zi_max, num_points), p=pdf_z(np.linspace(zi_min, zi_max, num_points)))  # Sample zi from PDF
    Pi = np.random.choice(np.linspace(Pi_min, Pi_max, num_points), p=pdf_P(np.linspace(Pi_min, Pi_max, num_points)))  # Sample Pi from PDF
    age = np.random.choice(np.linspace(age_min, age_max, num_points), p=pdf_age(np.linspace(age_min, age_max, num_points)))  # Sample age from PDF
    ellipticity = np.random.choice(np.linspace(ellipticity_min, ellipticity_max, num_points), p=pdf_ellipticity(np.linspace(ellipticity_min, ellipticity_max, num_points)))  # Sample ellipticity from PDF
    
    h_0 = intrinsic_strain(ri, zi, Pi, age, ellipticity)
    detectability = decide_detectability(h_0, threshold)
    
    results['ri'].append(ri)
    results['zi'].append(zi)
    results['Pi'].append(Pi)
    results['age'].append(age)
    results['ellipticity'].append(ellipticity)
    results['detectability'].append(detectability)

variables = ['ri', 'zi', 'Pi', 'age', 'ellipticity']
plt.figure(figsize=(12, 8))
for var in variables:
    plt.hist(results[var], bins=30, alpha=0.5, label=var)
plt.xlabel('Variable Value')
plt.ylabel('Number of Stars')
plt.legend()
plt.show()
