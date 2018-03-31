def calc(Xo,Yo,h,x):
    k = Xo + Yo
    Y = Yo + (h * k)
    print "Result of iteration 1: ",Y
def calc_iterat (Xo,Yo,h,x):
    for i in range(x):
        k = Xo + Yo
        Y = Yo + (h * k)
        iterat = i + 1
        print "Result of iteration ",iterat
        print "is ",Y
        Yo = Y
        Xo = Xo + h
Xo = float(raw_input("Enter Xo: "))
Yo = float(raw_input("Enter Yo: "))
h = float(raw_input("Enter time interval: "))
x = int(raw_input("Enter number of iterations: "))
if (x > 1):
    calc_iterat (Xo,Yo,h,x)
elif (x == 1):
    calc (Xo,Yo,h,x)

