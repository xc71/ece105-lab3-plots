"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np
import matplotlib.pyplot as plt

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

def generate_data(seed):
    """Generate synthetic temperature sensor data.
    
    Creates temperature readings from two simulated sensors over a time period.
    Sensor A has a lower mean (25°C) with smaller variance (std=3°C), while
    Sensor B has a higher mean (27°C) with larger variance (std=4.5°C).
    
    Parameters
    ----------
    seed : int
        Random seed for reproducibility. Typically the last 4 digits of
        a Drexel ID to ensure different users get different random sequences.
    
    Returns
    -------
    sensor_a : ndarray
        Temperature readings (°C) from Sensor A with shape (200,) and dtype float64.
        Normally distributed with mean=25.0 and std=3.0.
    sensor_b : ndarray
        Temperature readings (°C) from Sensor B with shape (200,) and dtype float64.
        Normally distributed with mean=27.0 and std=4.5.
    timestamps : ndarray
        Time values (seconds) with shape (200,) and dtype float64.
        Uniformly distributed over [0, 10] seconds, sorted in ascending order.
    """
    # Parameters
    n = 200
    mean_a, std_a = 25.0, 3.0
    mean_b, std_b = 27.0, 4.5
    
    # Initialize random number generator with seed
    rng = np.random.default_rng(seed)
    
    # Generate sensor readings
    sensor_a = rng.normal(loc=mean_a, scale=std_a, size=n)
    sensor_b = rng.normal(loc=mean_b, scale=std_b, size=n)
    
    # Generate timestamps uniformly from 0 to 10 seconds, sorted
    timestamps = np.sort(rng.uniform(0, 10, size=n))
    
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor temperature readings versus time on an Axes object.
    
    Creates a scatter plot with two sensor datasets overlaid on the same axes.
    Sensor A points are colored blue and Sensor B points are colored orange.
    
    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings (°C) from Sensor A with shape (n,) and dtype float64.
    sensor_b : ndarray
        Temperature readings (°C) from Sensor B with shape (n,) and dtype float64.
    timestamps : ndarray
        Time values (seconds) with shape (n,) and dtype float64.
    ax : matplotlib.axes.Axes
        Axes object on which to draw the scatter plot. Modified in place.
    
    Returns
    -------
    None
        The function modifies the Axes object in place and does not return a value.
    
    Notes
    -----
    The plot includes axis labels with units, a title, legend, and light grid.
    """
    
    ax.scatter(timestamps, sensor_a, color='tab:blue', alpha=0.75, s=24, label='Sensor A')
    ax.scatter(timestamps, sensor_b, color='tab:orange', alpha=0.75, s=24, label='Sensor B')
    
    ax.set_xlabel('Timestamp (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Readings vs Time')
    ax.legend()
    ax.grid(alpha=0.25)

# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# the histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid sensor temperature histograms on an Axes object.

    Creates an overlaid histogram comparison for the two sensor datasets.
    Sensor A is shown in blue and Sensor B is shown in orange, with vertical
    dashed lines marking each sensor mean.

    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings (°C) from Sensor A with shape (n,) and dtype float64.
    sensor_b : ndarray
        Temperature readings (°C) from Sensor B with shape (n,) and dtype float64.
    ax : matplotlib.axes.Axes
        Axes object on which to draw the histogram. Modified in place.

    Returns
    -------
    None
        The function modifies the Axes object in place and does not return a value.

    Notes
    -----
    The histogram uses 30 bins and includes labels, a title, a legend, and a
    light horizontal grid for readability.
    """
    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)

    ax.hist(sensor_a, bins=30, alpha=0.5, color='tab:blue', label='Sensor A', edgecolor='black', linewidth=0.5)
    ax.hist(sensor_b, bins=30, alpha=0.5, color='tab:orange', label='Sensor B', edgecolor='black', linewidth=0.5)

    ax.axvline(mean_a, color='tab:blue', linestyle='--', linewidth=2, label=f'Sensor A mean: {mean_a:.1f}°C')
    ax.axvline(mean_b, color='tab:orange', linestyle='--', linewidth=2, label=f'Sensor B mean: {mean_b:.1f}°C')

    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution Comparison: Sensor A vs Sensor B')
    ax.legend()
    ax.grid(alpha=0.25, axis='y')

# Create plot_boxplot(sensor_a, sensor_b, ax) that draws
# the box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot a side-by-side box plot comparison on an Axes object.

    Creates a box plot comparing the temperature distributions of Sensor A
    and Sensor B. The plot includes a horizontal dashed line showing the
    overall mean of the two sensors combined.

    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings (°C) from Sensor A with shape (n,) and dtype float64.
    sensor_b : ndarray
        Temperature readings (°C) from Sensor B with shape (n,) and dtype float64.
    ax : matplotlib.axes.Axes
        Axes object on which to draw the box plot. Modified in place.

    Returns
    -------
    None
        The function modifies the Axes object in place and does not return a value.

    Notes
    -----
    The box plot mirrors the notebook visualization with labeled sensor groups,
    a highlighted median line, and a reference line at the combined mean.
    """
    overall_mean = np.mean([sensor_a, sensor_b])

    ax.boxplot(
        [sensor_a, sensor_b],
        labels=['Sensor A', 'Sensor B'],
        patch_artist=True,
        boxprops=dict(facecolor='lightblue', alpha=0.7),
        medianprops=dict(color='red', linewidth=2),
        whiskerprops=dict(linewidth=1.5),
        capprops=dict(linewidth=1.5),
    )

    ax.axhline(overall_mean, color='black', linestyle='--', linewidth=2, label=f'Overall Mean: {overall_mean:.2f}°C')

    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Distribution Comparison: Box Plot')
    ax.legend()
    ax.grid(alpha=0.25, axis='y')