#test sync    
#apple
import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime

subnet_file = csv.reader(open('ahs_subnets_asc.csv', 'rb'))
ips=[]

for row in subnet_file:
	
	#defining variable to be used in Qualys API call
	subnetRange = (row[0])
	# print subnetRange

	# Setup connection to QualysGuard API.
	qgc = qualysapi.connect('../../config.qcrc')

	# API v2 Host List: list host alreay scanned. 
	call = '/api/2.0/fo/asset/host/'
	parameters= {'action': 'list', 'ips': subnetRange, 'details': 'Basic'}

	xml_output = qgc.request(call, parameters)
	
	root = ET.fromstring(xml_output)

	# print xml_output

	timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")

	subnetStatus  = open('subnetStatus.csv', 'a')

	with subnetStatus:
		writer = csv.writer(subnetStatus)
		row = ['subnetRange', 'status']
		writer.writerow(row)

		#A subnet that does not belong to an asset group nor scanned will not have "HOST_LIST" Element
		for host in root.iter('RESPONSE'):
			subnetScanned = host.find('HOST_LIST')
		
			if subnetScanned is None:
				status = "notScanned"
				# print subnetRange, status
			else:
				status = "scanned"
				# print subnetRange, status

		row = [subnetRange, status]
		writer.writerow(row)