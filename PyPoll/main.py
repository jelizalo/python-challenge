import os
import csv

#CSVpath to first
csvpath1 = os.path.join('election_data_1.csv')
with open (csvpath1, 'r', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader)

	#defining the variables
	votes = 0
	candidates = []
	for row in csvreader:
		#finding total number of votes
		#votes = votes + 1
 
    	if row[2] not in candidates:
           candidates = row[2]
           candidates.append(row[2]):
    print(candidates)

	#print("Election Results")
	#print("---------------------------")
	#print("Total Votes: " + str(votes))
	#print("---------------------------")
	#print()

   	#candidates = []
    #election_data_1 = list(election_data_1)
    #print(len(election_data_1))
   	#for row in election_data_1: 
    	#if row[2] not in candidates:
           #candidates.append(row[2])
    #print(candidates)
# Create a dictionary of the candiate with the number of vote
    #candidate = {}
    #number_of_election = 0
    #for row in election_data_1: 
        #if row[2] not in candidate.keys():
            #number_of_election = 0
            #candidate.update({row[2]: number_of_election})
        #if row[2] in candidate.keys(): 
           # candidate[row[2]] += 1
    #print(candidate)