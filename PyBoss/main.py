import os
import csv

#CSVpath to first
csvpath1 = os.path.join('employee_data1.csv')

with open (csvpath1, 'r', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	row = 0
	emp_id = 0
	name = []
	first_name = []
	last_name = []
	dob = []	
	new_dob = []
	ssn = []
	state = []

	for row in csvreader:
		#print(row)

		# Print Employee ID
		emp_id = row[0];
		#print (emp_id)

		# Splitting first and last name
		row.append(row[1])
		name = row[1];
		#print (name.split())

		# Print Birthdate
		from datetime import date
		row.append(row[2])
		dob = row[2];
		new_dob = datetime.strptime(dob, '%Y-%m-%d').strftime("%m/%d/%Y")
		print(new_dob)


	#next(csvreader)
	#for row in csvreader:
		#print(row)
