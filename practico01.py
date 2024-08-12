# -*- coding: utf-8 -*-
"""practico01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v6b_X2endY0qa8aSSGutTr_N-oUvjQTE

##Librerías
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Generación de datos Estatura"""

np.random.seed(25)
Es = np.random.uniform(1.45, 2.1, 100)
Ps = []

"""### Gereración de datos Peso"""

for E in Es:
    # minimo y maximo en base a la estatura
    P_min = 17 * (E ** 2)
    P_max = 25 * (E ** 2)
    peso = np.random.uniform(P_min, P_max)
    Ps.append(peso)  # Añadir el peso a la lista de pesos

"""### Crear un DataFrame con los datos y conseguir datos necesarios"""

data = pd.DataFrame({
    'Estatura (m)': Es,
    'Peso (kg)': Ps
})

sx = 0
sy = 0
sxy = 0
sx2 = 0
n = len(data)

for i in range(n):
    x = data['Estatura (m)'].iloc[i]
    y = data['Peso (kg)'].iloc[i]
    sx += x
    sy += y
    sxy += x * y
    sx2 += x ** 2

"""### Calcular la pendiente (m) y la intersección (b) de la recta y = mx + b"""

x = data['Estatura (m)']
y = data['Peso (kg)']
m = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
b = (sy - m * sx) / n

"""### Creamos la recta con lo datos obtenidos"""

y_line = m * x + b

"""### Visualización de los datos generados y la recta ajustada"""

plt.scatter(data['Estatura (m)'], data['Peso (kg)'], color='blue', label='Datos')
plt.plot(x, y_line, color='red', label='Línea ajustada')
plt.title('Estatura vs Peso con Línea Ajustada')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()