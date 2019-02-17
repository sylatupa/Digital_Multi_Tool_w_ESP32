>>> import dht
>>> import machine
>>> d = dht.DHT11(machine.Pin(4))

>>> import dht
>>> import machine
>>> d = dht.DHT22(machine.Pin(4))

Then measure and read their values with:

>>> d.measure()
>>> d.temperature()
>>> d.humidity()


