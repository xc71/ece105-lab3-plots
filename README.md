# Lab 3 Sensor Plots

This project generates synthetic temperature sensor data and produces three publication-style visualizations: a scatter plot, a histogram, and a box plot.

## Installation

1. Activate the `ece105` conda environment.
2. Install the required packages with conda or mamba:

```bash
conda install numpy matplotlib
```

If you prefer mamba, use:

```bash
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example Output

The script generates one output file:

- `sensor_analysis.png`: a 1x3 figure containing a scatter plot of temperature versus time, an overlaid histogram comparing the two sensors, and a side-by-side box plot with the combined mean marked.

## AI Tools Used and Disclosure

I used GitHub Copilot to help draft and edit the Python script and README content for this project. It was used to generate reusable plotting functions, organize the documentation, and check that the README matched the script's outputs and usage. I verified the final result by reviewing the code and confirming that the script produces the expected `sensor_analysis.png` output when run with the documented dependencies.