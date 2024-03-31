import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,4,100)
g=x**2-4*x+5
p=[1.446262]
z=[1.3064475]
# y=plt.quiver(0,0,1,1, scale_units='xy',angles='xy',scale=0.8)
# plt.xlim(0,4)
# plt.ylim(0,4)


plt.figure()
plt.plot(x,g)
plt.scatter(p,z,color="black")

plt.annotate('  (1.44626 , 1.30644) minimo', xy=((1.446262,1.3064475)))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica de la funcion')
plt.grid(True)
plt.yticks(np.arange(0,5+1,1))
plt.xticks(np.arange(0,5+1,1))

plt.show()