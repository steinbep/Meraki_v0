import csv
import os
from datetime import datetime
import meraki

start = datetime.now()
todays_date = f'{datetime.now():%m-%d-%Y-%H-%M}'
folder_name = f'Win7_Blocked_{todays_date}'
if folder_name not in os.listdir():
    os.mkdir(folder_name)

timespan = '604800'
noSearch = [] #Network Ids that you do not want to search
netdevices = []
client = []
blocked = []
newInventory = []

m = meraki.DashboardAPI()
orgs = m.organizations.getOrganizations()
nets = m.networks.getOrganizationNetworks(orgs[0]['id'])

for row in nets:
    if row['id'] in noSearch:
        continue
    else:
        devices = m.clients.getNetworkClients(row['id'], t0=None, timespan=timespan, perPage='1000', startingAfter=None,
                                              endingBefore=None, all_pages=True)

    for device in devices:
        device.update({'networkName': row['name']})
        device.update({'networkId': row['id']})
        netdevices.append(device)

for t in netdevices:

    if t['os'] == "Windows 7":
        client.append(t)
    elif t['os'] == "Windows 7/Vista":
        client.append(t)
    elif t['os'] == "Windows 8":
        client.append(t)
    else:
        pass

for n in client:
    policyLookup = m.clients.getNetworkClientPolicy(n['networkId'], n['id'])
    if policyLookup['type'] == 'Blocked':
        pass
    elif policyLookup['type'] == 'Group policy':
        pass
    elif policyLookup['type'] == 'Normal':
        n.update({'timestamp': datetime.now()})
        blockDevice = m.clients.updateNetworkClientPolicy(n['networkId'], n['id'], devicePolicy='Blocked')
        blocked.append(n)
    else:
        pass

# Write to file
file_name = f'Blocked {todays_date}.csv'
output_file = open(f'{folder_name}/{file_name}', mode='w', newline='\n')
field_names = blocked[0].keys()
csv_writer = csv.DictWriter(output_file, field_names, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
csv_writer.writeheader()
csv_writer.writerows(blocked)
output_file.close()

