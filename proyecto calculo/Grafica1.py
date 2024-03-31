import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,200)
f=np.e**-x+np.sin(x)-x**2+x-2
p=[0.6374874]
z=[-0.6451056]
t=[-1.3714047]
q=[-2.2914602]
a=[-2.3676666]
b=[0]

plt.figure()
plt.plot(x,f)
plt.scatter(p,z,color="black")
plt.scatter(t,q,color="black")
plt.scatter(a,b,color="black")

plt.annotate('  (0.63748,-0.64510) maximo', xy=(0.6374874 , -0.6451056))
plt.annotate('  (-1.37140,-2.29146) minimo', xy=(-1.3714047 , -2.2914602))
plt.annotate('  (-2.36766,0) corte', xy=(-2.3676666 , 0))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica de la funcion')
plt.grid(True)
plt.xticks(np.arange(-3,3+1,1))

plt.show()