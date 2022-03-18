#对端口的gcl使能、时间槽数量和循环时间进行设定
def portInitialPayload(portID,controlListLength,cycleTime,portEnabled=True,gateEnabled=True):
  payload="""
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched">
    <interface>
      <name>"""+str(portID)+"""</name>
      <enabled>"""+str(portEnabled)+"""</enabled>
      <sched:gate-parameters>
        <sched:gate-enabled>"""+str(gateEnabled)+"""</sched:gate-enabled>
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

def CLIFuncForHirschmannSwitch():
  pass

"""
#!/bin/sh
 
user="admin"
password="private"
ip="192.168.0.7"
 
{
  sleep 1
  echo "$user";     // 登录用户名
  sleep 1
  echo "$password";     // 登录密码
  enbale
  configure
  interface 1/1
  tsn gcl add id 1 gate-states 0,1,2,3,4,5,6,7 interval 4100
  ...
  tsn commit
  exit
  exit
  exit
  logout
  y
        
 
}|telnet $ip

"""