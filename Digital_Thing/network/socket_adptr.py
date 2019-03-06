def get_socket(hostName):
    ssid     = "spyprjct-219"
    password = "789sumrX"
    host     = "192.168.1.115"
    ai = socket.getaddrinfo(host,4444)
    socket = socket.socket()
    socket.connect(ai[0][-1])
    #s = ssl.wrap_socket(socket)
    return socket

def close_socket(socket):
    socket.close()
