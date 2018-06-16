# Must download Scapy library and create Twilio account before running
from scapy.all import *
from twilio.rest import Client


# Prints when script is listening for button press to send arp packet
print("Program Listening...\n")


#twilio account information
account = "Twilio_Account_#"
token = "Twilio_Token_#"
client = Client(account, token)


#replace the MAC add and phone numbers with corresponding numbers
def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == "Amazon_Dash_Button_MAC_Address":	
            print("ARP Probe from: Amazon_Dash_Button_MAC_Address" + pkt[ARP].hwsrc + "\n")
            message = client.messages.create(
				to="+Recieving_Phone_#",
				from_="+Sending_Phone_#",
                body="I NEED HELP!")
            print("Message sent \n")

			
# prints when sniffing is completed
# change the store and count to how many messages you want sent
print(sniff(prn=arp_display, filter="arp", store=1, count=1))
