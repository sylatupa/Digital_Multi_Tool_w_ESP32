try:
    import socket
except:
    print("socket import failure")
UDP_IP = "127.0.0.1"
UDP_PORT = 8200
MESSAGE = "Hello, World!"

from math import sqrt

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
    print("sending line", line)
    sock = get_socket()
    sock.sendto((line+end).encode('utf-8'),(UDP_IP,UDP_PORT))

# this was code used for streaming a text file over UDP, good for the desktop app, not esp32
# TODO: break up into reusable code
 
xhistory = [0]
yhistory = [0]
zhistory = [0]

xhist = []
yhist = []
zhist = []

velhistory = [0]
accelhistory = [0]
jerkhistory = [0]
snaphistory = [0]

def crack(snapval): # chang in velocity is acceleration
    cracked = snaphistory[0] - snapval
    snaphistory[0] = snapval
    return cracked 

def snap(jerkval): # chang in velocity is acceleration
    snapped = jerkhistory[0] - jerkval
    jerkhistory[0] = jerkval
    return snapped

def jerk(accelval): # chang in velocity is acceleration
    jerked = accelhistory[0] - accelval
    accelhistory[0] = accelval
    return jerked

def acceleration(velval): # chang in velocity is acceleration
    accel = velhistory[0] - velval
    velhistory[0] = velval
    return accel

def xChange(xval):
    xChange = xhistory[0] - xval
    xhistory[0] = xval;
    return xChange
def yChange(yval):
    yChange = yhistory[0] - yval
    yhistory[0] = yval;
    return yChange

def zChange(zval):
    zChange = zhistory[0] - zval
    zhistory[0] = zval;
    return zChange

timeHistory = [0] 

def timeChange(timeVal):
    timeChanged = timeHistory[0] - timeVal
    timeHistory[0] = timeVal
    print("time change:" , timeChanged)
    return timeChanged

slideHistory=[0]
MSlide = 10
def slide(x):
    slideHistory[0] = slideHistory[0] + ((x - slideHistory[0])/MSlide)
    return slideHistory[0]

smth_val = 100
def xSmooth(x):
    if len(xhist)< smth_val:
        xhist.append(x)
    else:
        xhist.pop(0)
        xhist.append(x)
    return float(sum(xhist))/(len(xhist)+1)

def ySmooth(y):
    if len(yhist)< smth_val:
        yhist.append(y)
    else:
        yhist.pop(0)
        yhist.append(y)
    return float(sum(yhist))/(len(yhist)+1)

def zSmooth(z):
    if len(zhist)< smth_val:
        zhist.append(z)
    else:
        zhist.pop(0)
        zhist.append(z)
    return float(sum(zhist))/(len(zhist)+1)

def magnitude(x,y,z):
    positionVector = sqrt(x**2+y**2+z**2)
    return positionVector
global end

def testingUDP():
    global end
    xsmooth = 0
    ysmooth = 0
    zsmooth = 0
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")   
    #import software.files_io as fio
    import os, sys, time
    #import network.UDP as UDP
    data = 'Digital_Multi_Tool_w_ESP32/data/TrackingData.txt'
    #dataFile = os.listdir(dataPath)[4]
    openFile = open(data)
    timeFrame = .1
    totalTime = 0
    n = 0
    for row in openFile:
        #Name       Frame   Time    x           y           z
        #RightHand  180     1.5     -3.554374   0.972789    -1.879561
        #0          1       2       3           4           5
        end = row[-1]
        sendto("n " +  str(n))
        if n > 3:
            timeFrame = abs(timeChange(timeFrame))
            totalTime += timeFrame
            x = float(row.split(" ")[3])
            sendto("x " +  str(x))
            y = float(row.split(" ")[4])
            sendto("y " +  str(y))
            z = float(row.split(" ")[5])
            sendto("z " +  str(z))
            timeFrame = .1

            xsmooth = float(xSmooth(x))
            ysmooth = float(ySmooth(y))
            zsmooth = float(zSmooth(z))
            sendto("xsmooth " +  str(xsmooth))
            sendto("ysmooth " +  str(ysmooth))
            sendto("zsmooth " +  str(zsmooth))
            #row = row[ :-1]
            mag = magnitude(x,y,z)
            #mag = magnitude(xsmooth,ysmooth,zsmooth)
            sendto("mag " +  str(mag))
            vel = xChange(mag)
            sendto("vel " +  str(vel))
            accel = acceleration(vel)
            sendto("accel " +  str(accel))
            jerked = jerk(accel)
            sendto("jerked " +  str(jerked))
            snapped = snap(jerked)
            sendto("snapped " +  str(snapped))
            cracked = crack(snapped)
            sendto("cracked " +  str(cracked))

            time.sleep(timeFrame)
            #time.sleep(.001)
        n += 1


testingUDP()
