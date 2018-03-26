import qualysapi, sys
import xml.etree.ElementTree as ET
# from lxml import objectify, etree

# Connect to QualysGuard.
qgc = qualysapi.connect()

# Capture number of days from command parameter.
number_of_days = sys.argv[1]

# Request assets older than number_of_days.
assets = qgc.request('asset_search.php', {'last_scan': 'not_within:%s' % number_of_days, 'target_asset_groups': 'All'})

root = ET.fromstring(assets)

# Parse assets XML for list of IPs.

ips = ''
for host in root.HOST_LIST.HOST:
    for ip in host.IP:
        ips += ip.text + ','
ips = ips[:-1]

# Purge assets older than number_of_days.
print ips
purge = qgc.request('/api/2.0/fo/asset/host/', {'action': 'purge', 'ips': ips})
print purge