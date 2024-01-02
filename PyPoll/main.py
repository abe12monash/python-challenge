import csv

# Path to the election data file
file_path = 'Resources/election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}
winner = ''
max_votes = 0

# Read the file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Prepare the election results
results = f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    if votes > max_votes:
        max_votes = votes
        winner = candidate

results += "-------------------------\n"
results += f"Winner: {winner}\n"
results += "-------------------------\n"

# Print the results to the terminal
print(results)

# Write the results to a text file
output_file = 'analysis/election_results.txt'
with open(output_file, 'w') as file:
    file.write(results)
