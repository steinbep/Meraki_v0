import time
import os
import json
from pprint import pprint as pp
from datetime import datetime
import meraki

companyOneOrgId = 'xxxx'
companyTwoOrgId = 'xxxx'
accesspoints = []
switches = []
serialNum = []

#set date and folder for json output files
todays_date = f'{datetime.now():%m-%d-%Y-%H-%M}'
folder_name = f'$FolderName_{todays_date}'
if folder_name not in os.listdir():
    os.mkdir(folder_name)
	
# I USE AN ENVIRONMENT VARIABLE SO BELOW I DO NOT NEED TO USE MY API KEY.  IF YOU NEED TO USE ONE, PUT IN PARENTHESES BELOW

m = meraki.DashboardAPI()

inventory = m.organizations.getOrganizationInventory(companyOneOrgId)
with open(f'{folder_name}/inventory.json', "w") as outfile:
    json.dump(inventory, outfile)

for line in inventory:
    if 'MR' in line['model']:
        accesspoints.append(line)
		    serialNum.append(line['serial'])
    else:
        switches.append(line)
		    serialNum.append(line['serial'])


# I don't know how to loop through this and increment the number of the file.  
# I was lazy and just wrote out the switches. Copy paste as needed.

Switch1 = m.switch_ports.getDeviceSwitchPorts(Switches[0]['serial'])
with open(f'{folder_name}/Switch1.json', "w") as outfile:
json.dump(Switch1, outfile)

Switch2 = m.switch_ports.getDeviceSwitchPorts(Switches[1]['serial'])
with open(f'{folder_name}/Switch2.json', "w") as outfile:
json.dump(Switch2, outfile)

Switch3 = m.switch_ports.getDeviceSwitchPorts(Switches[2]['serial'])
with open(f'{folder_name}/Switch3.json', "w") as outfile:
json.dump(Switch3, outfile)

# Tests and outputs


# pp(Switch1)
# pp(Switch2)
# pp(Switch3)
# pp(Switch4)
# pp(Switch5)

## I HAVE COMMENTED OUT THE BELOW SO YOU CAN RUN THROUGH THE SCRIPT AND NOT DO DAMAGE.  WHEN READY REMOVE THE THREE ' BELOW. 

'''
# REMOVE ACCESS POINTS :: If not deployed to a site you can comment this out

for line in accesspoints:
    removeAP = m.devices.removeNetworkDevice(companyOneSite, serial=line['serial'])

# REMOVE SWITCHES
for line in switches:
    removeSwitch = m.devices.removeNetworkDevice(companyOneSite, serial=line['serial'])

##########################################################################

# This is where the script waits the 20 minutes to reclaim. 
 
time.sleep(1200)

# CLAIM DEVICES TO NETWORKS

claim = m.devices.claimNetworkDevices(companyTwoSite, serials=serialNum)

time.sleep(120)


# rinse and repeat for the below. 
for switchport in Switch1:
    if switchport['type'] == 'access':
        updateSwitch = m.switch_ports.updateDeviceSwitchPort(switches[0]['serial'], switchport['number'],
                                                             name=switchport['name'],
                                                             enabled=switchport['enabled'],
                                                             type=switchport['type'],
                                                             vlan=switchport['vlan'],
                                                             voiceVlan=switchport['voiceVlan'],
                                                             poeEnabled=switchport['poeEnabled'],
                                                             isolationEnabled=switchport['isolationEnabled'],
                                                             rstpEnabled=switchport['rstpEnabled'],
                                                             stpGuard=switchport['stpGuard'],
                                                             linkNegotiation=switchport['linkNegotiation'],
                                                             portScheduleId=switchport['portScheduleId']
                                                             )
    elif switchport['type'] == 'trunk':
        updateSwitch = m.switch_ports.updateDeviceSwitchPort(switches[0]['serial'], switchport['number'],
                                                             name=switchport['name'],
                                                             allowedVlans=switchport['allowedVlans'],
                                                             tags=switchport['tags'],
                                                             enabled=switchport['enabled'],
                                                             type=switchport['type'],
                                                             vlan=switchport['vlan'],
                                                             voiceVlan=switchport['voiceVlan'],
                                                             poeEnabled=switchport['poeEnabled'],
                                                             isolationEnabled=switchport['isolationEnabled'],
                                                             rstpEnabled=switchport['rstpEnabled'],
                                                             stpGuard=switchport['stpGuard'],
                                                             linkNegotiation=switchport['linkNegotiation'])
    else:
        continue

for switchport in Switch2:
    if switchport['type'] == 'access':
        updateSwitch = m.switch_ports.updateDeviceSwitchPort(switches[1]['serial'], switchport['number'],
                                                             name=switchport['name'],
                                                             enabled=switchport['enabled'],
                                                             type=switchport['type'],
                                                             vlan=switchport['vlan'],
                                                             voiceVlan=switchport['voiceVlan'],
                                                             poeEnabled=switchport['poeEnabled'],
                                                             isolationEnabled=switchport['isolationEnabled'],
                                                             rstpEnabled=switchport['rstpEnabled'],
                                                             stpGuard=switchport['stpGuard'],
                                                             linkNegotiation=switchport['linkNegotiation'],
                                                             portScheduleId=switchport['portScheduleId']
                                                             )
    elif switchport['type'] == 'trunk':
        updateSwitch = m.switch_ports.updateDeviceSwitchPort(switches[1]['serial'], switchport['number'],
                                                             name=switchport['name'],
                                                             allowedVlans=switchport['allowedVlans'],
                                                             tags=switchport['tags'],
                                                             enabled=switchport['enabled'],
                                                             type=switchport['type'],
                                                             vlan=switchport['vlan'],
                                                             voiceVlan=switchport['voiceVlan'],
                                                             poeEnabled=switchport['poeEnabled'],
                                                             isolationEnabled=switchport['isolationEnabled'],
                                                             rstpEnabled=switchport['rstpEnabled'],
                                                             stpGuard=switchport['stpGuard'],
                                                             linkNegotiation=switchport['linkNegotiation'])
    else:
        continue

'''
print('END OF SCRIPT...')
