# Penguin Clustering in Antarctica

This project aims to identify groups in a dataset of penguins in Antarctica. The dataset includes measurements such as culmen length, culmen depth, flipper length, body mass, and the sex of the penguins. Using K-Means clustering, we group the penguins into three clusters, potentially corresponding to three species: Adelie, Chinstrap, and Gentoo.

## Dataset

The dataset, `penguins.csv`, contains the following columns:
- `culmen_length_mm`: Culmen length (mm)
- `culmen_depth_mm`: Culmen depth (mm)
- `flipper_length_mm`: Flipper length (mm)
- `body_mass_g`: Body mass (g)
- `sex`: Penguin sex

## Requirements

- Python 3.x
- pandas
- matplotlib
- scikit-learn

You can install the required packages using the following command:

```bash
pip install pandas matplotlib scikit-learn