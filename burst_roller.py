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

'''with open( CSV_FILE_PATH, "r") as csv_file:
    f = csv.DictReader(csv_file)

    filesize = 10000                 #size of the really big file
    offset = random.randrange(filesize)

    f.seek(offset)                  #go to random position
    f.readline()                    # discard - bound to be partial line
    random_line = f.readline()      # bingo!
    # extra to handle last/first line edge cases
    if len(random_line) == 0:       # we have hit the end
        f.seek(0)
        random_line = f.readline()  # so we'll grab the first line instead
        print(random_line)'''
