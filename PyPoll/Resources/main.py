import os # import operating system
import csv # import CSV module

csvpath = os.path.join("../Resources/election_data.csv") # path to grab CSV data

# set Total Votes as an integer
total_votes = 0 

candidates = [] # set Candidates as a list
number_votes = [] # set Number of Votes as a list
percent_votes = [] # set Percent of Votes as a list
votes_per_candidate = []

with open(csvpath) as csvfile: # open CSV file
    csvreader = csv.reader(csvfile, delimiter=',') # CSV reader specifies delimiter and variables
    next(csvreader) # skip header row

    for row in csvreader: # read through each row of the data
        total_votes += 1 # add up the voter counts

        if row[2] not in candidates: # check to see if voter is in list. if not, assign vote and count
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1

for votes in number_votes: # add to the percent_vote list
    percentage = (votes / total_votes) * 100
    percentage = round(percentage) # round the percentage
    percentage = "%.3f%%" % percentage # format for % to 3 decimal points
    percent_votes.append(percentage) # create 'Percent of Votes' list

    # find the winning candidate
    winner = max(number_votes) # winner is the max number of votes
    index = number_votes.index(winner) # return the index of the Number of Votes in the list
    winning_candidate = candidates[index]

# print the results
print("Election Results")
print("------------------")
print(f"Total Votes: {str(total_votes)}") # Total Votes is an integer, set as string
print("------------------")
for count in range(len(candidates)): # check count range for candidates, percent of votes, and number of votes
    print(f"{candidates[count]}: {str(percent_votes[count])} ({str(number_votes[count])})")
print("------------------")
print(f"Winner: {winning_candidate}") 
print("------------------")

# create output txt file to be loaded into Analysis folder
election_output = open("../Analysis/election_output.txt", "w")

# write each line of the statements above, use \n to create a new indent line
election_output.write("Election Results")
election_output.write("\n------------------")
election_output.write(f"\nTotal Votes: {str(total_votes)}") # Total Votes is an integer, set as string
election_output.write("\n------------------")
for count in range(len(candidates)): # check count range for candidates, percent of votes, and number of votes
    election_output.write(f"\n{candidates[count]}: {str(percent_votes[count])} ({str(number_votes[count])})")
election_output.write("\n------------------")
election_output.write(f"\nWinner: {winning_candidate}") 
election_output.write("\n------------------")
