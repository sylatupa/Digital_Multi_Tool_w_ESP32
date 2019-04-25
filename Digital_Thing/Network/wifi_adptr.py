def connect(ssid,password):
    import network
    import time
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            for t in range(0, 120):
                if sta_if.isconnected() != True:
                    print('Oh Yes! Get connected')
                    time.sleep_ms(200)
                    sta_if.active(True)
                    sta_if.connect(ssid, pwd)
                else:
                    break

    print('network config:', sta_if.ifconfig())
