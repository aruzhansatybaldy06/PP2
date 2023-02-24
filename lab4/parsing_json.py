import json

with open('sample-data.json') as file:
    json_data = json.load(file)

a=''' 
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''
print(a)

iamdata=json_data["imdata"]

for item in iamdata:
    
    print("{DN:50}{Speed:>30}{MTU:>6}".format(DN=item['l1PhysIf']['attributes']['dn'],Speed=item['l1PhysIf']['attributes']['speed'],MTU=item['l1PhysIf']['attributes']['mtu']))
   