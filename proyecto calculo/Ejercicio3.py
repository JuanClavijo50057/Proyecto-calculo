import math as mt

def sec(x):
    return 1.0/mt.cos(x)
 
def cot(x):
    return 1.0/mt.tan(x)
 
def csc(x):
    return 1.0/mt.sin(x)

y = (2/3)*mt.pi
L = 7
K = 9

def fx(x,y,L,K):
    func = K/mt.sin(x)+ L/mt.sin(180-x-y)
    return func

def Dfx(x,y,L,K):
    dFunc = L*cot(x+y-180)*csc(x+y-180)-K*cot(x)*csc(x)
    return dFunc

def SDfx(x,y,L,K):
    SDfunc = K*csc(x)*(csc(x)**2+cot(x)**2)-L*csc(x+y-180)*(csc(x+y-180)**2+cot(x+y-180)**2)
    return SDfunc

def newtomRaphsonMax(x0,tol,y,L,K):
    i=0
    x=0
    while abs(x0-x)>tol:
        i=i+1
        x=x0
        x0=x0-(Dfx(x0,y,L,K)/SDfx(x0,y,L,K))
        print("iteracion:",i)
        print(round(x0,7))
        
    z = fx(x0,y,L,K)
    print("Punto maximo: (", round(x0,7),",",round(z,7),")")
    
newtomRaphsonMax(1, 0.9*pow(10,-5),y,L,K)