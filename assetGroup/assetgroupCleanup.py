import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')


# API v2 Asset Group: list asset groups
call = '/api/2.0/fo/asset/group/'
parameters={'action': 'list', 'truncation_limit': '0'}

# Call the API and store the result in ag_output.
ag_output = qgc.request(call, parameters)

# Reading the data from a string, fromstring() parses XML from a string directly into an Element
root = ET.fromstring(ag_output)

timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")

with open('assetgroupcleanupList_'+timestamp+'.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		row = ['name', 'ID']
		writer.writerow(row)

		for ag in root.iter('ASSET_GROUP'):
			assetgroupTitle = str(ag.find('TITLE').text)
			assetgroupID = ag.find('ID').text
			# print assetgroupTitle

			# Regex [notinUse] in assetgroupTitle
			notinUse = re.search('^((?!GRP).)*$', assetgroupTitle)    
				
			if notinUse:    
			
				row = [notinUse.group(0), assetgroupID]
				writer.writerow(row)
