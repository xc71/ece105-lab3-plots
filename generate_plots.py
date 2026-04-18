"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np

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
