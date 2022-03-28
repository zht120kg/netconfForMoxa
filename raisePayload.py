#对端口的gcl使能、时间槽数量和循环时间进行设定
def portInitialPayload(portID,controlListLength,cycleTime,portEnabled='true',gateEnabled='true'):
  payload="""
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched">
    <interface>
      <name>"""+str(portID)+"""</name>
      <enabled>"""+portEnabled+"""</enabled>
      <sched:gate-parameters>
        <sched:gate-enabled>"""+gateEnabled+"""</sched:gate-enabled>
        <sched:admin-control-list-length>"""+str(controlListLength)+"""</sched:admin-control-list-length>
        <sched:admin-cycle-time>
          <sched:numerator>"""+str(cycleTime)+"""</sched:numerator>
          <sched:denominator>1000000000</sched:denominator>
        </sched:admin-cycle-time>
      </sched:gate-parameters>
    </interface>
  </interfaces>
</config>
"""
  return payload



#增加/修改单个时间槽,时间单位：纳秒
def createSlotPayload(portID,slotIndex,gataStateValue,timeIntervalValue):
  payload = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched">
    <interface>
      <name>"""+str(portID)+"""</name>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:iana-interface-type</type>
      <sched:gate-parameters>
        <sched:admin-control-list>
          <sched:index>"""+str(slotIndex)+"""</sched:index>
          <sched:operation-name xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched">sched:set-gate-states</sched:operation-name>
          <sched:sgs-params>
            <sched:gate-states-value>"""+str(gataStateValue)+"""</sched:gate-states-value>
            <sched:time-interval-value>"""+str(timeIntervalValue)+"""</sched:time-interval-value>
          </sched:sgs-params>
        </sched:admin-control-list>
      </sched:gate-parameters>
    </interface>
  </interfaces>
</config>
"""
  return payload 



#删除单个时间槽，时间单位：纳秒
def deleteSlotPayload(portID,slotIndex):
  payload = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched">
    <interface>
      <name>"""+str(portID)+"""</name>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:iana-interface-type</type>
      <sched:gate-parameters>
        <sched:admin-control-list xc:operation="delete">
          <sched:index>"""+str(slotIndex)+"""</sched:index>
          <sched:operation-name xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched">sched:set-gate-states</sched:operation-name>
        </sched:admin-control-list>
      </sched:gate-parameters>
    </interface>
  </interfaces>
</config>
"""
  return payload



#获取交换机端口的时间槽数量
def getSlotIndexPayload(portID):
  payload="""
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched">
    <interface>
      <name>"""+str(portID)+"""</name>
      <sched:gate-parameters>
        <sched:admin-control-list>
          <sched:index/>
          <sched:operation-name xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched">sched:set-gate-states</sched:operation-name>
        </sched:admin-control-list>
      </sched:gate-parameters>
    </interface>
  </interfaces>
</filter>
"""
  return payload



#赫斯曼交换机的CLI配置方法
def raiseSingleGCL_CLI(slotID,queueIndex,timeIntervalValue):
  singleGCL='tsn gcl add id ' +str(slotID)+ ' gate-states ' +queueIndex+ ' interval ' +str(timeIntervalValue)\
    +'\n'
  return singleGCL



def raiseHirschmannSwitchCLI(portID,cycleTime,gcl_CLIs):
  if portID!=1 and portID!=2:  #赫斯曼交换机的常用TSN口只有1口与2口
    return 
    #print("Only Port1 & Port2 are TSN Ports")
  else: 
    ScriptContent="""interface 1/"""+str(portID)+"""
tsn gcl delete all
tsn gates operation enable
tsn cycle-time """+str(cycleTime)+'\n'+ gcl_CLIs +'tsn commit\n'+'exit\n'  
    return ScriptContent





    #import os
    #from stat import  S_IRWXU
    # ScriptPath='./HirschmannCLI.sh'
    # with open(ScriptPath,"w") as Script:
    #   Script.writelines(ScriptContent)
    # os.chmod(ScriptPath,S_IRWXU)  #给脚本添加执行权限


  
