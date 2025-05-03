with open("./weather_data.csv") as weather_file:
    weather_data = weather_file.readlines()
    print(weather_data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for rows in data:
        if rows[1] != "temp":
            temperature.append(int(rows[1]))
    print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])