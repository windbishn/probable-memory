import qualysapi
import csv
import logging
import sys
import xml.etree.ElementTree as ET

#Read facility IP information from SolarWinds export

with open('acd_names.csv', 'rb') as file:
	reader = csv.reader(file)
	next(reader)
	for row in reader:
		#defining variables
		displayname = (row[0])
		# subnetaddressCIDR = (row[1])
		# comments = (row[1])

		print displayname
		
		# # Setup connection to QualysGuard API.
		# qgc = qualysapi.connect('../../config.qcrc')
		
		# # API v2 call: Add a new asset group
		# call = '/api/2.0/fo/asset/group/'
		# parameters = {'action': 'add', 'title': displayname, 'ips': subnetaddressCIDR, 'comments': comments, 'business impact': 'High'}
		
		# # Call the API and store the result in xml_output.
		# xml_output = qgc.request(call, parameters)	
		
		# # Reading the data from a string, fromstring() parses XML from a string directly into an Element
		# root = ET.fromstring(xml_output)
		
		# print xml_output		