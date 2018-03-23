import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')


# API v2 Asset Group: list asset groups
call = '/api/2.0/fo/asset/group/'
parameters={'action': 'list', 'truncation_limit': '0'}

ag_output = qgc.request(call, parameters)
root = ET.fromstring(ag_output)

for ag in root.iter('ASSET_GROUP'):
	assetgroupTitle = str(ag.find('TITLE').text)
	# print assetgroupTitle

	# Regex [biomed] in assetgroupTitle
	biomed = re.search('.*[bB][iI][oO][mM][eE][dD].*', assetgroupTitle)    
        
	if biomed:    
    
		# print biomed.group(0)

# API v2 Host List: list hosts in [biomed] asset group(s) 
		call = '/api/2.0/fo/asset/host/'
		parameters= {'action': 'list', 'ag_titles': biomed.group(0), 'details': 'All/AGs'}

		xml_output = qgc.request(call, parameters)
		
		root = ET.fromstring(xml_output)
	    		
		# print xml_output
				
		# print root.tag
		# print root[0].text
		# print root.attrib

		# Open file for writing
		with open('test.csv', 'ab') as csvfile:
				writer = csv.writer(csvfile)
				row = ['IP', 'DNS', 'assetgroupID']
				writer.writerow(row)
				for host in root.iter('HOST'):
				
					hostIP = host.find('IP').text
					assetgroupID = host.find('ASSET_GROUP_IDS').text
					# hostDNS = host.find('DNS')
					findDNS = host.find('DNS')
					
					if findDNS is None:
						DNS = "noDNS"
					else:
						DNS = host.find('DNS').text
						
					row = [hostIP, DNS, assetgroupID]
					
					writer.writerow(row)		