#from active state github repo, code recepies.
# https://github.com/rickyhan/portal/blob/master/getch.py
#this is a helper file that allows for keyboard interaction
#renaming from getch to keyboard
class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            print("importing getch unix")
            self.impl = _GetchUnix()
    def __call__(self): return self.impl()
class _GetchUnix:
    def __init__(self):
        import sys,select,termios,tty
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
    def __call__(self):
        import sys, tty, termios,select
        #fd = sys.stdin.fileno()
        #old_settings = termios.tcgetattr(fd)
        #try:
        if True:
            input = select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
            if input:
                value = sys.stdin.read(1)
                return value
        #except:
        #    pass
        #finally:
        #    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        #return ch
class _GetchWindows:
    def __init__(self):
        import msvcrt
    def __call__(self):
        #import msvcrt
        if msvcrt.kbhit(): # <--------
            key = msvcrt.getch()
            print("a to exit, current key: "+ key)
            if key == 'a':
                sys.exit()
            return key
class _GetchMacCarbon:
    """
    A function which returns the current ASCII key that is down;
    if no ASCII key is down, the null string is returned.  The
    page http://www.mactech.com/macintosh-c/chap02-1.html was
    very helpful in figuring out how to do this.
    """
    def __init__(self):
        import Carbon

    def __call__(self):
        import Carbon
        if Carbon.Evt.EventAvail(0x0008)[0]==0: # 0x0008 is the keyDownMask
            return ''
        else:
            (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            return chr(msg)


