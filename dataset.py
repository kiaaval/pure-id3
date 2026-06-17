import csv

from schema import feature


def load_data(path: str = "data.csv"):
    weather: feature = {"name": "Weather", "array": []}
    temperature: feature = {"name": "Temperature", "array": []}
    humidity: feature = {"name": "Humidity", "array": []}
    windy: feature = {"name": "Windy", "array": []}
    play: list[str] = []

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            weather["array"].append(row["Weather"])
            temperature["array"].append(row["Temperature"])
            humidity["array"].append(row["Humidity"])
            windy["array"].append(row["Windy"])
            play.append(row["Play"])

    features = [weather, temperature, humidity, windy]
    return features, play
