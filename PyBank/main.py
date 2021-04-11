import os  # create paths to operating systems
import csv  # module for reading CSV files

csvpath = os.path.join("../Resources/budget_data.csv")  # path to grab CSV data

total_months = [] # set Total Months as list
net_profit = [] # set Net Profit as list
profit_change = [] # set Profit Change as list

with open('budget_data.csv') as csvfile: # open CSV file
    csvreader = csv.reader(csvfile, delimiter=',')  # CSV reader specifies delimiter and variable that holds contents

    next(csvreader)  # skip header row

    for row in csvreader: # read through each row of the data
        total_months.append(row[0]) # add the Total Months in Column 1, which is row 0
        net_profit.append(int(row[1])) # add the Net Profit in Column 2, which is row 1, set as an integer

    for i in range(len(net_profit)-1): # read through any variable in the list, set to -1
        profit_change.append(net_profit[i+1]-net_profit[i]) # make a new list where (second month[i+1] - first month[i])

increase = max(profit_change) #find max of Profit Change, set to "increase"
decrease = min(profit_change) # find mix of Profit Change, set to "decrease"

monthly_increase = profit_change.index(max(profit_change))+1 # find Monthly Increase of max Profit Change, set to +1 to go to next month
monthly_decrease = profit_change.index(min(profit_change))+1 # find Monthly Decrease of min Profit Change, set to +1 to go to next month

# print statements with associated math, make f statements so there's less code for explanation
print("Financial Analysis") 
print("-----------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_profit)}")
print(f"Average Change: ${round(sum(profit_change) / len(profit_change), 2)}")
print(f"Greatest Increase In Profits: {total_months[monthly_increase]} (${(str(increase))})") 
print(f"Greatest Decrease In Profits: {total_months[monthly_decrease]} (${(str(decrease))})")

# creat output txt file to be loaded into Analysis folder
budget_output = open("../Analysis/budget_output.txt", "w")

# write each line of the statements above, use \n to create a new indent line
budget_output.write("Financial Analysis")
budget_output.write("\n-----------------------")
budget_output.write(f"\nTotal Months: {len(total_months)}")
budget_output.write(f"\nTotal: ${sum(net_profit)}")
budget_output.write(f"\nAverage Change: ${round(sum(profit_change) / len(profit_change), 2)}")
budget_output.write(f"\nGreatest Increase In Profits: {total_months[monthly_increase]} (${str(increase)})")
budget_output.write(f"\nGreatest Decrease In Profits: {total_months[monthly_decrease]} (${str(decrease)})")
