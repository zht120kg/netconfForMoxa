import lxml.etree as ET
#from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

#默认为moxa交换机，NETCONF的running库
def editConfig(host,payload,username='admin',password='moxa',target='running'):
    # connect to netconf agent
    with manager.connect(host=host,
                         port=830,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'': ''}) as m:

        # execute netconf operation
        try:
            response = m.edit_config(target=target, config=payload).xml
            data = ET.fromstring(response)
        except RPCError as e:
            data = e._raw

        # beautify output
        print(ET.tostring(data, pretty_print=True))



def getConfig(host,payload,username='admin',password='moxa',target='running'):
    # connect to netconf agent
    with manager.connect(host=host,
                         port=830,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'': ''}) as m:

        # execute netconf operation
        try:
            response = m.get_config(source=target, filter=payload).xml
            data = ET.fromstring(response)
        except RPCError as e:
            data = e._raw

        # beautify output
        return ET.tostring(data, pretty_print=True)