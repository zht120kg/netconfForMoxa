
import json2XML
#import nc_operations



def PortConf(moxaSwitch):
    host=moxaSwitch.ipAddr
    for payload in moxaSwitch.portInitialPayloadList:
        print(payload)
        #nc_operations.editConfig(host,payload)
        


def SlotConf(moxaSwitch):
    host=moxaSwitch.ipAddr
    for payload in moxaSwitch.createSlotPayloadList:
        print(payload)
        #nc_operations.editConfig(host,payload)
        
json2XML.GetSwitchInfo()
json2XML.gcl2XML()
PortConf(json2XML.moxaSwitchList[1])
SlotConf(json2XML.moxaSwitchList[1])


# def DeleteGCL():
    
#     json2XML.topo2XML()

#     for switch in json2XML.moxaSwitchList:
#         for payload in switch.deleteSlotPayloadList:
#             nc_operations.editConfig(str(switch.ipAddr),payload)
        

