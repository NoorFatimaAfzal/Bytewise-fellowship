# Negative Reviews Clustering Analysis

## Overview
This repository contains a Python script that analyzes negative reviews from a dataset. It preprocesses the text data, applies TF-IDF vectorization, and utilizes K-means clustering to identify common themes in negative reviews. The result is a summary of the most significant terms associated with each cluster.

## Contents
- `negative_reviews_clustering_analysis.py`: The main script for analyzing negative reviews.
- `reviews.csv`: The dataset containing customer reviews with associated scores.

## Requirements
To run the script, you will need:
- Python 3.x
- The following Python libraries:
  - pandas
  - numpy
  - scikit-learn
  - nltk

You can install the required libraries using pip:
```bash
pip install pandas numpy scikit-learn nltk
