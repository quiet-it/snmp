import socket
import nmap
import os, subprocess
nm = nmap.PortScanner()
res = nm.scan('10.31.8.0/22', '22-443')
for host in res['scan']:
    print(res['scan'][host])
# nm = nmap3.Nmap()
# results = nm.scan_top_ports("10.31.8.0", args="-n -sP -PE -PA21,23,80,3389")

# print(nm.all_hosts())
# for host in nm.all_hosts():
#
#     print(nm[host].hostname())

    # print(socket.gethostbyaddr(host))
# hosts_list = [(x, nm[x]['status']['state'],socket.gethostbyaddr(x)[0]) for x in nm.all_hosts() if socket.gethostbyaddr(x)[0]]
# hosts_list = [(x, nm[x]['status']['state'],socket.gethostbyaddr(x)[0]) for x in nm.all_hosts() if socket.gethostbyaddr(x)[0]]
# for host, status,name in hosts_list:
#   print('{0}:{1}:{2}'.format(host, status,name))


# res = subprocess.check_output('nmap -sV -T4 -O -F --version-light -oX 10.31.8.185', shell=True)
# dict = xmltodict.parse(res)
# print(dict)








# nmap -sV -T4 -O -F --version-light 10.31.8.185
#
# nmap -T4 -F 10.31.8.185
