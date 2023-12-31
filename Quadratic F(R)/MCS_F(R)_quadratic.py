import numpy as np
import math
import csv
from scipy.optimize import root_scalar
from scipy.special import erfinv

# Conversions
kpc = 3.08567758128e19  # m
Yr = 3.15576e7  # s

# Constants
G = 6.6743e-11  # m^(3) kg^(-1) s^(-2)
c = 2.99792458e8  # m^(1) s^(-1)
pi = 3.14159265358979  # Dimensionless
e = 2.718281828459  # Dimensionless
I_zz = 1e38  # kg^(1) m^(2)
Birthrate = 0.01  # 1 per 100 Yr
Ti = 0  # Yr
Tf = 100e6  # Yr
N = math.ceil(Birthrate * Tf)
R_E = 8.2  # kpc (Galactic-Earth distance)
h_z = 0.075  # kpc
R_exp = 4.5  # kpc
a_r = 1.18285425  # Dimensionless normalizing constant
a_ellipticity = 1.010050628  # Dimensionless normalizing constant
F_R_constant = 1e5 # m^2
R_chosen = xe-5 # / m^2, choose value and change csv file name as you please

# Bounds
ri_min = 0  # kpc
ri_max = 15  # kpc
zi_min = 0  # kpc
phi_min = 0  # rad
phi_max = pi  # rad
Pi_min = 0  # s
Pi_avg = 0.09  # s, the log of this is overline(log_10 (P_i))
Pi_std = 0.53
age_min = 0  # Yr
age_max = Tf  # Yr
ellipticity_min = 1e-9  # Dimensionless
ellipticity_avg = 1e-7  # Dimensionless
ellipticity_max = 1e-6  # Dimensionless


def tilde_G(R):
    return G / (1+ 2 * F_R_constant * R)

def ri(p):
    def cdf_ri_p(ri, p):
        return a_r - (a_r * math.exp(-ri / R_exp) * (R_exp + ri)) / R_exp - p

    return root_scalar(cdf_ri_p, bracket=[ri_min, ri_max * 1.001], args=(p,)).root

def zi(p):
    return h_z * math.log(1 / (1 - p), e)


def ellipticity(p):
    def cdf_ellipticity_p(ellipticity, p):
        return a_ellipticity * (math.exp(-ellipticity_min / ellipticity_avg) - math.exp(-ellipticity / ellipticity_avg)) / (1 - math.exp(-ellipticity_max / ellipticity_avg)) - p
    return root_scalar(cdf_ellipticity_p, bracket=[ellipticity_min, ellipticity_max * 1.01], args=(p,)).root


def Pi(p):
    return Pi_avg * math.pow(10, math.sqrt(2) * Pi_std * erfinv(2 * p - 1))


def f_GW(Pi, ellipticity, age, R):
    return math.pow((math.pow(Pi, 4) / 16 + (128 * math.pow(pi, 4) * tilde_G(R) * math.pow(ellipticity, 2) * I_zz * (age * Yr)) / (5 * math.pow(c, 5))), -1 / 4)


def d(zi, phi, ri):
    return math.pow(
        math.pow(zi, 2) + math.pow(ri * math.cos(phi) - R_E, 2) + math.pow(ri * math.sin(phi), 2), 0.5)


def h_0(ellipticity, f_GW, d, R):
    return (4 * math.pow(pi, 2) * tilde_G(R) * ellipticity * I_zz * math.pow(f_GW, 2)) / (math.pow(c, 4) * (d * kpc))

with open('output_F(R)_R=x.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(
            ['log(f)', 'log(h)'])  # Write header row
    for _ in range(N):
        ri_output = ri(np.random.uniform(0, 1))
        zi_output = zi(np.random.uniform(0, 1))
        phi_output = np.random.uniform(0, phi_max)
        d_output = d(zi_output, phi_output, ri_output)
        ellipticity_output = ellipticity(np.random.uniform(0, 1))
        Pi_output = Pi(np.random.uniform(0, 1))
        age_output = np.random.uniform(0, age_max)
        f_GW_output = f_GW(Pi_output, ellipticity_output, age_output, R_chosen)
        f_GW_output_log = math.log(f_GW_output, 10)
        h_0_output = h_0(ellipticity_output, f_GW_output, d_output, R_chosen)
        h_0_output_log = math.log(h_0_output, 10)
        writer.writerow([f_GW_output_log, h_0_output_log])
