import csv
import numpy as np

# Read data from the CSV file and create a list of rows
csv_data = []

with open('output_GR_low.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header row
    csv_data.append(header)  # Store the header

    for row in reader:
        csv_data.append(row)  # Store each row

# Extract CSV frequencies
csv_frequencies = [float(row[7]) for row in csv_data]  # 8th column for frequency

# Read data from the TXT file
txt_data = np.loadtxt('Detectors.txt')
txt_frequencies = txt_data[:, 0]
txt_strains_2nd = txt_data[:, 1]  # 2nd column for strain
txt_strains_3rd = txt_data[:, 2]  # 3rd column for strain
txt_strains_4th = txt_data[:, 3]  # 4th column for strain

# Create a mask to filter CSV frequencies within the range of TXT frequencies
mask = (csv_frequencies >= np.min(txt_frequencies)) & (csv_frequencies <= np.max(txt_frequencies))

# Find the corresponding TXT strain values and add them to CSV
for i in range(1, len(csv_data)):  # Start from the second row (skipping the header)
    if mask[i]:  # Check if this star's frequency is within the TXT range
        star_frequency = float(csv_data[i][7])  # Frequency from the CSV
        nearest_txt_frequency = txt_frequencies[np.argmin(np.abs(txt_frequencies - star_frequency))]
        csv_data[i].append(
            str(nearest_txt_frequency))  # Append the nearest TXT frequency to the 12th column

        # Find the corresponding TXT strain values and write them to CSV columns 13th, 14th, and 15th
        txt_index = np.where(txt_frequencies == nearest_txt_frequency)[0][0]
        csv_data[i].extend([str(txt_strains_2nd[txt_index]), str(txt_strains_3rd[txt_index]), str(txt_strains_4th[txt_index])])

# Write the updated data back to the CSV file
with open('output_GR_low.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
