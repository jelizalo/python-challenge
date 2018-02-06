import os
import csv

#CSVpath to first
csvpath1 = os.path.join('budget_data_1.csv')
with open (csvpath1, 'r', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader)
	row = 0
	total_rev = 0
	total_months = 0
	average = 0	 
	for row in csvreader:
		print(row)

		# Finding total months
		total_months = total_months + 1
	
		# Finding Revenue Total
		row.append(row[1])
		revenue = row[1]
		total_rev += int(revenue)

		# Finding Average Revenue Change
		average = total_rev/total_months
s
		# Finding Greatest Increase in Revenue

		# Finding Greatest Decrease in Revenue 

	#print our statements	
	print("Total Months : " + str(total_months))		
	print("Total Revenue: " + str(total_rev))
	print("Average Revenue Change: " + str(average))
			
#total_months.append(row[0])
#total_rev.append(row[1])
#avg_rev_change.append(row[1])
#inc_rev.append(row[1])
#dec_rev.append(row[1])



#csvpath2 = os.path.join('budget_data_2.csv')
#with open (csvpath2, 'r', newline='') as csvfile:
	#csvreader = csv.reader(csvfile,delimiter=',')
