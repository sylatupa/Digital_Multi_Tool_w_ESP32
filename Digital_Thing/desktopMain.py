if __name__=="__main__":
    import subprocess as sp
    import software.files_io as fio

    #sp.call('cls',shell=True)
    tmp = sp.call('clear',shell=True)
 
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
