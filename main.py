from Utilities import Quadtree_ChessCoord
import socket
import json
 
# Define the IP address and port on which the server will listen
UDP_IP = "192.168.2.103"  # this PC
UDP_PORT = 11
ESP_IP = "192.168.2.113" # ESP
ESP_PORT = 11

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Server is listening on {UDP_IP}:{UDP_PORT}")
ESP_addr = (ESP_IP,ESP_PORT)
while True:
    msg = input()   
    msg = msg.strip()  # remove leading/trailing white spaces
    if msg:# not empty message    
        try:
            msg = Quadtree_ChessCoord.find_coord(msg)
            msg = json.dumps(msg)# dump to json string
            sock.sendto(msg.encode(), (ESP_IP, ESP_PORT))
            print(f"send message: {msg}")
        except:
            print("please enter a coordinate input")
    if msg.lower() == "exit":  # exit
        print("exit")
        break
# test:
# print(Quadtree_ChessCoord.find_coord("A6"))
# [1, 3, 1]
