
import json2XML
import nc_operations



def PortConf():
    host='192.168.0.253'
    for payload in json2XML.portInitialPayloadList:
        print(payload)
        nc_operations.editConfig(host,payload)
        


def SlotConf():
    host='192.168.0.253'
    for payload in json2XML.createSlotPayloadList:
        print(payload)
        nc_operations.editConfig(host,payload)
        

json2XML.gcl2XML()
#PortConf()
#SlotConf()


def DeleteGCL():
    
    json2XML.topo2XML()

    for switch in json2XML.switchList:
        for payload in switch.deleteSlotPayloadList:
            nc_operations.editConfig(str(switch.ipAddr),payload)
        

