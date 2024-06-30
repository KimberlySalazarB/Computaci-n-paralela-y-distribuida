## Instrucciones para Configurar el Entorno

Este documento proporciona instrucciones detalladas para configurar el entorno necesario para implementar y ejecutar algoritmos de machine learning utilizando Dask y PySpark, así como PyTorch para la visión computacional.

### Requisitos del Sistema

- **Memoria RAM**: Mínimo 8 GB (Recomendado 16 GB o más)
- **Espacio en Disco**: Mínimo 10 GB de espacio libre
- **Python**: Versión 3.7 o superior

### Instalación de Python y Dependencias

1. **Instalar Python**:
   - [Descargar e instalar Python](https://www.python.org/downloads/)
   - Asegúrate de que Python y `pip` estén correctamente instalados:
     ```
     python --version
     pip --version
     ```

2. **Crear y Activar un Entorno Virtual**:
   ```
   python -m venv ml-env
   source ml-env/bin/activate  # En Windows: ml-env\Scripts\activate
   ```

3. **Instalar Dependencias**:
     ```
     pip install scikit-learn
     pip install torch
     pip install torchvision
     pip install pandas
     pip install numpy
     pip install matplotlib
     ```

### Configuración de Dask

1. **Instalar Dask y Dask-ML**:
   ```
   pip install dask[complete] dask-ml
   ```


2. **Iniciar el Clúster de Dask**:
   ```python
   from dask.distributed import Client
   client = Client()
   ```

### Configuración de PySpark

1. **Instalar PySpark**:
   ```
   pip install pyspark
   ```

2. **Iniciar PySpark**:
   ```python
   from pyspark.sql import SparkSession
   spark = SparkSession.builder \
       .appName("ML Project") \
       .getOrCreate()
   ```

### Instalación Adicional de Bibliotecas Necesarias

- **Bibliotecas de Machine Learning y Otras Utilidades**:
  ```
  pip install scikit-learn xgboost psutil
  ```
- **Instalar PyTorch**
  ```
   pip install torch torchvision
   ```
### Problemas Comunes y Soluciones

- **Problema**: Error al instalar `dask-ml` o `pyspark`.
  - **Solución**: Asegúrate de tener `pip` actualizado:
    ```
    pip install --upgrade pip
    ```
### Para ver el dashboard de Dask desde colab 
 ```
Obten tu AUTHTOKEN desde la pagina ngrok
# Configurar ngrok con el authtoken: para poder observar el dashboard
from pyngrok import ngrok
ngrok.set_auth_token("AUTHTOKEN")

Inicializas el cliente de dask

Luego:

# Obtener la URL del Dashboard
dashboard_link = client.dashboard_link
print("Dashboard link:", dashboard_link)

from pyngrok import ngrok

# Lista de tuneles
#ngrok.get_tunnels()

# Cerra si hay algun tunnel abierto para crear uno nuevo
#ngrok.disconnect(ngrok_tunnel.public_url) # Replace with the actual public URL if needed

# Conectar ngrok al puerto del dashboard
ngrok_tunnel = ngrok.connect(addr="127.0.0.1:8787")
print("ngrok tunnel:", ngrok_tunnel.public_url)
```
### Recursos Adicionales

- [Documentación de Dask](https://dask.pydata.org/en/latest/install.html)
- [Documentación de PySpark](https://spark.apache.org/docs/latest/api/python/index.html)
- [Guía de PyTorch](https://pytorch.org/get-started/locally/#windows-python)

