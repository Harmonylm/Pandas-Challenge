# Election:  version 2
# Run with:  python3 election_v2.py

# Data file row[0] = voter ID
# Data file row[1] = county
# Data file row[2] = candidate

import csv

ELECTION_FILE = "election_data.csv"
OUTPUT_FILE = "Election_Results.txt"

vote_count = 0          # total vote count
tally = {}              # empty dictionary to tally votes
winner = ""             # person that won
max_votes = 0           # winner vote count

with open(ELECTION_FILE, "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)

    # Make sure first word of header is "Voter ID"
    if (header[0] != "Voter ID"):
        print("ERROR: Unexpected data file format.")
        exit(1)

    # Read each line of file. Pick up candidate name.
    for row in reader:
        vote_count += 1             # count votes
        person = row[2]             # candidate name

        # See if person is already in our database.
        # If so just increment the vote count.
        # If not add the person and give a starting count of one.

        if person in tally.keys():
            tally[person] += 1              # increment existing person
        else:
            tally[person] = 1               # new person gets 1 vote

f.close()
# Done counting votes.
# Find the winner by looking at votes and remembering largest count.


for person,count in tally.items():  # look at every dictionary entry
    if (count > max_votes):         # see if this entry has largest vote count yet
        max_votes = count
        winner = person


print("\n")
print('Election Results')
print('-----------------------------')
print('Total Votes: {}'.format(vote_count))
print('-----------------------------')
for person,count in tally.items():      # look at every dictionary entry
    percent = (count / vote_count) * 100.0
    print('{}: {:.3f}% ({})'.format(person, percent, count))
print('-----------------------------')
print('Winner: {}'.format(winner))
print('-----------------------------')

f = open(OUTPUT_FILE, "w")
print('Election Results', file = f)
print('-----------------------------', file = f)
print('Total Votes: {}'.format(vote_count), file = f)
print('-----------------------------', file = f)
for person,count in tally.items():      # look at every dictionary entry
    percent = (count / vote_count) * 100.0
    print('{}: {:.3f}% ({})'.format(person, percent, count), file = f)
print('-----------------------------', file = f)
print('Winner: {}'.format(winner), file = f)
print('-----------------------------', file = f)

