import qualysapi
import sys
import csv
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')

agCleanup_file = csv.reader(open('assetgroupcleanupList_20180402.160147.csv', 'r'))

for row in agCleanup_file:
    #defining variables
    name = (row[0])
    agID = (row[1])

    # API v2 call: Delete asset group by ID        
    call = '/api/2.0/fo/asset/group/'
    parameters = {'action': 'delete', 'id': agID, 'echo_request': '0'}
        
    # Call the API and store the result in xml_output.
    xml_output = qgc.request(call, parameters)

    root = ET.fromstring(xml_output)
        
with open('assetgroupDeleted.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                row = ['status']
                writer.writerow(row)

                for ag in root.iter('RESPONSE'):
                    status = ag.find('TEXT').text
                    # agID = ag.find('ITEM_LIST').find('VALUE').text

                    # print agID, status

                    row = [status]

                    writer.writerow(row)




