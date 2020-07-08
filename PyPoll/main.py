#Import the os module - provides support for filepaths and other OS functions
import os

# Import the CSV modulewhich includes functions for reading CSV files
import csv

# Establish a path variable for the specific path for the location of the budget file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the CSV file on the path in csvpath
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Initialize variables to compute values while looping through the rows in the file
    rowcount = 0
    unique_candidate_list = []
    unique_candidate_votecount = []
    c_index = int(0)
    max_votes = 0
    votes_index = 0
    max_votes_index = 0

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        rowcount = rowcount + 1
        # Find unique list of candidates and add them to a list of unique candidates
        if row[2] not in unique_candidate_list:
            unique_candidate_list.append(row[2]) 
            unique_candidate_votecount.append(0)
        # Get the corresponding index for the specific candidate, to be used to maintain
        # the total votes in the corresponding list of vote counts
        c_index = unique_candidate_list.index(row[2])
        unique_candidate_votecount[c_index] = int(unique_candidate_votecount[c_index]) + 1

# Find the index of the vote count winner, and use it to identify the winning candiate
for votes in unique_candidate_votecount:
    if max_votes < votes:
        max_votes = votes
        max_votes_index = votes_index
    votes_index = votes_index + 1


print("==================================")
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {rowcount}")
print("----------------------------------")

# Loop through the csvoutputlist and write to the FILE and the screen simultaneously.
#for item in csvoutputlist:
    #csvfile.write(str(item)+ "\n")
    #print(str(item))   
for name in unique_candidate_list:
    c_index = unique_candidate_list.index(name)
    print(str(name)+ ":" + 
        "  " + str('{:,.3f}%'.format(unique_candidate_votecount[int(c_index)]/rowcount * 100)) + 
        "  " + "(" + str(unique_candidate_votecount[int(c_index)]) + ")"
        )
print("----------------------------------")
print("Winner: "+ str(unique_candidate_list[max_votes_index]))
print("==================================")
