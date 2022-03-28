import switchConfFuncs
import json2XML

json2XML.GetSwitchInfo()
json2XML.gcl2CLI()
json2XML.gcl2XML()

#----------配置moxa交换机----------
#初始化交换机并配置gcl
if len(json2XML.moxaSwitchList)!=0:
    switchConfFuncs.DeleteGCL()
    for switch in json2XML.moxaSwitchList:
        switchConfFuncs.PortConf(switch)
        switchConfFuncs.SlotConf(switch)

#---------配置赫斯曼交换机----------
if len(json2XML.hirschmannSwitchList)!=0:
    for switch in json2XML.hirschmannSwitchList:
        switchConfFuncs.CLIConf(switch)
