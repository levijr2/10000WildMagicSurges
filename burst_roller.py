import random
import os
import csv


file_path = os.path.realpath(__file__)
CSV_FILE_PATH = os.path.join(os.path.dirname(file_path), "WildMagicSurges.csv")


num=random.randint(2,10001)
print(num)

with open( CSV_FILE_PATH, "r") as csv_file:
    csv_data = csv.DictReader(csv_file)
        
    for line in csv_data:
        if csv_data.line_num==num:
            print(line)

