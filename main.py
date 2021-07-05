# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #name variables
    Total_Months=0 
    Total= 0
    Average_Change= 0
    Greatest_Increase=0
    Greatest_Decrease=0

    ProfitLosses = []
    Previous_ProfitLosses = 0
    Month_Of_Change = []
    ProfitLosses_Change = 0
    Greatest_Decrease = ["", 9999999]
    Greatest_Increase = ["", 0]
    ProfitLosses_Change_List = []
    ProfitLosses_Average = 0

    # Count total months 
    #+= 1 for every index [0]
    for row in csvreader: 
        Total_Months+=1 
    
    #Count total Profit/Losses
        Total += int(row[1])
        
    
    #Find average chnage

        ProfitLosses_Change = float(row[1])- Previous_ProfitLosses
        Previous_ProfitLosses = float(row[1])
        ProfitLosses_Change_List = ProfitLosses_Change_List + [ProfitLosses_Change]
        Month_Of_Change = [Month_Of_Change] + [row[0]]

        

#Find greatest increse in profits + dates
        if ProfitLosses_Change>Greatest_Increase[1]:
            Greatest_Increase[1] = ProfitLosses_Change
            Greatest_Increase[0] =row[0]

#Find greatest decrease in profits + dates
    if ProfitLosses_Change<Greatest_Decrease[1]:
            Greatest_Decrease[1]= ProfitLosses_Change
            Greatest_Decrease[0] = row[0]
            ProfitLosses_average = sum(ProfitLosses_Change_List)/len(ProfitLosses_Change_List)


        
#Print 
print("Financial Analysis")
print("----------------------------")
print("Total Months:" + str(Total_Months))
print("Total: $" + str(Total))
print("Average Change:" + str(Average_Change))
print("Greatest Increase in Profits:" + str(Greatest_Increase))
print("Greatest Decrease in Profits" + str(Greatest_Decrease))


#to print strings on new lines in text
#tried
#Total_Month_String=("Total Months:" + str(Total_Months))
#^ didnt work




#Export a text file
with open("TextPath/output.txt", 'w') as file: 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months:" + str(Total_Months))
    file.write("Total: $" + str(Total))
    file.write("Average Change:\n" + str(Average_Change))
    file.write("Greatest Increase in Profits:" + str(Greatest_Increase))
    file.write("Greatest Decrease in Profits" + str(Greatest_Decrease))