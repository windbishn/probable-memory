import qualysapi
import sys
import csv
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Setup connection to QualysGuard API.
qgc = qualysapi.connect('../../config.qcrc')

call = 'api/2.0/fo/asset/excluded_ip/'
parameters = {'action': 'list'}

# Call the API and store the result in xml_output.
xml_output = qgc.request(call, parameters)

# Reading the data from a string, fromstring() parses XML from a string directly into an Element
root = ET.fromstring(xml_output)

print xml_output