import csv

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_month_profit_losses = None
total_change = 0
max_increase = ["", 0]
max_decrease = ["", 0]

# Open and read the CSV file
with open('Resources/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        # Count total months
        total_months += 1

        # Calculate total profit/losses
        current_month_profit_losses = int(row[1])
        total_profit_losses += current_month_profit_losses

        # Calculate change from the previous month if possible
        if previous_month_profit_losses is not None:
            change = current_month_profit_losses - previous_month_profit_losses
            total_change += change

            # Check for max increase/decrease in profit
            if change > max_increase[1]:
                max_increase = [row[0], change]
            if change < max_decrease[1]:
                max_decrease = [row[0], change]

        previous_month_profit_losses = current_month_profit_losses

# Calculate average change
average_change = total_change / (total_months - 1)

# Prepare the analysis report
analysis_report = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]:,.0f})\n"
    f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]:,.0f})\n"
)

# Print the analysis report
print(analysis_report)

# Write the analysis report to a text file
with open('analysis/analysis.txt', 'w') as file:
    file.write(analysis_report)
