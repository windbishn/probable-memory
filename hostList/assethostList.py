import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime


with open('ahs_subnets.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		#defining variable to be used in Qualys API call
		subnetRange = (row[0])

		# Setup connection to QualysGuard API.
		qgc = qualysapi.connect('../../config.qcrc')

		# API v2 Host List: list host alreay scanned. 
		call = '/api/2.0/fo/asset/host/'
		parameters= {'action': 'list', 'ips': subnetRange, 'details': 'Basic'}

		xml_output = qgc.request(call, parameters)
	
		root = ET.fromstring(xml_output)

		timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")

		with open ('subnet_Status.csv', 'a') as csvfile:
				writer = csv.writer(csvfile)
				row = ['subnetRange', 'status']
				writer.writerow(row)

			#Check if subnet has been scanned.
				for host in root.iter('RESPONSE'):
					subnetScanned = host.find('HOST_LIST')
		
					if subnetScanned is None:
						status = "notScanned"
					# print subnetRange, status
					else:
						status = "scanned"
					# print subnetRange, status

					row = [subnetRange, status ]
					writer.writerow(row)