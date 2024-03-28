import math as mt

def fx(x):
    func=mt.e**-x +mt.sin(x) -x**2 +x -2
    return func
def Dfx(x):
    dFunc=-mt.e**-x +mt.cos(x) -2*x +1
    return dFunc
def SDfx(x):
    SDfunc=mt.e**-x -mt.sin(x) -2
    return SDfunc
def newtomRaphsonMax(x0,tol):
    i=0
    x=0
    while abs(x0-x)>tol:
        i=i+1
        x=x0
        x0=x0-(Dfx(x0)/SDfx(x0))
        # print("iteracion:",i)
        # print(round(x0,7))
        
    y=fx(x0)
    print("Punto maximo: (", round(x0,7),",",round(y,7),")")
def newtomRaphsonMin(x0,tol):
    i=0
    x=0
    while abs(x0-x)>tol:
        i=i+1
        x=x0
        x0=x0-(Dfx(x0)/SDfx(x0))
        # print("iteracion:",i)
        # print(round(x0,7))
        
    y=fx(x0)
    print("Punto minimo: (", round(x0,7),",",round(y,7),")")

newtomRaphsonMax(1, 0.5*pow(10,-5))
newtomRaphsonMin(-1, 0.5*pow(10,-5))