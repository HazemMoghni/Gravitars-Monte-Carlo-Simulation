import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.stats import norm

log_f = []  # Column for log(f)
log_h = []  # Column for log(h)

# Read data from the CSV file
with open('output 11.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        log_f.append(float(row[8]))  # Column index 8 for log(f)
        log_h.append(float(row[10]))  # Column index 10 for log(h)

# Create histograms for log(f) and log(h)
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)  # First subplot for log(f)
plt.hist(log_f, bins=500, density=True, color='gray', alpha=0.6,
         edgecolor='gray', linewidth=0.5)

# Plot the normal distribution curve
mu_f = 1.341827219
sigma_f = 0.521295942
x_f = np.linspace(min(log_f), max(log_f), 100)
y_f = norm.pdf(x_f, mu_f, sigma_f)
plt.plot(x_f, y_f, color='black', linestyle='dashed')

plt.xlabel(r'$\log_{10}(f_{\mathrm{GW}})$')
plt.ylabel('Density')
plt.xlim(-0.5, 3)
plt.xticks([-0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3])

plt.subplot(2, 1, 2)  # Second subplot for log(h)
plt.hist(log_h, bins=500, density=True, color='gray', alpha=0.6,
         edgecolor='gray', linewidth=0.5)

# Plot the normal distribution curve
mu_h = -29.47867884
sigma_h = 1.184416974
x_h = np.linspace(min(log_h), max(log_h), 100)
y_h = norm.pdf(x_h, mu_h, sigma_h)
plt.plot(x_h, y_h, color='black', linestyle='dashed')

plt.xlabel(r'$\log_{10}(h_0)$')
plt.ylabel('Density')
plt.xlim(-33, -26)
plt.xticks([-33, -32, -31, -30, -29, -28, -27, -26])

plt.tight_layout()  # To prevent overlapping of subplots

plt.show()