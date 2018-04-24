import qualysapi
import sys
import csv
import requests
import xml.etree.ElementTree as ET
from datetime import datetime


# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.ini')
#

# API v2 call: Host List Detection
call = '/api/2.0/fo/asset/host/vm/detection'
parameters= {'action': 'list', 'show_igs': '1', 'ag_ids': '243924', 'truncation_limit': '0'}

# Call the API and store the result in xml_output.
xml_output = qgc.request(call, parameters)

# Reading the data from a string, fromstring() parses XML from a string directly into an Element
root = ET.fromstring(xml_output)

print xml_output
