import json
import csv

file_path_txt = "C:/Users/ASUS/OneDrive/Desktop/test_file.txt"
file_path_json = "C:/Users/ASUS/OneDrive/Desktop/json_file.json"
file_path_csv = "C:/Users/ASUS/OneDrive/Desktop/csv_file.csv"


try:
    with open(file_path_txt , "r") as file:
        content = file.read()
        print(content)

    with open(file_path_json , "r") as file:
        content = json.load(file)
        print(content)

    with open(file_path_csv , "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        #   print(line[0])

except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to open this file")