# Election:  version 1
# Run with:  python3 election_v1.py

# Data file row[0] = voter ID
# Data file row[1] = county
# Data file row[2] = candidate

import csv

ELECTION_FILE="election_data.csv"

vote_count = 0          # total vote count
tally = {}              # empty dictionary to tally votes

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


print("\n")
print("total votes: ", vote_count)
for person in tally:
    print('Candidate {}  votes: {}'.format(person, tally[person]))
print("\n")

