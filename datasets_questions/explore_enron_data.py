#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print enron_data["LAY KENNETH L"]


total_pois = 0
missing_payments = 0
for person in enron_data.keys():
	if enron_data[person]["poi"] == True:
		total_pois += 1
		if enron_data[person]["total_payments"] == "NaN":
			missing_payments += 1
print missing_payments

# salary_count = 0
# email_count = 0
# for person in enron_data.keys():
# 	if enron_data[person]["email_address"] != "NaN":
# 		email_count += 1
# 	if enron_data[person]["salary"] != "NaN":
# 		salary_count += 1
# print email_count, salary_count


# total_pois = 0
# for person in enron_data.keys():
# 	if enron_data[person]["poi"] == True:
# 		total_pois += 1
# print total_pois

# total_pois = 0
# with open('../final_project/poi_names.txt', 'r') as the_file:
# 	for line in the_file:
# 		total_pois +=1 
# 		# if line[1:2] == "y":
# 		# 	total_pois += 1
# print total_pois
