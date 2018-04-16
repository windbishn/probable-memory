import qualysapi
import sys
import csv
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.qcrc')


# API v2 call: List all asset groups
call = '/api/2.0/fo/asset/group/'
parameters={'action': 'list', 'truncation_limit': '0'}

# Call the API and store the result in xml_output.
xml_output = qgc.request(call, parameters)

# Reading the data from a string, fromstring() parses XML from a string directly into an Element
root = ET.fromstring(xml_output)

timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")


with open('assetgroupList_'+timestamp+'.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		row = ['name', 'ID']
		writer.writerow(row)
		for ag in root.iter('ASSET_GROUP'):

			agName = ag.find('TITLE').text
			agID = ag.find('ID').text
			row = [agName, agID]
			
			writer.writerow(row)
			
