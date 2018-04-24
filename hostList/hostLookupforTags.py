import qualysapi
import sys
import csv
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')

    # API v2 Host List: 
call = '/api/2.0/fo/asset/host/'
parameters= {'action': 'list', 'ag_ids': '243923', 'details': 'Basic/AGs','show_tags': '1' }

xml_output = qgc.request(call, parameters)
          
root = ET.fromstring(xml_output)

print xml_output

timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")