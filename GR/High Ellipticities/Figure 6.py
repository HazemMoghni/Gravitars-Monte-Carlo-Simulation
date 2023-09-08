import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.stats import norm

log_f = []  # Column for log(f)
log_h = []  # Column for log(h)

# Read data from the CSV file
with open('output_GR_high.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        log_f.append(float(row[8]))  # Column index 8 for log(f)
        log_h.append(float(row[10]))  # Column index 10 for log(h)

# Calculate mu (average) and sigma (standard deviation) for log(f) and log(h)
mu_f = np.mean(log_f)
sigma_f = np.std(log_f)
mu_h = np.mean(log_h)
sigma_h = np.std(log_h)

# Print mu and sigma for log(f) and log(h)
print(f"mu_f (log(f) average): {mu_f}")
print(f"sigma_f (log(f) standard deviation): {sigma_f}")
print(f"mu_h (log(h) average): {mu_h}")
print(f"sigma_h (log(h) standard deviation): {sigma_h}")

# Create histograms for log(f) and log(h)
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)  # First subplot for log(f)
plt.hist(log_f, bins=500, density=True, color='gray', alpha=0.6,
         edgecolor='gray', linewidth=0.5)

plt.xlabel(r'$\log_{10}(f_{\mathrm{GW}})$')
plt.ylabel('Density')
plt.xlim(-0.5, 3)
plt.ylim(0, 0.8)
plt.xticks([-0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3])
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
plt.grid(True, linestyle='-', linewidth=0.5)

plt.subplot(2, 1, 2)  # Second subplot for log(h)
plt.hist(log_h, bins=500, density=True, color='gray', alpha=0.6,
         edgecolor='gray', linewidth=0.5)

plt.xlabel(r'$\log_{10}(h_0)$')
plt.ylabel('Density')
plt.xlim(-33, -26)
plt.ylim(0, 0.35)  # Corrected y-axis limits
plt.xticks([-33, -32, -31, -30, -29, -28, -27, -26])
plt.grid(True, linestyle='-', linewidth=0.5)

plt.tight_layout()  # To prevent overlapping of subplots

plt.show()
