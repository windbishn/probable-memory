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

call = '/api/2.0/fo/asset/host'
parameters= {'action': 'list', 'ag_ids': '262062'}

# Call the API and store the result in ag_output.
xml_output = qgc.request(call, parameters)

print xml_output

timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")

# with open('scanFetch_'+ timestamp + '.csv', 'ab') as csvfile:
#     writer = csv.writer(csvfile)
#     for row in xml_output:
#         writer.writerow(row)
