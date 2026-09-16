from scapy.all import *
from scapy.layers.l2 import Ether
from scapy.sendrecv import AsyncSniffer

print(conf.ifaces) # lists interfaces
print(conf.route)

a = Ether()


