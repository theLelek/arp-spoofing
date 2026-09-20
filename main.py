from scapy.all import *


default_gateway = conf.route.route("0.0.0.0")[2]
print(default_gateway)
print(conf.route)

#print(conf.ifaces) # lists interfaces
#print(conf.route)


# Capture only 10 packets
packets = sniff(count=10)

# Display a simple summary
packets.summary()


arp_response = (
    Ether(
        dst="aa:bb:cc:dd:ee:ff"
    )
    / ARP(
        op="is-at",
        hwsrc="11:22:33:44:55:66",
        psrc="192.168.1.1",
        hwdst="aa:bb:cc:dd:ee:ff",
        pdst="192.168.1.100"
    )
)

packet.show()
