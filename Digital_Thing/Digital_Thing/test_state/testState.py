from simple_device import SimpleDevice
device = SimpleDevice()

device.on_event('device_locked')
print(device.state)
device.on_event('pin_entered')
print(device.state)
device.on_event('device_locked')
print(device.state)
