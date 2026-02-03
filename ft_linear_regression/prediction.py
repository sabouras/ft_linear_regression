from utils import load_parameters


def predict_price(mileage, intercept, slope):
    return (mileage * slope + intercept)


def main():
    try:
        intercept, slope = load_parameters()
        mileage = int(input("Enter mileage (in km): "))
        if mileage < 0:
            print("Error: Mileage has to be a positive int")
            exit()
        predicted_price = predict_price(mileage, intercept, slope)
        if predicted_price < 0:
            predicted_price = 0
        print(f"The predicted price is {int(predicted_price)} .")
    except ValueError:
        print(f"Error: Mileage has to be an int")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()