import qualysapi
import csv
import logging
import sys
import xml.etree.ElementTree as ET

#Read facility IP information from SolarWinds export

with open('acc_out.csv', 'r') as file:
	reader = csv.reader(file)
	next(reader)
	for row in reader:
		#defining variables
		displayname = (row[0])
		subnetaddressCIDR = (row[1])
		
		# Set the MAXIMUM level of log messages displayed @ runtime. 
		logging.basicConfig(level=logging.INFO,
							format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
							datefmt='%m-%d %H:%M',
							filename='myQualysAGimport.log',
							filemode='w')
		
		# Setup connection to QualysGuard API.
		qgc = qualysapi.connect('config.ini')
		
		# Logging must be set after instanciation of connector class.
		logger = logging.getLogger('qualysapi.connector')
		logger.setLevel(logging.DEBUG)

		# Log to sys.out.
		logger_console = logging.StreamHandler()
		logger_console.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
		logging.getLogger(__name__).addHandler(logger)

		# API v2 call: Add a new asset group
		call = '/api/2.0/fo/asset/group/'
		parameters = {'action': 'add', 'title': displayname, 'ips': subnetaddressCIDR, 'business impact': 'High', 'appliance_ids': '394123'}
		
		# Call the API and store the result in xml_output.
		xml_output = qgc.request(call, parameters)	
		
		# Reading the data from a string, fromstring() parses XML from a string directly into an Element
		root = ET.fromstring(xml_output)
		
		print xml_output		