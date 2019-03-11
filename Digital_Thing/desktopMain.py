if __name__=="__main__":
    import subprocess as sp
    #sp.call('cls',shell=True)
    tmp = sp.call('clear',shell=True)

    import Digital_Thing.Menu as mn 
    menu = mn.Menu()
    while True:
        menu.menu_event() 


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
