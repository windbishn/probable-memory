import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime


# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.qcrc')

# API v2 Host List: list hosts in [biomed] asset group(s)

call = '/api/2.0/fo/scan'
parameters= {'action': 'list', 'launched_after_datetime': '2018-03-27', 'show_ags': '1'}

# Call the API and store the result in ag_output.
xml_output = qgc.request(call, parameters)

# print xml_output

# Reading the data from a string, fromstring() parses XML from a string directly into an Element
root = ET.fromstring(xml_output)

timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")

with open('scanList_'+ timestamp + '.csv', 'ab') as csvfile:
    writer = csv.writer(csvfile)
    row = ['scanTitle', 'REF', 'target', 'duration', 'type']
    writer.writerow(row)
    for scan in root.iter('SCAN'):
        scanRef = scan.find('REF').text
        scanType = scan.find('TYPE').text
        scanTitle = str(scan.find('TITLE').text)
        apsubnetScan = re.search('.*(Block).*', scanTitle)
        scanDuration = scan.find('DURATION').text
        scanTarget = scan.find('TARGET').text
        scanState = scan.find('STATUS').find('STATE').text
        
        if apsubnetScan:

            # print apsubnetScan.group(0),scanRef, scanType, scanDuration, scanState, scanTarget

            row = [apsubnetScan.group(0), scanRef, scanTarget, scanDuration, scanType]
            writer.writerow(row)
