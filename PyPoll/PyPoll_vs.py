import os
import csv

#load file
election_data = os.path.join('..', 'Practice', 'election_data.csv')

total_votes = 0
candidate_options = []
vote_per_candidate = []
percent_vote_per_candidate = []
election_winner = []



with open(election_data) as poll_data:
    reader = csv.DictReader(poll_data)

    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row["Candidate"]
    
        if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)  

        
output = (
    f"Total Votes: {total_votes}\n"
    f"Candidate: {candidate_options}\n"
    
)


print(output)

with open(election_data, "w") as txt_file:
    txt_file.write(output) 


