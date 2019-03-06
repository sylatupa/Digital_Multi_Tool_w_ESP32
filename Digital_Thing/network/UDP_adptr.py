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
