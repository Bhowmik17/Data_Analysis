import os
import csv

budget_data = os.path.join("..", "Practice", "budget_data.csv")


total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]

with open(budget_data) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
        revenue_change = int(row["Revenue"]) - int(prev_revenue)
        revenue_change_list = revenue_change_list + [revenue_change]

        # prepare prev_revenue for next iteration
        prev_revenue = row["Revenue"]

        # calculate greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

         # calculate greatest decrease
        if (revenue_change < greatest_increase[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
output = (
    f"Total Months: {total_months}\n"
    f"Total: {total_revenue}\n"
    f"Average Change: {revenue_change}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n"
)

print(output)

with open(budget_data, "w") as txt_file:
    txt_file.write(output)  

         



    


