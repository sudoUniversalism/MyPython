def calc_iterat (Xo,Yo,h,x):
    for i in range(x):
        ka = 2*Xo*Xo + Yo
        kb_Xo = Xo + (h/2)
        kb_Yo = Yo + (h/2) * ka
        kb = 2*kb_Xo*kb_Xo + kb_Yo 
        kc_Xo = Xo + (h/2)
        kc_Yo = Yo + (h/2) * kb
        kc = 2*kc_Xo*kc_Xo + kc_Yo
        kd_Xo = Xo + h
        kd_Yo = Yo + h * kc
        kd = 2*kd_Xo*kd_Xo + kd_Yo 
        k = ka + kb + kc + kd
        M = (h * k)/6
        Y = Yo + M
        iterat = i + 1
        print "Result of iteration ",iterat
        print "is ",Y
        Yo = Y
        Xo = Xo + h
def calc (Xo,Yo,h,x):
    ka = 2*Xo*Xo + Yo
    kb_Xo = Xo + (h/2)
    kb_Yo = Yo + (h/2) * ka
    kb = 2*kb_Xo*kb_Xo + kb_Yo 
    kc_Xo = Xo + (h/2)
    kc_Yo = Yo + (h/2) * kb
    kc = 2*kc_Xo*kc_Xo + kc_Yo
    kd_Xo = Xo + h
    kd_Yo = Yo + h * kc
    kd = 2*kd_Xo*kd_Xo + kd_Yo 
    k = ka + kb + kc + kd
    M = (h * k)/6
    Y = Yo + M
    print "Result of iteration 1: ",Y
Xo = float(raw_input("Enter Xo: "))
Yo = float(raw_input("Enter Yo: "))
h = float(raw_input("Enter time interval: "))
x = int(raw_input("Enter number of iterations: "))
if (x > 1):
    calc_iterat (Xo,Yo,h,x)
elif (x == 1):
    calc (Xo,Yo,h,x)


