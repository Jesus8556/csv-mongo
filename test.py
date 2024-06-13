import numpy as np
from scipy.fft import fft
import pandas as pd
import requests
# Parámetros dados
fmax = 3000
size = 802

# Cargar los datos desde el archivo CSV
data = pd.read_csv('data5.csv', header=None)

# Tomar solo la columna de datos (asumiendo que están en la primera columna)
datos = data[0].values  # Convertir los datos a un arreglo NumPy

# Aplicar la transformada de Fourier
transformada = fft(datos)

# Calcular la amplitud (usando el valor absoluto de los coeficientes)
amplitud = np.abs(transformada)

# Calcular la frecuencia correspondiente a cada coeficiente de la transformada
frecuencia = np.fft.fftfreq(size, 1/fmax)







# Por ejemplo, si quieres guardarlos en un archivo CSV:
resultados = pd.DataFrame({'Frecuencia': frecuencia, 'Amplitud': amplitud})
resultados.to_csv('resultado6.csv', index=False)
