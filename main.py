from dataset import load_data
from tree import model, predict
from display import print_tree, ask


def main():
    features, play = load_data("data.csv")

    print("[1] Training on data.csv (" + str(len(play)) + " rows)...")
    tree = model(features, play)

    print("[2] Learned tree:")
    print_tree(tree)

    print("[3] Predict new day:")
    day = {
        "Weather":     ask("Weather", ["Sunny", "Overcast", "Rainy"]),
        "Temperature": ask("Temperature", ["Hot", "Mild", "Cool"]),
        "Humidity":    ask("Humidity", ["High", "Normal"]),
        "Windy":       ask("Windy", ["True", "False"]),
    }
    steps, label = predict(tree, day)
    print("        " + " → ".join(steps) + " → " + label)
    print("        Prediction: " + label.upper())


if __name__ == "__main__":
    main()
