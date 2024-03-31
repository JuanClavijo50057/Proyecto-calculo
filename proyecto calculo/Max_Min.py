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
def newtomRaphson(x0,tol,mensaje):
    i=0
    x=0
    while abs(x0-x)>tol:
        i=i+1
        x=x0
        x0=x0-(Dfx(x0)/SDfx(x0))
        
    y=fx(x0)
    print(mensaje,"(", round(x0,7),",",round(y,7),")")
    


newtomRaphson(1, 0.9*10**-5, "punto maximo")
newtomRaphson(-1, 0.9*10**-5, "punto minimo")
