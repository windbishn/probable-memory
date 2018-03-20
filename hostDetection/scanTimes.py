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
    # print host.tag, host.text
    hostIP = host.find('IP').text
    findDNS = host.find('DNS')
    findOS = host.find('OS')
    for detection in root.iter('DETECTION'):
        QID = detection.find('QID').text
        hostResults = str(detection.find('RESULTS').text)
        firstDetected = detection.find('FIRST_FOUND_DATETIME').text
        lastDetected = detection.find('LAST_FOUND_DATETIME').text
        resultArray = hostResults.splitlines( )
        durationTime = resultArray[0]
        # startTime = resultArray[2] 
        # endTime = resultArray[4]

		
        if findOS is None:
				OS = "noOS"
        else:
				OS = host.find('OS').text

        if findDNS is None:
				DNS = "noDNS"
        else:
				DNS = host.find('DNS').text 

                   
    print hostIP
    print DNS
    print firstDetected
    print lastDetected
    print "duration= ",durationTime
    # print "start= ",startTime
    # print "end= ",endTime
	

# for host in root.RESPONSE.HOST_LIST.HOST:
# 	findDNS = host.find('DNS')
# 	hostIP = host.IP; 
# 	hostQID = host.DETECTION_LIST.DETECTION.QID;
# 	hostResults = str(host.DETECTION_LIST.DETECTION.RESULTS)
# 	firstDetected = host.DETECTION_LIST.DETECTION.FIRST_FOUND_DATETIME
# 	lastDetected = host.DETECTION_LIST.DETECTION.LAST_FOUND_DATETIME
# 	resultArray = hostResults.splitlines( )
# 	durationTime = resultArray[0]
# 	startTime = resultArray[2] 
# 	endTime = resultArray[4]

# 	print hostIP
# 	print firstDetected
# 	print lastDetected
# 	print "duration= ",durationTime
# 	print "start= ",startTime
# 	print "end= ",endTime
	
	
	# if findDNS is None:
		# DNS = "noDNS";
	# else:
		# DNS = host.DNS;
	

# Open and write to file. Use last commandline argument for filename

# f_csv = open(sys.argv[-1], 'w') 
# f_csv.write(ret)
# f_csv.close()
	

