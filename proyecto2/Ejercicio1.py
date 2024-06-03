import math as mt

def g(x):
    f=(mt.e**-x)+(x**2)-mt.sin(x)+1
    return f
def hx(x):
    func=4-3*x**2+mt.log(x)-(mt.e**-x)+mt.sin(x)
    return func
def Dfx(x):
    dFunc=mt.cos(x)+(mt.e**-x)+(1/x)-6*x
    return dFunc
def newtomRaphson(x0, tol):
    i=0
    x=0
    while abs(x0-x)>tol:
        i=i+1
        x=x0
        x0=x0-(hx(x0)/Dfx(x0))
        print("iteracion:",i)
        print(round(x0,7))
    y0=g(x0)
    print("El punto de interseccion es:", "(", round(x0,7), ",", round(y0,8), ")")       

newtomRaphson(1.5, 0.9*10**-6)
newtomRaphson(0.1, 0.9*10**-6)

def funIntegral(x):
    fInt=(5-2*(x**2)+mt.log(x))-((mt.e**-x)+(x**2)-mt.sin(x)+1)
    return fInt 

a=0.04576654
b=1.281835
n=500
deltaX=(b-a)/n

suma1=0
for i in range(1,n,2):
    deltaX=(b-a)/n
    xi=a+i*deltaX
    suma1=suma1+funIntegral(xi)

suma2=0     
for j in range(2,n,2):
    xj=a+j*deltaX
    suma2=suma2+funIntegral(xj)  

R=(deltaX/3)*(funIntegral(a)+4*suma1+2*suma2+funIntegral(b))

print("El area aproximada de la region R es:", round(R,7)) 