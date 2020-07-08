# import and create file pat
import os
import csv

#path 
csvpath = os.path.join('..','Resources','election_data_copy.csv')

#declaring variables
total_votes = 0
candidates = {}
candidates_per = {}
winner = ""
winner_count = 0

# read file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

for key, value in candidates.items():
    candidates_per[key] = round((value/total_votes)*100,2)

for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

#print analysis result
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_per[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

#path to output folder
output_path = os.path.join("..","Output", "budget_data.txt")
with open(output_path, 'w', newline='') as text_file:
    print("Election Results", file=text_file)
    print("-------------------------------------", file=text_file)
    print("Total Votes: " + str(total_votes), file=text_file)
    print("-------------------------------------", file=text_file)
    for key, value in candidates.items():
        print(key + ": " + str(candidates_per[key]) + "% (" + str(value) + ")", file=text_file)
        print("-------------------------------------", file=text_file)
    print("Winner: " + winner, file=text_file)
    print("-------------------------------------", file=text_file)

    csvfile.close()