import csv

data = []

with open("archive_dataset.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)



#Converting all planet names to lower case


#Sorting planet names in alphabetical order




#remove blank lines

