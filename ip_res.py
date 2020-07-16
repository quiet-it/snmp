import socket, os, textwrap, inspect, re

def get_hostname(ip):
    out = os.popen('nmblookup -A ' + ip).read()
    out = out.splitlines()
    out = out[1].split(' ')
    regex = re.compile(r'[\n\r\t]')
    s = regex.sub(" ", out[0])
    return s
