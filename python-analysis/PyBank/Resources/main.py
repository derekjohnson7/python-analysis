import os 
import csv

budgetpath = os.path.join("budget_data.csv")

#create empty lists
months = []
profits = []
changes = []


#open and read the csv file
with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(budgetreader)
    prev_month = 0

#use list comprehension to get our profit and months
    for row in budgetreader:
        months.append(row[0])
        profits.append(int(row[1]))


#use list comprehension tp get the change in profits
for count in range(1, len(profits)):
    changes.append(int(profits[count] - profits[count - 1]))

 #calculate the average change   
average_change = sum(changes) / len(changes)

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: $ {sum(profits)}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase: {months[changes.index(max(changes))+1]} (${max(changes)})')
print(f'Greatest Decrease: {months[changes.index(min(changes))+1]} (${min(changes)})')

#create output path for .txt file
output_path = os.path.join("analysis","analysis.txt")

#open and write the file
with open(output_path, 'w') as txtfile:

    writer = csv.writer(txtfile)

    txtfile.write("Financial Analysis")
    txtfile.write('\n''-------------------------')
    txtfile.write(f'\nTotal Months: {len(months)}')
    txtfile.write(f'\nTotal: $ {sum(profits)}')
    txtfile.write(f'\nAverage Change: {round(average_change,2)}')
    txtfile.write(f'\nGreatest Increase: {months[changes.index(max(changes))]} (${max(changes)})')
    txtfile.write(f'\nGreatest Decrease: {months[changes.index(min(changes))]} (${min(changes)})')
    