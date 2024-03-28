import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,200)

f=np.e**-x+np.sin(x)-x**2+x-2

plt.figure()
plt.plot(x,f,)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica de la funcion')
plt.grid(True)
plt.xticks(np.arange(-3,3+1,1))

plt.show()