if __name__=="__main__":
    import subprocess as sp
    #sp.call('cls',shell=True)
    tmp = sp.call('clear',shell=True)

    import Digital_Thing.Menu as mn 
    menu = mn.Menu()
    while True:
        menu.menu_event() 
