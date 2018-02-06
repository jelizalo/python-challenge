import os
import csv

#CSVpath to first
csvpath1 = os.path.join('election_data_1.csv')
with open (csvpath1, 'r', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader)

	#defining the variables
	votes = 0
	candidates = {}
	for row in csvreader:
		#finding total number of votes
		votes = votes + 1

		#Create a dictionary of the candiate with the number of vote
		if row[2] not in candidates.keys():
			num_of_elections = 0
			candidates.update({row[2]:num_of_elections})
		if row[2] in candidates.keys():
			candidates[row[2]] +=1
		#store each candidate's election number
	
	#defining more variables
	candidate_results = []
	winner = ''
	winner_total = 0

	for name, total in candidates.items():
		percent = (total/votes)*100
		candidate_results.append("{}: {}% ({})".format(name, str(percent), str(total)))
		if total > winner_total:
			winner_total = total
			winner = name

#print on command prompt
print("Election Results")
print("---------------------------")
print("Total Votes: " + str(votes))
print("---------------------------")
for line in candidate_results:
	print(line)
print("---------------------------")
print("Winner: " + winner)


#Output to txt file "Output.txt"
text_file = open("Output.txt", "w")
text_file.write("Election Results")
text_file.write("\n---------------------")
text_file.write("\nTotal Votes: " + str(votes))
text_file.write("\n---------------------------")
for line in candidate_results:
	text_file.write("\n" + line)
text_file.write("\n---------------------------")
text_file.write("\nWinner: " + winner)

text_file.close()

