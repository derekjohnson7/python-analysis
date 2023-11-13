import os 
import csv

budgetpath = os.path.join("budget_data.csv")

total = 0

with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=",")


for row in budgetreader:
    print("Total Months:" + len(row[0]))

for row in budgetreader:
    total = total + int(row[1])
    print("Total:" + int(total))
    print("Average Change:" + int(total//row[1]))

