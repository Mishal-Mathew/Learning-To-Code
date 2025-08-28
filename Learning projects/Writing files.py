# (.txt , .json , .csv)

import csv
import json

Names = ["Aang" , "Katara", "Suko", "Toph", "Appa", "Momo"]
text_file = "C:/Users/ASUS/OneDrive/Desktop/test_file.txt"

Avatar = {"Name" : "Katara", 
          "Age" : 112 ,
          "Profession" : "Airbender"}
json_file = "C:/Users/ASUS/OneDrive/Desktop/json_file.json"

spread_sheet = [["Name   "," Age ","Element  "],          # 2-D Data structure like spread-sheets are used by csv
                ["Aang   ",112,"  Airbender"],
                ["Katara " ,  13 , "   Waterbender"],
                ["Toph   " ,  12  ,"   Earthbender"],
                ["Suko   ",   14   ,"   Non-bender"]]
                
csv_file = "C:/Users/ASUS/OneDrive/Desktop/csv_file.csv"

try:

    with open(file = text_file,mode = 'w') as file:
        for Name in Names:
            file.write(Name + " ")
        print(f"Text file '{text_file}' created")

    with open(json_file, "w")as file:
        json.dump(Avatar, file , indent = 4)
     #  json.dump(Avatar["Name"], file , indent = 4)
        print(f"Json file '{json_file}' created")

    with open(csv_file , "w", newline = "") as file:
        writer = csv.writer(file) 
        for row in spread_sheet:
            writer.writerow(row)
        print(f"CSV file '{csv_file}' created")

except FileExistsError:
    print("File already exists")

