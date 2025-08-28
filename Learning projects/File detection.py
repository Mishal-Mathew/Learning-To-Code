
import os

file_path = "wierd.txt"

if os.path.exists(file_path):
    print("That file exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory(folder)")

else:
    print("That file doesn't exist")
