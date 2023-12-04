# Import Dependencies
import csv
import os

# Define the path file
csv_path = "PyBank/Resources/budget_data.csv"

# Assign Variables and Values
total_months = 0
total_net = 0
#Create List of Changes
changes = []
#Set a Lower Limit
max_change = -9999999999
max_month = ""
#Set an Upper Limit
min_change = 9999999999
min_month = ""

# Read in the CSV file
with open(csv_path) as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Assign the Header row
    header = next(csvreader)

    for row in csvreader:
        # Figure out the amount of months and the net profits
        total_months += 1
        total_net += int(row["Profit/Losses"])

        # Calculate changes in profit/loss *might need work*
        current_value = int(row["Profit/Losses"])
        if total_months == 1:
            last_value = current_value
        else:
            change = current_value - last_value
            changes.append(change)
            last_value = current_value

            # Find greatest increase and decrease
            if change > max_change:
                max_change = change
                max_month = row["Date"]
            if change < min_change:
                min_change = change
                min_month = row["Date"]

# Calculate average change *needs work, might be prior error*
average_change = sum(changes) / len(changes)

# Print the analysis to terminal
output = f'''Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})
'''

print(output)

# Print output as text file
output_path = os.path.join("Pybank/Analysis", "Analysis.txt")
with open(output_path, 'w') as textfile:
    textfile.write(output)

print(f"Analysis results saved to {output_path}")