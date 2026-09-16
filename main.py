from scapy.all import *
from scapy.layers import dhcp


default_gateway = conf.route.route("0.0.0.0")[2]
print(default_gateway)
print(conf.route)

#print(conf.ifaces) # lists interfaces
#print(conf.route)

a = Ether()

#p = sr1(
#    IP(dst="example.com") / ICMP() / "XXXXXXXXXXX"
#)


#reply = sr1(IP(dst="8.8.8.8")/ICMP())
#if reply:
#    reply.show()