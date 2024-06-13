import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos del archivo CSV
data = pd.read_csv('data1.csv', header=None)
values = data[0].values

# Calcular la transformada de Fourier
fft_values = np.fft.fft(values)
frequencies = np.fft.fftfreq(len(values))

# Graficar el resultado
plt.figure(figsize=(12, 6))

# Magnitud de la FFT
plt.subplot(2, 1, 1)
plt.plot(frequencies, np.abs(fft_values))
plt.title('Magnitud de la Transformada de Fourier')
plt.xlabel('Frecuencia')
plt.ylabel('Magnitud')

# Fase de la FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.angle(fft_values))
plt.title('Fase de la Transformada de Fourier')
plt.xlabel('Frecuencia')
plt.ylabel('Fase')

plt.tight_layout()

# Guardar la gráfica como un archivo de imagen
plt.savefig('fft_result.png')
print("Gráfica guardada como 'fft_result.png'")
