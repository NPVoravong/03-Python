import os
import csv

#Location for the CSV file that need to be processed for the analysis

budget_csv = os.path.join ('.', 'Resources','budget_data.csv')

#Load the Budget CSV

with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

#Use the len command to find the total number of months in the CSV

    months = len(list(csv_reader))

#Reload the Budget CSV

with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

#Create a list from the CSV of the Profit/Loss column and months column

    pl_values = []
    budget_months = []
    for row in csv_reader:
        pl_values.append(int(row[1]))
        budget_months.append(row[0])

#Get the Net Total of the Profit/Loss using the Sum function

    total = sum(pl_values)

#Calculate the average change over the entire period using the average change formula

    average_change = (pl_values[0] - pl_values[-1]) *-1 /(int(months) - 1)

#Convert Profit/Loss and Increase/Decrease from Months to Dictionary. Add an extra value to the beginning of the list so it can be converted to a dictionary

    month_to_month = []
    for num in range(len(pl_values)-1): 
        sum = pl_values[num + 1] - pl_values[num] 
        month_to_month.append(sum)
    month_to_month.insert(0,0)

    budget_dict = dict(zip(budget_months,month_to_month)) 
#Calculate the Increase/Decrease for the entrire period
    increase_date = max(budget_dict, key=budget_dict.get)
    increase_num = max(month_to_month)
    decrease_date = min(budget_dict, key=budget_dict.get)
    decrease_num = min(month_to_month)

print("")
print("Financial Analysis")
print('-------------------------------') 
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {increase_date} (${increase_num})')
print(f'Greatest Decrease in Profits: {decrease_date} (${decrease_num})')
print("")