import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,4,100)
g=x**2-4*x+5
p=[1.446262]
z=[1.3064475]

plt.figure()
plt.plot(x,g)
plt.scatter(p,z,color="black")

plt.annotate('  (1.44626 , 1.30644) punto mas cercano', xy=((1.446262,1.3064475)))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica de la funcion')
plt.grid(True)
plt.yticks(np.arange(0,5+1,1))
plt.xticks(np.arange(0,5+1,1))

plt.show()