try:
    accel = pyb.Accel()
    SENSITIVITY = 3
    x = accel.x()
    y = accel.y()
except:
    print("spirit_level failed")
