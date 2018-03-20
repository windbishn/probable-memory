import qualysapi
import sys
import csv
import requests
import lxml
import re
import xml.etree.ElementTree as ET


from lxml import objectify
# from lxml.builder import E

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')
#

# API v2 call: List all asset groups
call = '/api/2.0/fo/asset/group/'
parameters={'action': 'list', 'truncation_limit': '0'}


agList_output = qgc.request(call, parameters)
assetgroupList = lxml.objectify.fromstring(agList_output)

	
	
	
with open('agList.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		row = ['name', 'ID']
		writer.writerow(row)
		for ag in assetgroupList.RESPONSE.ASSET_GROUP_LIST.ASSET_GROUP:
		
			agName = ag.TITLE;
			agID = ag.ID
			row = [agName, agID]
			
			print agName,",",agID
			writer.writerow(row)
			