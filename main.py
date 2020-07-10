# from pysnmp.hlapi import *
import sys, datetime
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.hlapi import ContextData

cmdGen = cmdgen.CommandGenerator()
target = sys.argv[0]

host = '10.31.109.163'
community = 'public'

system_name = '1.3.6.1.2.1.43.9.2.1.8.1.1'

toner_max_copies = '1.3.6.1.2.1.43.11.1.1.8.1.1'
toner_left = '1.3.6.1.2.1.43.11.1.1.9.1.1'
number_of_printed_pages = '1.3.6.1.2.1.43.10.2.1.4.1.1'



def snmp_query(host, community, oid):
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        # ContextData(),
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((host, 161)),
        oid
    )

    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
            ))
        else:
            for name, val in varBinds:
                return(str(val))

result = {}
result['Time'] = datetime.datetime.utcnow().isoformat()
result['hostname'] = snmp_query(host, community, system_name)
result['max_copies'] = snmp_query(host, community, toner_max_copies)
result['toner_left'] = snmp_query(host, community, toner_left)
result['number_of_printed_pages'] = snmp_query(host, community, number_of_printed_pages)

print(result)
