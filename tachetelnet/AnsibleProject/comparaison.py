#!/usr/bin/python

import json
import sys

def compare(data):

	data['Status'] = ''
	for i in data['Destination']:
        	result = i['details']
        	ch1 = ' uConnection closed by foreign host.'
        	i['details'] = ''

        	if result != ch1:
            		i['Status'] = "Not Ok"
            		i['details'] = result
	    		data['Status'] = "Not Ok"
        	else:
            		i['Status'] = "Ok"
            		i['details'] = "Successfully Connected" 
			

	if data['Status'] == '':
		data['Status'] = "Ok"

	return data


with open(sys.argv[1], 'r') as f:
    file_data = json.load(f)

data = compare(file_data)

with open(sys.argv[1], 'w') as f:
    json.dump(data, f)

