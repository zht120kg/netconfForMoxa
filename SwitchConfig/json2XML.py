import json
import raisePayload
#import nc_operations

class switch:
    def __init__(self,ipAddr,portNum):
        self.ipAddr=ipAddr
        self.portNum=portNum

class moxaSwitch(switch):
    def __init__(self,ipAddr,portNum):
        super().__init__(ipAddr,portNum)
        self.portInitialPayloadList=[]  #存储端口配置信息的xml列表
        self.createSlotPayloadList=[]   #存储时间草配置循序的xml列表
        self.deleteSlotPayloadList=[]   #存储删除gcl的xml列表

class hirschmannSwitch(switch):
    def __init__(self,ipAddr,portNum):
        super().__init__(ipAddr,portNum)


#获取拓扑json中moxa交换机的ip地址，用于后续与gcl中的ip进行对比
#目前只有moxa能够通过netconf进行配置
def GetSwitchInfo():

    global moxaSwitchList   #用于存放支持NETCONF的交换机实例,目前为moxa
    moxaSwitchList=[]
    with open('./SwitchConfig/topology.json','r',encoding='utf8') as topo:
        topo_dic=json.load(topo)
        
        for item in topo_dic['switches']:
            if ('moxa' in item['alias'])==True:
                switch_moxa=moxaSwitch(item['ipAddr'],item['portNum'])
                moxaSwitchList.append(switch_moxa)
        
        # for item in moxaSwitchList:
        #     print(item.ipAddr,item.portNum)
        #     print(type(item.ipAddr),type(item.portNum))

#根据gcl生成netconf配置的xml
def gcl2XML():
    global moxaSwitchList

    #打开json文件并存储为字典
    with open('./SwitchConfig/gcl-example.json','r',encoding='utf8') as gcl:
        gcl_dic=json.load(gcl)
        #print(gcl_dic)
    
    for switch in moxaSwitchList:
         #将gcl字典中的元素存入列表（该列表中的单个元素为子字典）   
        portInfo_gcls=[]
        for portInfo in gcl_dic[switch.ipAddr]['portInfo']:            
            portInfo_gcls.append(gcl_dic[switch.ipAddr]['portInfo'][portInfo])

        #生成用于netconf配置的xml信息
        for singlePort in portInfo_gcls:
            portID=singlePort['portInfo']['value']          
            controlListLength=singlePort['operControlListLength']
            cycleTime=singlePort['operCycleTime']


            
            #生成NETCONF端口配置xml
            portConfig=raisePayload.portInitialPayload(portID,controlListLength,cycleTime)
            switch.portInitialPayloadList.append(portConfig)
        


            i=0
            for CtlList_item in singlePort['operControlList']:
                gateStateList=CtlList_item['gateStatesValue']['gateStateList']
                #将gateStateList中二进制表示的门控状态变为可用于NETCONF配置的十进制，取值范围0~255
                sum = ""
                for num in gateStateList:
                    sum +=str(num)
                gateStateValue=int(int(sum,2))
                timeIntervalValue=CtlList_item['timeIntervalValue']
                #生成NETCONF时间槽配置xml
                slotConfig=raisePayload.createSlotPayload(portID,i,gateStateValue,timeIntervalValue)
                switch.createSlotPayloadList.append(slotConfig)


# GetSwitchInfo()
# gcl2XML()
# for switch in switchList:
#     #for item in switch.portInitialPayloadList:
#         #print(item)
#     for item in switch.createSlotPayloadList:
#         print(item)



# """
# ---------以下由拓扑信息的json文件生成用于初始化交换机的NETCONF标准的XML----------
# """


#由拓扑获取的信息，生成删除交换机端口gcl的xml
def topo2XML():

    global moxaSwitchList      
    GetSwitchInfo()

    for switch in moxaSwitchList:
        for portID in range(1,1+switch.portNum):
            #getSlotNumPayload=raisePayload.getSlotIndexPayload(portID)
            #reply=nc_operations.getConfig(str(switch.ipAddr),getSlotNumPayload)
            reply="adadadasd"
            SlotNum=reply.count('<index>')
            if SlotNum==0:
                print('There is no slot in Port ',portID,' of switch',switch.ipAddr)
                continue
            else:
                for slotIndex in range((SlotNum-1),-1,-1):
                    deleteSingleSlot=raisePayload.deleteSlotPayload(portID,slotIndex)
                    (switch.deleteSlotPayloadList).append(deleteSingleSlot)
    
