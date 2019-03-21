try:
    import socket
except:
    print("socket import failure")
UDP_IP = "127.0.0.1"
UDP_PORT = 8200
MESSAGE = "Hello, World!"

#print("UDP target IP:", UDP_IP)
#print("UDP target port:", UDP_PORT)
#print("message:", MESSAGE)

def get_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))


def set_UDP_ip(ip):
    UDP_IP = ip

def set_UPD_port(port):
    UDP_PORT = port

def sendto(line):
    sock = get_socket()
    sock.sendto(line.encode('utf-8'),(UDP_IP,UDP_PORT))


# this was code used for streaming a text file over UDP, good for the desktop app, not esp32
# TODO: break up into reusable code

def testingUDP():
    import software.files_io as fio
    import os, sys, time
    import network.UDP as UDP
    UDP.sendto("abc")
    dataPath = 'Digital_Multi_Tool_w_ESP32/data/dance'
    dataFile = os.listdir(dataPath)[4]
    print("Reading File:" + dataFile)
    openFile = fio.getOPENfile(dataPath +"/"+dataFile)
    for row in openFile:
        UDP.sendto(row.replace(","," "))
        print(row)
        time.sleep(1)

