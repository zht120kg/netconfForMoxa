import json
import raisePayload
#import nc_operations



def gcl2XML():

    global portInitialPayloadList
    global createSlotPayloadList
    portInitialPayloadList=[]
    createSlotPayloadList=[]

    #打开json文件并存储为字典
    with open('./SwitchConfig/gcl.json','r',encoding='utf8') as gcl:
        gcl_dic=json.load(gcl)


    #将gcl字典中的元素存入列表（该列表中的单个元素为子字典）   
    portInfo_gcls=[]
    for portInfo in gcl_dic: 
        portInfo_gcls.append(gcl_dic[portInfo]) 

    #生成用于netconf配置的xml信息
    for item in portInfo_gcls:
        portID=item['portInfo']['value']
        portEnabled=True
        gateEnabled=True
        controlListLength=item['operControlListLength']
        cycleTime=item['operCycleTime']

        #print(item['portInfo'],end=' ')
        #print(item['operCycleTime'],end=' ') 
        #print(item['operBaseTime'],end=' ')
        #print(item['operControlListLength'],end=' ')
        #print(item['timeIntervalGranularity'])
        
        #生成NETCONF端口配置xml
        portConfig=raisePayload.portInitialPayload(portID,portEnabled,gateEnabled,controlListLength,cycleTime)
        portInitialPayloadList.append(portConfig)
    


        i=0
        for CtlList_item in item['operControlList']:
            gateStateList=CtlList_item['gateStatesValue']['gateStateList']
            #将gateStateList中二进制表示的门控状态变为可用于NETCONF配置的十进制，取值范围0~255
            sum = ""
            for num in gateStateList:
                sum +=str(num)
            gateStateValue=int(int(sum,2))
            timeIntervalValue=CtlList_item['timeIntervalValue']
            #生成NETCONF时间槽配置xml
            slotConfig=raisePayload.createSlotPayload(portID,i,gateStateValue,timeIntervalValue)
            createSlotPayloadList.append(slotConfig)



# """
# ---------以下由拓扑信息的json文件生成用于初始化交换机的NETCONF标准的XML----------
# """

class switch:
    def __init__(self,ipAddr,portNum):
        self.ipAddr=ipAddr
        self.portNum=portNum
        self.deleteSlotPayloadList=[]   #存储删除gcl的xml列表

#switchList=[]       #用于存放支持NETCONF的交换机实例


#获取拓扑json中moxa交换机的ip地址与端口数
def GetSwitchInfo():

    global switchList   #用于存放支持NETCONF的交换机实例
    switchList=[]
    with open('./SwitchConfig/topology.json','r',encoding='utf8') as topo:
        topo_dic=json.load(topo)
        
        for item in topo_dic['switches']:
            if ('moxa' in item['alias'])==True:
                switch_n=switch(item['ipAddr'],item['portNum'])
                switchList.append(switch_n)
        
        for item in switchList:
            print(item.ipAddr,item.portNum)
            print(type(item.ipAddr),type(item.portNum))

#由拓扑获取的信息，生成删除交换机端口gcl的xml
def topo2XML():

    global switchList      
    GetSwitchInfo()

    for switch in switchList:
        for portID in range(1,1+switch.portNum):
            #getSlotNumPayload=raisePayload.getSlotIndexPayload(portID)
            #reply=nc_operations.getConfig(str(switch.ipAddr),getSlotNumPayload)
            reply="adadadasd"
            SlotNum=reply.count('<index>')
            if SlotNum==0:
                print('There is no slot in Port ',portID,' of switch',switch.ipAddr)
            else:
                for slotIndex in range((SlotNum-1),-1,-1):
                    deleteSingleSlot=raisePayload.deleteSlotPayload(portID,slotIndex)
                    (switch.deleteSlotPayloadList).append(deleteSingleSlot)
    




