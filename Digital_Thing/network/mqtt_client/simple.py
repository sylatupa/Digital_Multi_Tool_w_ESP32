    from umqtt.simple import MQTTClient
    

defgt
        c = MQTTClient("umqtt_client", "192.168.1.55")
        c.connect()
        #c.publish(b"foo_topic", b"hello")
        c.disconnect()

        c.set_callback(sub_cb)
        c.connect()
        c.subscribe(b"#")
        while True:
            # Non-blocking wait for message
            c.check_msg()
            time.sleep(1)
        c = MQTTClient("umqtt_client", "192.168.1.55")
 
