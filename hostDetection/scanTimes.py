import qualysapi
import sys
import csv
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

if len(sys.argv) !=2:
        print "Usage: python scanTimes.py AssetGroupID. Multiple asset group entries are comma separated."
        sys.exit(2)

	
# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')
#

# API v2 call: Host List Detection
call = '/api/2.0/fo/asset/host/vm/detection'
parameters= {'action': 'list', 'qids': '45038', 'show_igs': '1', 'ag_ids': sys.argv[1], 'truncation_limit': '0'}

# Call the API and store the result in xml_output.
xml_output = qgc.request(call, parameters)

# Reading the data from a string, fromstring() parses XML from a string directly into an Element
root = ET.fromstring(xml_output)

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

filename = sys.argv[1]

with open(filename +'_'+ timestamp + '.csv', 'wb') as csvfile:
            csv_writer = csv.writer(csvfile)	
            row = ['hostIP', 'DNS', 'OS', 'firstDetected', 'lastDetected', 'QID', 'durationTime', 'startTime', 'endTime']
            csv_writer.writerow(row)

            for host in root.iter('HOST'):
                hostIP = host.find('IP').text
                findDNS = host.find('DNS')
                findOS = host.find('OS')
                
                if findOS is None:
                  OS = "noOS"
                else:
                  OS = host.find('OS').text
                  
                if findDNS is None:
                  DNS = "noDNS"
                else:
                  DNS = host.find('DNS').text
              
                firstDetected = host.find('DETECTION_LIST').find('DETECTION').find('FIRST_FOUND_DATETIME').text
                lastDetected = host.find('DETECTION_LIST').find('DETECTION').find('LAST_FOUND_DATETIME').text
                QID = host.find('DETECTION_LIST').find('DETECTION').find('QID').text
                # status = str(host.find('DETECTION_LIST').find('DETECTION').find('STATUS').text
                hostResults = str(host.find('DETECTION_LIST').find('DETECTION').find('RESULTS').text)
                resultArray = hostResults.splitlines()
                durationTime = resultArray[0]
                startTime = resultArray[2]
                endTime = resultArray[4]

                row = [hostIP, DNS, OS, firstDetected, lastDetected, QID, durationTime, startTime, endTime]
                
                csv_writer.writerow(row)
                
    