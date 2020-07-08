# Import the os module - provides support for filepaths and other OS functions
import os

# Import the CSV modulewhich includes functions for reading CSV files
import csv

# Establish a path variable for the specific path for the location of the budget file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the CSV file on the path in csvpath
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Initialize variables to compute values while looping through the rows in the file
    rowcount = 0
    nettotalprofitandloss = float(0)
    greatestprofitincrease = float(0)
    greatestprofitdecrease = float(0)
    totalmonthlychange = float(0)
    # To be able to compare the values of the prior and current row need to be able to reference the prior row. 
    # pre_row = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        rowcount = rowcount + 1
        if rowcount == 1:
            pre_row = row
            
        # Maintain a runnint total of the profit & loss column values to 
        # calculate the nettotal of profit and loss
        nettotalprofitandloss = nettotalprofitandloss + float(row[1])

        # Comparing profit and loss values across prior and current rows.
        # Needed to compare floats in order to compare larger values correctly

        # To find greatest increase in profits, compare each month to the next and if the 
        # difference is greater than the currnt greatest value save it to a variable.
        # The converse applies to find the greates loss in profits between any pair of months.
        if float(pre_row[1]) < float(row[1]): # <--indicates a profit has occured from the previous month to the current month
            #print(f"previous row is less in: {row[0]},{pre_row[1]} < {row[1]}")
            if float(row[1]) - float(pre_row[1]) > float(greatestprofitincrease):
                greatestprofitincrease = float(row[1]) - float(pre_row[1])
                greatestprofitincreasemonth = row[0]
        else:  # <--a loss has occured from the previous month to the current month
            #print(f"previous row is greater in: {row[0]},{pre_row[1]} > {row[1]}")
            if float(row[1]) - float(pre_row[1]) < float(greatestprofitdecrease):
                greatestprofitdecrease = float(row[1]) - float(pre_row[1])
                greatestprofitdecreasemonth = row[0]

        # Calculate running total of change from month to month
        if float(pre_row[1]) != float(row[1]):
            totalmonthlychange = totalmonthlychange + float(row[1]) - float(pre_row[1])

        pre_row = row
        

#Setup a single list to contain the output for the SCREEN and FILE 
csvoutputlist = ["----------------------------------",
                "Financial Analysis",
                "-----------------------------------",
                f"Total Months: {rowcount}", 
                f"Total: {'${:,.2f}'.format(nettotalprofitandloss)}", 
                f"Average Change: {'${:,.2f}'.format(totalmonthlychange/(rowcount-1))}",
                f"Greatest Increase in Profits: {greatestprofitincreasemonth} ({'${:,.2f}'.format(greatestprofitincrease)})",
                f"Greatest Decrease in Profits: {greatestprofitdecreasemonth} ({'${:,.2f}'.format(greatestprofitdecrease)})"
                ]

# Specify the file to write to
outputpath = os.path.join("Analysis", "PyBank_results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputpath, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Loop through the csvoutputlist and write to the FILE and the screen simultaneously.
    for item in csvoutputlist:
        csvfile.write(str(item)+ "\n")
        print(str(item))

    


