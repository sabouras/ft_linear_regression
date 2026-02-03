import pandas as pd
import json
import matplotlib.pyplot as plt


def visualize(mileage, price, regression_line=None):
    try:
        plt.figure(figsize = (13,9))
        plt.scatter(mileage, price, marker='o', color='red')
        if regression_line is not None:
            plt.plot(mileage, regression_line, color='blue', linestyle='dashed')
        plt.xlabel("Mileage (in km)", fontsize=14, fontweight="bold")
        plt.ylabel('price', fontsize=14, fontweight="bold")
        plt.title("Car Price vs Mileage", fontsize=20, fontweight="bold", pad=20)
        plt.show()
        plt.close()
    except Exception as e:
        print(f"Error: {e}")


def read_file():
    try:
        data = pd.read_csv("data.csv")
        mileage = data['km'].tolist()
        price = data['price'].tolist()
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        exit()
    except Exception as e:
        print(f"Error reading dataset: {e}")
        exit()
    return mileage, price


def load_parameters():
    try:
        with open("parameters.txt", "r") as file:
            parameters = json.load(file)
        return parameters["theta0"], parameters["theta1"]
    except FileNotFoundError:
        print("Warning: Parameters file not found.")
        return 0, 0 
    except Exception as e:
        print(f"Error: {e}")
        exit()


def save_parameters(theta0, theta1):
    parameters = {"theta0": theta0, "theta1": theta1}
    try:
        with open("parameters.txt", "w") as file:
            json.dump(parameters, file)
    except Exception as e:
        print(f"Error: {e}")
        exit()

