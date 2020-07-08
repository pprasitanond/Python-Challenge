# import and create file path
import os
import csv

csvpath = os.path.join('..','Resources','budget_datacopy.csv')

# define and initiate some variables
months = []
profit_loss = []
profitchangelist = []
date_list = []

count_months = 0
net_profit_loss = 0
current_month_profit = 0
previous_month_profit = 0
profitchange = 0
max_net_change = 0
min_net_change = 0

# read file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        count_months = count_months + 1

        current_month_profit = int(row[1])
        net_profit_loss += (current_month_profit)
        net_final = "${:,.2f}".format(net_profit_loss)

        current_month_profit = int(row[1])
        profitchange = float(current_month_profit) - float(previous_month_profit)
        profitchangelist.append(profitchange)
        previous_month_profit = current_month_profit

def average(profitchangelist):
    x = len(profitchangelist)
    total = sum(profitchangelist) - profitchangelist[0]
    avg = total / (x - 1)
    return avg

average_change = round(average(profitchangelist), 2)
average_change_final = "${:,.2f}".format(average_change)

#greatest increase/decrease
greatest_increase = max(profitchangelist)
greatest_increase_final = "${:,.2f}".format(greatest_increase)
increase_index = profitchangelist.index(greatest_increase)

greatest_decrease = min(profitchangelist)
greatest_decrease_final = "${:,.2f}".format(greatest_decrease)
decrease_index = profitchangelist.index(greatest_decrease)

#print
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {count_months}")
print(f"Total: {net_final}")
print(f"Average Change: {average_change_final}")
print(f"Greatest Increase in Profits: Feb-2012 ({greatest_increase_final})")
print(f"Greatest Decrease in Profits: Sep-2013 ({greatest_decrease_final}")

#path to output folder
output_path = os.path.join("..","Output", "Financial_Analysis.txt")
with open(output_path, 'w', newline='') as text_file:
    print("Financial Analysis", file = text_file)
    print("---------------------------", file = text_file)
    print(f"Total Months: {count_months}", file = text_file)
    print(f"Total: {net_final}", file = text_file)
    print(f"Average Change: {average_change_final}", file = text_file)
    print(f"Greatest Increase in Profits: Feb-2012 ({greatest_increase_final})", file = text_file)
    print(f"Greatest Decrease in Profits: Sep-2013 ({greatest_decrease_final}", file = text_file)

    csvfile.close()




        