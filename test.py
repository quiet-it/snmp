import os, subprocess


subnet = '10.31.109.'

def get_info(host):
    info = {}
    info['consum'] = os.system('./check_snmp_printer -H '+host+' -C public -x "CONSUM ALL" -w 25 -c 10')
    info['model'] = os.system('./check_snmp_printer -H '+host+' -C public -x "MODEL"')
    info['devices'] = os.system('./check_snmp_printer -H '+host+' -C public -x "DEVICES"')
    info['tray'] = os.system('./check_snmp_printer -H '+host+' -C public -x "TRAY ALL"')
    info['status'] = os.system('./check_snmp_printer -H '+host+' -C public -x "STATUS"')

    return info

def host_type(type,location):
    sites = {
        'saratoga' : '10.21.',
        'barnum' : '10.31.',
        'jackson' : '10.31.'
    }
    subnet = {
        'pc' : '8',
        'printer' : '9',
        'z_printer' : '10'
    }

    if location == 'jackson':
        subnet = {
            'pc' : '108',
            'printer' : '109',
            'z_printer' : '110'
        }
    return str(sites[location]) + str(subnet[type]) + '.{}'

def lookup(addr):
     try:
         return socket.gethostbyaddr(addr)
     except socket.herror:
         return None, None, None

with open(os.devnull, "wb") as limbo:
        for n in range(1, 254):
                ip=host_type('printer', 'jackson').format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print(ip, "inactive")
                else:
                        print(ip, "active")
