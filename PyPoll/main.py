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
		if row[2] not in candidate.keys():
			num_of_elections = 0
			candidates.update({row[2]:num_of_elections})
		if row[2] in candidates.keys():
			candidates[row[2]] +=1
		#store each candidate's election number
			for candidate, vote in elections.items():
		print(candidate + ":" + vote ) 
	#print(candidates)

 

    
   # candidate = {}
    #number_of_election = 0
    #for row in csvreader: 
      #  if row[2] not in candidate.keys():
       #     candidate.update({row[2]: number_of_election})
        #if row[2] in candidate.keys(): 
        #	candidate[row[2]] += 1
    #print(candidate)

#print("Election Results")
#print("---------------------------")
#print("Total Votes: " + str(votes))
#print("---------------------------")
#print(str{candidate})
