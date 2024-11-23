class Gates:
    def land(a, b):
        if (a == 0 and b == 0):
            return 0
        elif (a == 0 and b == 1):
            return 0
        elif (a == 1 and b == 0):
            return 0
        elif (a == a and b == 1):
            return 1
        else:
            return ValueError
    
    def lor(a, b):
        if (a == 0 and b == 0):
            return 0
        elif (a == 0 and b == 1):
            return 1
        elif (a == 1 and b == 0):
            return 1
        elif (a == a and b == 1):
            return 1
        else:
            return ValueError
    
    def lnot(a):
        if (a == 1):
            return 0
        elif (a == 0):
            return 1
        else:
            return ValueError
    
    def lnand(a, b):
        if (a == 0 and b == 0):
            return 1
        elif (a == 0 and b == 1):
            return 1
        elif (a == 1 and b == 0):
            return 1
        elif (a == a and b == 1):
            return 0
        else:
            return ValueError
    
    def lnor(a, b):
        if (a == 0 and b == 0):
            return 1
        elif (a == 0 and b == 1):
            return 0
        elif (a == 1 and b == 0):
            return 0
        elif (a == a and b == 1):
            return 0
        else:
            return ValueError
    
