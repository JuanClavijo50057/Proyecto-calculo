import math as mt
#Halla los cortes con el eje x de la funcion
def fx(x):
    func=mt.e**-x +mt.sin(x) -x**2 +x -2
    return func
def Dfx(x):
    dFunc=-mt.e**-x +mt.cos(x) -2*x +1
    return dFunc
def newtomRaphson(x0, tol):
    i=0
    x=0
    while abs(x0-x)>tol:
        i=i+1
        x=x0
        x0=x0-(fx(x0)/Dfx(x0))
        print("iteracion:",i)
        print(round(x0,7))
    print("el corte con el eje x es:", round(x0,7))    

newtomRaphson(-2.5, 0.9*10**-5)