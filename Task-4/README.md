# Logistic Regression Feature Selection

This project demonstrates how to perform feature selection using logistic regression to identify which single feature provides the best accuracy for predicting an outcome variable.

## Description

The script loads a dataset and iterates through each feature (excluding the target variable) to fit a logistic regression model. It evaluates the accuracy of the model for each feature and identifies the feature that yields the highest accuracy.

## Requirements

- Python 3.x
- pandas
- numpy
- statsmodels

You can install the required libraries using pip:

```bash
pip install pandas numpy statsmodels
