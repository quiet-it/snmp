import os


subnet = '10.31.109.'

def get_info(host):
    info = {}
    info['consum'] = os.system('./check_snmp_printer -H '+host+' -C public -x "CONSUM ALL" -w 25 -c 10')
    info['model'] = os.system('./check_snmp_printer -H '+host+' -C public -x "MODEL"')
    info['devices'] = os.system('./check_snmp_printer -H '+host+' -C public -x "DEVICES"')
    info['tray'] = os.system('./check_snmp_printer -H '+host+' -C public -x "TRAY ALL"')
    info['status'] = os.system('./check_snmp_printer -H '+host+' -C public -x "STATUS"')

    return info

def ping(host):
    ping = os.system('ping -v -c 1 ' + subnet + str(x))
    if ping == 0:
        print("Host " + subnet + str(x) + ' is online')
    else:
        print("Host " + subnet + str(x) + ' is offline')
# print(get_info('10.31.101.200'))

x = 1
while x < 255:
    x+=1
    ping(x)
