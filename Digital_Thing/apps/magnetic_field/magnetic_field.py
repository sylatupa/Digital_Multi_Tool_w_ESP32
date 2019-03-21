hallV =666
triggerV = 555
#pubs
def hall():
    return 666

#pubs
def trigger_threshold(message=None):
    print('$$$trigger from hall',message)
    if hall() >= triggerV:
        return hall
    else:
        return 0

#subs
def trigger_value(x=555):
    triggerV = x 

#subs
def sample_rate(x):
    print('$$$new sample rate in hall',x)
    sample_rate = x/60 # 1 is one every second 60 is 60 per second 2/60
    return sample_rate
