import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Read data from the CSV file
csv_frequencies = []
csv_strains = []
with open('output 22.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        csv_frequencies.append(float(row[7]))  # 8th column for frequency
        csv_strains.append(float(row[9]))  # 10th column for strain

# Read data from the TXT file
txt_data = np.loadtxt('Data.txt')
txt_frequencies = txt_data[:, 0]
txt_strains = txt_data[:, 2]  # 3rd column for Cosmic Explorer's strains

# Filter CSV frequencies to be within the range of TXT frequencies
filtered_indices = np.where((csv_frequencies >= np.min(txt_frequencies)) & (csv_frequencies <= np.max(txt_frequencies)))
filtered_csv_frequencies = np.array(csv_frequencies)[filtered_indices]
filtered_csv_strains = np.array(csv_strains)[filtered_indices]

# Interpolate strain values for filtered CSV frequencies
strain_interpolator = interp1d(txt_frequencies, txt_strains, kind='linear')
estimated_strains = strain_interpolator(filtered_csv_frequencies)

# Compare strains and store boolean values
comparison_results = estimated_strains >= filtered_csv_strains

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(np.log10(filtered_csv_frequencies), bins=5, weights=comparison_results, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel(r'$\log_{10}(f_{\mathrm{GW}})$')
plt.ylabel('Count')
plt.grid(True)
plt.show()
