import sys
import numpy as np
import pandas as pd
from utils import save_parameters, read_file, visualize


def normalize(mileage):
    mileage_mean = np.mean(mileage)
    mileage_std = np.std(mileage)
    return [(x - mileage_mean) / mileage_std for x in mileage]


def training(mileage, price):
    learning_rate = 0.02
    theta0 = 0
    theta1 = 0
    m = len(price)
    max_iterations = 1000
    epsilon = 1e-3

    for i in range(max_iterations):
        predictions = [theta0 + theta1 * x for x in mileage]
        errors = [predictions - actual for predictions, actual in zip(predictions, price)]
        temp0 = learning_rate * (1 / m) * sum(errors)
        temp1 = learning_rate * (1 / m) * (sum(errors * mileage for errors, mileage in zip(errors, mileage)))
        theta0 -= temp0
        theta1 -= temp1

        if abs(temp0) < epsilon and abs(temp1) < epsilon:
            print(f"Convergence after {i + 1} iterations")
            break

    else:
        print(f"Reached {max_iterations} iterations without convergence")

    return(theta0, theta1)


def revert_normalize(estimated_intercept, estimated_slope, mileage):
    mileage_mean = np.mean(mileage)
    mileage_std = np.std(mileage)
    estimated_intercept_original = estimated_intercept - (estimated_slope * mileage_mean / mileage_std)
    estimated_slope_original = estimated_slope / mileage_std

    return estimated_intercept_original, estimated_slope_original


def main():
    try:
        mileage, price = read_file()
        if len(sys.argv) == 1:
            mileage_normalized = normalize(mileage)
            estimated_intercept, estimated_slope = training(mileage_normalized, price)
            intercept, slope = revert_normalize(estimated_intercept, estimated_slope, mileage)
            regression_line = [intercept + slope * x for x in mileage]

            save_parameters(intercept, slope)
            visualize(mileage, price, regression_line)
        else:
            print("""
            Error: Check arguments
        """)
    except Exception as e:
        print(f"Error: {e}")
