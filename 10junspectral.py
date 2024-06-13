import pandas as pd
import numpy as np
import requests
from scipy.fftpack import fft, fftfreq

# Leer el archivo CSV
file_path = 'dato2.csv'
data = pd.read_csv(file_path)

# Separar los datos por eje
data_x = data[data['axis'] == 'x']['value'].values
data_y = data[data['axis'] == 'y']['value'].values
data_z = data[data['axis'] == 'z']['value'].values

# Definir la frecuencia de muestreo
sampling_rate = 1 / 600

# Calcular la longitud de la señal
n_x = len(data_x)
n_y = len(data_y)
n_z = len(data_z)

# Calcular la FFT para cada eje
fft_values_x = fft(data_x)
fft_values_y = fft(data_y)
fft_values_z = fft(data_z)

# Calcular las frecuencias
freq_x = fftfreq(n_x, d=sampling_rate)[:n_x // 2]
freq_y = fftfreq(n_y, d=sampling_rate)[:n_y // 2]
freq_z = fftfreq(n_z, d=sampling_rate)[:n_z // 2]

# Construir la estructura JSON
spectral_data = {
    "frecMax": max(freq_x.max(), freq_y.max(), freq_z.max()),
    "modoX": {
        "frecuencia": freq_x.tolist(),
        "amplitud": np.abs(fft_values_x)[:n_x // 2].tolist()
    },
    "modoY": {
        "frecuencia": freq_y.tolist(),
        "amplitud": np.abs(fft_values_y)[:n_y // 2].tolist()
    },
    "modoZ": {
        "frecuencia": freq_z.tolist(),
        "amplitud": np.abs(fft_values_z)[:n_z // 2].tolist()
    }
}

# URL de la API
url = 'http://localhost:9000/api/spectral'

# Enviar la solicitud POST con la estructura JSON en el cuerpo
response = requests.post(url, json=spectral_data)

# Verificar la respuesta
if response.status_code == 201:
    print('Datos enviados exitosamente')
else:
    print(f'Error al enviar datos: {response.status_code}, {response.text}')
