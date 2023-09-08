import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Define line styles for the curves
line_styles = ['-', '-.', ':', 'solid', ':', '-.', '-']

# Data for frequency curves
curve_data = [
    {"mu_f": 1.308087469, "sigma_f": 0.473810507, "label": r"$R=-\frac{10^{-3}}{201} /\mathrm{m}^2$", "color": 'blue'},
    {"mu_f": 1.330363658, "sigma_f": 0.50208803, "label": r"$R=-\frac{10^{-4}}{21} /\mathrm{m}^2$", "color": 'blue'},
    {"mu_f": 1.339600075, "sigma_f": 0.515664635, "label": r"$R=-\frac{10^{-5}}{3} /\mathrm{m}^2$", "color": 'blue'},
    {"mu_f": 1.3422572776816433, "sigma_f": 0.5206344440291812, "label": "$R=0$ (GR)", "color": 'black'},
    {"mu_f": 1.344388273, "sigma_f": 0.524092914, "label": "$R=10^{-5}/\mathrm{m}^2$", "color": 'red'},
    {"mu_f": 1.346669162, "sigma_f": 0.527444782, "label": "$R=10^{-4}/\mathrm{m}^2$", "color": 'red'},
    {"mu_f": 1.346449228, "sigma_f": 0.52934649, "label": "$R=10^{-3}/\mathrm{m}^2$", "color": 'red'},
]

# Create a subplot for frequency (f)
plt.figure(figsize=(10, 6))
plt.xlabel(r'$\log_{10}(\tilde{f}_{\mathrm{GW}})$')
plt.ylabel('Density')
plt.xlim(-0.5, 3)
plt.ylim(0, 0.9)
plt.xticks([-0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3])

# Lists to store top points of each bell curve
top_points_x = []
top_points_y = []

# Loop through the curve data and plot each frequency curve with different line styles and colors
for i, data in enumerate(curve_data):
    x = np.linspace(-0.5, 3, 1000)
    y_f = norm.pdf(x, data["mu_f"], data["sigma_f"])
    label = data["label"]
    color = data["color"]

    # Find the top point of each bell curve
    top_point_x = x[np.argmax(y_f)]
    top_point_y = max(y_f)
    top_points_x.append(top_point_x)
    top_points_y.append(top_point_y)

    # Plot the bell curve with the specified color and line style
    plt.plot(x, y_f, linestyle=line_styles[i % len(line_styles)], color=color, label=label)

plt.legend()
plt.grid(True, linestyle='-', linewidth=0.5)
plt.show()
