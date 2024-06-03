y1=[0, 0.12, 0.32, 1.1, 1.2, 0.8, 0.53, 0.5, 0.3, 0.15, 0]
y2=[0, -0.16, -0.16, -0.1, -0.1, -0.15, -0.16, -0.18, -0.18, -0.15, 0]

suma1=0
for n in range(0,11,2):
    resta=(y1[n]-y2[n])*2
    suma1= suma1+resta

suma2=0
for n in range(1,11,2): 
    resta=(y1[n]-y2[n])*4
    suma2=suma2+resta

a=0
b=3
n=10
deltax=(b-a)/n
result=(suma1+suma2)*(deltax/3)
print(result)   