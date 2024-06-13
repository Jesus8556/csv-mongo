import pandas as pd
import matplotlib.pyplot as plt

# Cargar los resultados de la transformada desde el archivo CSV
resultados = pd.read_csv('resultado6.csv')

# Extraer las frecuencias y amplitudes del DataFrame
frecuencia = resultados['Frecuencia']
amplitud = resultados['Amplitud']

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(frecuencia, amplitud)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Transformada de Fourier')
plt.grid(True)

# Guardar la gráfica como una imagen
plt.savefig('transformada_fourier2.png')

# Mostrar la gráfica en pantalla
plt.show()
