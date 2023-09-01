import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.spatial import ConvexHull
from matplotlib.colors import Normalize

log_f = []  # Column for log(f)
log_h = []  # Column for log(h)

with open('output 11.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        log_f.append(float(row[8]))  # Column index 8 for log(f)
        log_h.append(float(row[10]))  # Column index 10 for log(h)

plt.figure(figsize=(10, 6))

# Create 2D histogram
hist, xedges, yedges = np.histogram2d(log_f, log_h, bins=475, range=[[0, 3], [-34, -24]])
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Invert colors
plt.imshow(hist.T, origin='lower', extent=extent, cmap='gray_r', aspect='auto', vmax=hist.max())

plt.xlabel(r'$\log_{10}(f_{\mathrm{GW}})$')
plt.ylabel(r'$\log_{10}(h_0)$')

plt.xlim(0, 3)
plt.ylim(-34, -24)

# Set custom tick locations and labels for x-axis
plt.xticks([0, 0.5, 1, 1.5, 2, 2.5, 3])

# Set custom tick locations and labels for y-axis
plt.yticks([-34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24])

# Compute convex hull and plot it (black dashed line)
points = np.array(list(zip(log_f, log_h)))
hull = ConvexHull(points)
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k--', lw=1)

# Create color bar to the right
cax = plt.axes([0.92, 0.15, 0.02, 0.6])
norm = Normalize(vmin=0, vmax=100)
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap='gray_r'), cax=cax)

plt.show()