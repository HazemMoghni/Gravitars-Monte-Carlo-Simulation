import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.spatial import ConvexHull

log_f = []  # Column for log(f)
log_h = []  # Column for log(h)

with open('output_GR_low.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        if len(row) >= 11:  # Check if there are at least 11 columns in the row
            log_f.append(float(row[8]))  # Column index 8 for log(f)
            log_h.append(float(row[10]))  # Column index 10 for log(h)

plt.figure(figsize=(10, 6))

# Create 2D histogram
hist, xedges, yedges = np.histogram2d(log_f, log_h, bins=480, range=[[0, 3], [-34, -23]])
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Invert colors
plt.imshow(hist.T, origin='lower', extent=extent, cmap='gray_r', aspect='auto', vmax=hist.max())

# Read data from the text file
data = np.loadtxt('curve_data.txt')

# Separate the data into frequency (f) and strain (h) columns for each detector
frequencies = data[:, 0]
strains_aligo = data[:, 1]
strains_et = data[:, 2]
strains_ce = data[:, 3]

# Plot data for aLIGO with a line
plt.plot(np.log10(frequencies), np.log10(strains_aligo), color='blue', label='aLIGO')

# Plot data for ET with a line
plt.plot(np.log10(frequencies), np.log10(strains_et), color='green', label='Einstein Telescope')

# Plot data for Cosmic Explorer with a line
plt.plot(np.log10(frequencies), np.log10(strains_ce), color='purple', label='Cosmic Explorer')

# Draw a dotted line at y = -25
plt.axhline(y=-25, color='red', linestyle='-.')

plt.xlabel(r'$\log_{10}(f_{\mathrm{GW}})$')
plt.ylabel(r'$\log_{10}(h_0)$')

plt.xlim(0, 3)
plt.ylim(-34, -23)

# Set custom tick locations and labels for x-axis
plt.xticks([0, 0.5, 1, 1.5, 2, 2.5, 3])

# Set custom tick locations and labels for y-axis
plt.yticks([-34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23])

# Compute convex hull and plot it (black dashed line)
points = np.array(list(zip(log_f, log_h)))
hull = ConvexHull(points)
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k--', lw=1)

# Add a legend
plt.legend(loc='upper left')

# Add logarithmic gridlines (minor ticks) on both axes
plt.grid(which='both', linestyle='-', color='gray', alpha=0.5)

plt.show()
