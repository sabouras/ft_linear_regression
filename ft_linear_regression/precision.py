from utils import read_file, load_parameters
import math


def get_rmse(actual_p, predicted_p):
    mse = sum((p - a) ** 2 for p, a in zip(predicted_p, actual_p)) / len(actual_p)
    return math.sqrt(mse)


def main():
    mileage, actual_price = read_file()
    theta0, theta1 = load_parameters()

    predicted_price = [km * theta1 + theta0 for km in mileage]

    rmse = get_rmse(actual_price, predicted_price)
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

if __name__ == "__main__":
    main()