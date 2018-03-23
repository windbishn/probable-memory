import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')
#

# API v2 call: List all asset groups
call = '/api/2.0/fo/asset/group/'
parameters={'action': 'list', 'truncation_limit': '0'}

xml_output = qgc.request(call, parameters)

root = ET.fromstring(xml_output)

# agList_output = qgc.request(call, parameters)
# assetgroupList = lxml.objectify.fromstring(agList_output)

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")


with open('agList-'+ timestamp +'.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		row = ['name', 'ID']
		writer.writerow(row)
		for ag in root.iter('ASSET_GROUP'):

			agName = ag.find('TITLE').text
			agID = ag.find('ID').text
			row = [agName, agID]
			
			writer.writerow(row)
			