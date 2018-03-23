import qualysapi
import sys
import csv
import requests
import xml.etree.ElementTree as ET

# if len(sys.argv) != 2:
        # print 'Usage: python qid_host_list_detection.py #QID. Multiple QIDs are comma separated.'
        # sys.exit(2)

	
# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')

# API v2 call: QID Host List Detection

call = '/api/2.0/fo/asset/host/vm/detection'
parameters= {'action': 'list', 'qids': sys.argv[1], 'show_igs': '1', 'truncation_limit': '0'}

xml_output = qgc.request(call, parameters)

root = ET.fromstring(xml_output)

filename = sys.argv[1]

with open(filename +'.csv', 'wb') as csvfile:
			csv_writer = csv.writer(csvfile)	
			row = ['hostIP', 'DNS', 'OS', 'QID', 'port', 'results', 'status']
			csv_writer.writerow(row)

			for host in root.iter('HOST'):
			#   print child.tag, child.text
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

				port = host.find('DETECTION_LIST').find('DETECTION').find('PORT').text
				QID = host.find('DETECTION_LIST').find('DETECTION').find('QID').text
				status = host.find('DETECTION_LIST').find('DETECTION').find('STATUS').text
				results = host.find('DETECTION_LIST').find('DETECTION').find('RESULTS').text
				
				row = [hostIP, DNS, OS, QID, port, results, status]	
				
				# print hostIP, ",",DNS,",",OS,",",QID,",",port,",",results,",",status

				csv_writer.writerow(row)