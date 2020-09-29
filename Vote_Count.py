import os
import csv

#Location for the CSV files that need to be processed for the analysis

election_csv = os.path.join ('.', 'Resources','election_data.csv')

#Open the election csv so data can be read from it
with open(election_csv, 'r') as elec_csv_file:
    elec_csv_reader = csv.reader(elec_csv_file, delimiter=',')

#Skip the header row in the CSV and use the Len function to define the total number of votes

    elec_csv_header = next(elec_csv_reader)
    
    votes = len(list(elec_csv_reader))

#Reload the Election CSV 

with open(election_csv, 'r') as elec_csv_file:
    elec_csv_reader = csv.reader(elec_csv_file, delimiter=',')

    elec_csv_header = next(elec_csv_reader)

#Append all of the votes as names to a list to be processed later.

    all_votes = []
    for row in elec_csv_reader:
        all_votes.append(row[2])

#Count all of votes of the specified string from the group all_votes

    khan_vote = all_votes.count("Khan")
    correy_vote = all_votes.count("Correy")
    li_vote = all_votes.count("Li")
    otooley_vote = all_votes.count("O'Tooley")

#Find the percent of votes each candidate received

    khan_per = (khan_vote/votes) * 100
    correy_per = (correy_vote/votes) * 100
    li_per = (li_vote/votes) * 100
    otooley_per = (otooley_vote/votes) * 100

#Using a dictionary find the candidate that had the most votes

    candidate_dict = {"Khan" : int(khan_vote), "Correy" : int(correy_vote), "Li" : int(li_vote), "O'Tooley" : int(otooley_vote)}
    winner = max(candidate_dict, key=candidate_dict.get)

#Print the results of the voting data that has been proccessed

print("")
print("Election Results")
print('-------------------------------')   
print(f"Total Votes: {votes}")
print('-------------------------------') 
print(f"Khan: {round(khan_per,2)}% ({khan_vote})")
print(f"Correy: {round(correy_per,2)}% ({correy_vote})")
print(f"Li: {round(li_per,2)}% ({li_vote})")
print(f"O'Tooley: {round(otooley_per,2)}% ({otooley_vote})")
print('-------------------------------')
print(f"Winner: {winner}")
print("")