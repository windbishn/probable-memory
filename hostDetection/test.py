import qualysapi
import sys
import csv
import requests
import lxml
import xml.etree.ElementTree as ET

# from lxml import objectify
# from lxml.builder import E


# if len(sys.argv) !=3:
        # print 'Usage: python vm_hostDetection.py #AssetGroupID AssetGroup_name.csv. Multiple asset group entries are comma separated'.
        # sys.exit(2)

	
# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')
#

# API v2 call: Host List Detection

call = '/api/2.0/fo/asset/host/vm/detection'
parameters= {'action': 'list', 'qids': '45038', 'show_igs': '1', 'ag_ids': sys.argv[1], 'truncation_limit': '0'}

xml_output = qgc.request(call, parameters)

root = ET.fromstring(xml_output)

# print xml_output

# root = lxml.objectify.fromstring(xml_output)

for host in root.iter('HOST'):
		# print child.tag, child.text
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
    status = host.find('DETECTION_LIST').find('DETECTION').find('STATUS').text
    results = str(host.find('DETECTION_LIST').find('DETECTION').find('RESULTS').text)           
print hostIP
print DNS
print firstDetected
print lastDetected
print "duration= ",durationTime
print "start= ",startTime
print "end= ",endTime
	