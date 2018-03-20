import qualysapi
import sys
import csv
import requests
import lxml
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

with open('filename.csv', 'wb') as csvfile:
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

			for detection in root.iter('DETECTION'):
				QID = detection.find('QID').text
				port = detection.find('PORT').text
				results = detection.find('RESULTS').text
				status = detection.find('STATUS').text
							
				row = [hostIP, DNS, OS, QID, port, results, status]	

				# print hostIP, ",",DNS,",",OS,",",QID,",",port,",",results,",",status

				csv_writer.writerow(row)