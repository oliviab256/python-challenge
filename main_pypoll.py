# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

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


    #Name Variables
    Total_Votes=0
    Votes=[]
    Candidates=[]
    Winner=""
    Winner_Count=0



    #Count total votes cast
    #+= 1 for every index [0]
    for row in csvreader: 
       Total_Votes+=1 


    #Candidates list

    Candidates= len([2])




    #% of votes for each candidate

    #Total number of votes for each candidate

    #Winner of election based off votes














#Print 
print("Election Results")
print("----------------------------")
print("Total Votes: "+str(Total_Votes))
print("----------------------------")
print()

print("----------------------------")
print("Winner: ")
print("----------------------------")





#Export a text file
with open("TextPath/output_pypoll.txt", 'w') as file: 
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write("Total Votes:" + str(Total_Votes))
    file.write("----------------------------\n")
    file.write("\n")

    file.write("----------------------------\n")
    file.write("Winner: \n")
    file.write("----------------------------\n")
