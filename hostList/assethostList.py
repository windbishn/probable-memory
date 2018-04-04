import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.qcrc')


# API v2 Host List: list hosts in [] asset group(s), comma separated. 
call = '/api/2.0/fo/asset/host/'
parameters= {'action': 'list', 'ag_ids': '217806', 'details': 'Basic'}

xml_output = qgc.request(call, parameters)
	
root = ET.fromstring(xml_output)

timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")
	    		
		# print xml_output
				
		# print root.tag
		# print root[0].text
		# print root.attrib

# Open file for writing
with open('assetgrouphostList_'+ timestamp + '.csv', 'ab') as csvfile:
				writer = csv.writer(csvfile)
				row = ['IP', 'DNS']
				writer.writerow(row)
				for host in root.iter('HOST'):
				
					hostIP = host.find('IP').text
					findDNS = host.find('DNS')
					
					if findDNS is None:
						DNS = "noDNS"
					else:
						DNS = host.find('DNS').text
						
					row = [hostIP, DNS]
					
					writer.writerow(row)		