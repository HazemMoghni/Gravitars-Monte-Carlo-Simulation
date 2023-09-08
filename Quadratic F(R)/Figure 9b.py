import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Define line styles for the curves
line_styles = ['-', '-.', ':', 'solid', ':', '-.', '-']

# Data for strain curves
curve_data = [
    {"mu_h": -27.24376692, "sigma_h": 1.080563193, "label": r"$R=-\frac{10^{-3}}{201} /\mathrm{m}^2$", "color": 'blue'},
    {"mu_h": -28.18041088, "sigma_h": 1.142365645, "label": r"$R=-\frac{10^{-4}}{21} /\mathrm{m}^2$", "color": 'blue'},
    {"mu_h": -29.00618053, "sigma_h": 1.172356577, "label": r"$R=-\frac{10^{-5}}{3} /\mathrm{m}^2$", "color": 'blue'},
    {"mu_h": -29.478957051208194, "sigma_h": 1.1829925682267526, "label": "$R=0$ (GR)", "color": 'black'},
    {"mu_h": -29.9518163, "sigma_h": 1.190216733, "label": "$R=10^{-5}/\mathrm{m}^2$", "color": 'red'},
    {"mu_h": -30.79186049, "sigma_h": 1.197020827, "label": "$R=10^{-4}/\mathrm{m}^2$", "color": 'red'},
    {"mu_h": -31.77337673, "sigma_h": 1.201148558, "label": "$R=10^{-3}/\mathrm{m}^2$", "color": 'red'},
]

# Create a subplot for strain (h)
plt.figure(figsize=(10, 6))
plt.xlabel(r'$\log_{10}(\tilde{h}_0)$')
plt.ylabel('Density')
plt.xlim(-35, -24)
plt.ylim(0, 0.4)
plt.xticks([-35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24])

# Lists to store top points of each bell curve
top_points_x = []
top_points_y = []

# Loop through the curve data and plot each strain curve with different line styles and colors
for i, data in enumerate(curve_data):
    x = np.linspace(-35, -24, 1000)
    y_h = norm.pdf(x, data["mu_h"], data["sigma_h"])
    label = data["label"]
    color = data["color"]

    # Find the top point of each bell curve
    top_point_x = x[np.argmax(y_h)]
    top_point_y = max(y_h)
    top_points_x.append(top_point_x)
    top_points_y.append(top_point_y)

    # Plot the bell curve with the specified color and line style
    plt.plot(x, y_h, linestyle=line_styles[i % len(line_styles)], color=color, label=label)

plt.legend()
plt.grid(True, linestyle='-', linewidth=0.5)
plt.show()
