def connect(ssid,password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        #while not sta_if.isconnected():
        #    pass
        for t in range(0, 120):
            if sta_if.isconnected():
                print('Oh Yes! Get connected')
            time.sleep_ms(200)
            # Stage two: if not yet connected and after a hard reset activate and connect
            if t == 60 and hard_reset:
                sta_if.active(True)
                sta_if.connect(ssid, pwd)
    print('network config:', sta_if.ifconfig())
