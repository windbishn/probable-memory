import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.qcrc')

ip_file = csv.reader(open('APsubnets.csv', 'r')) 
 
for row in ip_file:
    ips_param = ','.join(map(str,row))        

    # API v2 Host List: 
    call = '/api/2.0/fo/asset/host/'
    parameters= {'action': 'list', 'ips': ips_param, 'details': 'Basic/AGs'}

    xml_output = qgc.request(call, parameters)
          
    root = ET.fromstring(xml_output)

    timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")
                       
    # print xml_output

    # Open file for writing
with open('APassetgrouphostList_'+ timestamp + '.csv', 'wb') as csvfile:
                    writer = csv.writer(csvfile)
                    row = ['IP', 'OS', 'DNS', 'assetgroupID', 'assetgroupTitle']
                    writer.writerow(row)
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
                                        
                                assetgroupID = host.find('ASSET_GROUP_IDS').text
                                # assetgroupTitle = host.find('ASSET_GROUP_LIST').find('ASSET_GROUP').find('TITLE').text
                                            
                                row = [hostIP, DNS, OS, assetgroupID]
                                        
                                writer.writerow(row)
                                    
                

        