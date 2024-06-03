import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def f(x):
    return 5 - 2*x**2 + np.log(x)

def g(x):
    return np.exp(-x) + x**2 - np.sin(x) + 1

# Crear el rango de valores para x
x_full_range = np.linspace(-2, 5, 700)
x_positive_range = np.linspace(0.1, 5, 400)

# Calcular los valores de las funciones
y_f_positive = f(x_positive_range)
y_g_full = g(x_full_range)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_positive_range, y_f_positive, label='$f(x) = 5 - 2x^2 + \ln(x)$')
plt.plot(x_full_range, y_g_full, label='$g(x) = e^{-x} + x^2 - \sin(x) + 1$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Gráfica de las funciones $f(x)$ y $g(x)$')
plt.axvline(0, color='grey', linestyle='--', linewidth=0.5)  # Añadir línea vertical en x=0
plt.legend()
plt.grid(True)
plt.show()