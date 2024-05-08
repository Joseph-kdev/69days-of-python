# with open("./002 weather-data.csv", mode="r") as f:
#     data = f.readlines()
    
# print(data)

# import csv

# with open("./002 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

#     print(temperature)

import pandas

# data = pandas.read_csv("./weather-data.csv")

# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data['temp'].to_list()

# print(data['temp'].max())

#get data in columns
# print(data.condition)

#get data in rows
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "John"],
#     "scores": [45, 83, 93]
# }

# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")

data = pandas.read_csv("./2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

grays = data[data["Primary Fur Color"] == "Gray"]
cinnamons = data[data["Primary Fur Color"] == "Cinnamon"]
blacks = data[data["Primary Fur Color"] == "Black"]

grays_total = len(grays)
cinnamons_total = len(cinnamons)
blacks_total = len(blacks)

color_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [ grays_total, cinnamons_total, blacks_total]
}

color_dataframe = pandas.DataFrame(color_data)
color_dataframe.to_csv("color_data.csv")