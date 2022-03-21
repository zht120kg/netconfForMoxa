import os
from stat import  S_IRWXU
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
        


def CLIConf(hirschmannSwitch):
    ScriptPath='./SwitchConfig/Hirschmann-'+hirschmannSwitch.ipAddr+'-CLI.sh'
    ScriptContent=json2XML.raiseShell(hirschmannSwitch)
    with open(ScriptPath,"w") as Script:
          Script.writelines(ScriptContent)
    os.chmod(ScriptPath,S_IRWXU)  #给脚本添加执行权限
    #data=os.popen(ScriptPath)
    #print(data.read())


json2XML.GetSwitchInfo()
json2XML.gcl2CLI()
CLIConf(json2XML.hirschmannSwitchList[0])
#PortConf(json2XML.moxaSwitchList[0])
#SlotConf(json2XML.moxaSwitchList[0])


def DeleteGCL():
    
    json2XML.topo2XML()

    for switch in json2XML.moxaSwitchList:
        for payload in switch.deleteSlotPayloadList:
            #nc_operations.editConfig(str(switch.ipAddr),payload)
            pass
        

