import math as mt

a = 1
b = -4
c = 5

def fx(x, a, b, c):
    func = mt.sqrt(x**2 + (a*(x**2) + b*x + c)**2)
    return func

def Dfx(x ,a , b, c):
    dFunc = (2*(2*a*x+b)*(a*x**2+b*x+c)+2*x)/(2*mt.sqrt((a*x**2+b*x+c)**2 + (x**2)))
    return dFunc

def SDfx(x ,a , b, c):
    SDfunc = (2*(2*a*x+b)**2 + 4*a*(a*x**2+b*x+c)+2)/(2*mt.sqrt((a*x**2+b*x+c)**2+x**2))-(2*(2*a*x+b)*(a*x**2+b*x+c)+2*x)**2/(4*((a*x**2+b*x+c)**2+x**2)**(3/2))
    return SDfunc

def newtomRaphsonMin(x0,tol):
    i=0
    x=0
    while abs(x0-x)>tol:
        i = i + 1
        x = x0
        x0 = x0 - (Dfx(x0, a,b,c) / SDfx(x0,a,b,c))
        print("iteracion:",i)
        print(round(x0,7))
        
    y = a*x**2 + b*x + c
    print("Punto minimo: (", round(x0,7),",",round(y,7),")")
    print("La distancia mínima entre el origen y la función es: ", round(fx(x0,a,b,c),7))
    
newtomRaphsonMin(1.5 , 0.5*pow(10,-5))