# Budget:    version 1
# Run with:  python3 budget_v1.py

import csv

BUDGET_FILE="budget_data.csv"

month_count = 0          # number of months read
total_pl = 0             # total profit less all losses
max_profit =  0          # largest profit increase seen
max_profit_month = ""    # month string with maximum profit increase
max_loss = 0             # largest loss seen
max_loss_month = ""      # month string with maximum loss
last_pl = 0              # last month profit/loss value
current_pl = 0           # current month profit/loss value
current_month = ""       # current month name

with open(BUDGET_FILE, "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)

    # Make sure first word of header is "Date"
    if (header[0] != "Date"):
        print("ERROR: Unexpected data file format.")
        exit(1)

    # Read each line of file and perform calculations
    for row in reader:
        month_count += 1            # count months
        current_month = row[0]      # this month name
        current_pl = int(row[1])    # this month profit/loss value

# Debugging
#        print("month_count: ", month_count)
#        print("current_month: ", current_month)
#        print("current_pl: ", current_pl)

        # Check for an increase in profit.
        # Assume that we must have had a profit - the profit/loss value must be positive.
        # If we increased profit over last month save the value if largest seen so far.

        if (current_pl > 0):    # had a profit, see if biggest so far
            if (current_pl > last_pl):  # made more than last month
                size = current_pl - last_pl     # how much did we grow over last month
                if (size > max_profit):
                    max_profit = size
                    max_profit_month = current_month

        # Check for greatest decrease in profit (decrease between two months).
        # Test is that profit/loss value is less than last month.
        # Record value if largest loss seen so far.

        if (current_pl < last_pl):          # had a loss from last month
            size = current_pl - last_pl     # how much of a loss since last month
            if (size < max_loss):
                max_loss = size             # record the loss
                max_loss_month = current_month 

        # Total all profits and subtract all losses to determine total revenue
        total_pl += current_pl
        
        # Update last month value for use in next loop
        last_pl = current_pl

# Done - print results.

print("Total Months: ", month_count)
print("Total profit/loss: ", total_pl)
print("Max increase in profit: ", max_profit)
print("Max increase in profit month: ", max_profit_month)
print("Max decrease in profit: ", max_loss)
print("Max decrease in profit month: ", max_loss_month)


