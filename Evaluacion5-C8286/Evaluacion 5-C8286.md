**EJERCICIO 1:** Sistema de procesamiento de imágenes en tiempo real

import os![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.001.png)
´´´
from PIL import Image, ImageFilter

import time

from concurrent.futures import ThreadPoolExecutor from functools import wraps

def convert\_to\_grayscale(image):

"""Convierte la imagen a escala de grises.""" return [image.convert('L')]

def apply\_edge\_detection(image):

"""Aplica detección de bordes a la imagen.""" return [image.filter(ImageFilter.FIND\_EDGES)]

def time\_it(func):

"""Decorador que mide el tiempo de ejecución de una función.""" @wraps(func)

def wrapper(\*args, \*\*kwargs):

start = time.time()

result = func(\*args, \*\*kwargs)

end = time.time()

print(f"{func.\_\_name\_\_} took {end - start:.2f} seconds to

run.")

return result return wrapper

def parallelize\_image\_processing(function):

"""Decorador que paraleliza el procesamiento de imágenes.""" @wraps(function)

def wrapper(images):

with ThreadPoolExecutor(max\_workers=5) as executor:

results = list(executor.map(function, images)) return results

return wrapper

import asyncio @time\_it

def process\_images(images):

"""Procesa una lista de imágenes aplicando las funciones de procesamiento."""

processed\_images = [convert\_to\_grayscale(img)[0] for img in images]

processed\_images = [apply\_edge\_detection(img)[0] for img in processed\_images]

return processed\_images

async def main():

- Simulando la carga de imágenes

#images = [Image.open(f'cat\_{i}.jpg') for i in range(10)] # Asegúrate de tener imágenes disponibles

#processed\_images = process\_images(images)

- Simulando la carga de imágenes

folder\_path = r'C:\Users\Asus\Downloads\archive\data\cats' images = []

for i in range(202):

image\_path = os.path.join(folder\_path, f'cat.{i+1}.jpg') try:

image = Image.open(image\_path) images.append([image])

except FileNotFoundError:

print(f"No se encontró la imagen {image\_path}") processed\_images = process\_images(images)

- Guardar

output = r'C:\Users\Asus\Downloads\archive\data\cats\_pro'

for i, processed\_image\_list in enumerate(processed\_images): processed\_image = processed\_image\_list[0] processed\_image.save(os.path.join(output,

f'cats\_pro.{i+1}.jpg'))

- Aquí podrías guardar las imágenes procesadas o enviarlas a otro

servicio

if \_\_name\_\_ == "\_\_main\_\_":

asyncio.run(main())

´´´

Resultado:

![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.003.png)

Dataset Cats de 202 imagenes= <https://www.kaggle.com/datasets/pavansanagapati/images-dataset/data>

![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.004.png) ![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.005.png)

**EJERCICIO 2:**Simulación de sistema de reservas con alta concurrencia

**def add\_reservation(reservations, reservation):![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.006.png)**

**"""Agrega una nueva reserva a la lista de reservas de manera inmutable."""**

**return reservations + [reservation]**

**def cancel\_reservation(reservations, reservation\_id):**

**"""Cancela una reserva por ID, inmutablemente."""**

**return [res for res in reservations if res['id'] != reservation\_id]**

**def update\_reservation(reservations, reservation\_id, new\_details):**

**"""Actualiza una reserva por ID, inmutablemente."""**

**return [res if res['id'] != reservation\_id else {\*\*res, \*\*new\_details} for res in reservations]**

**from concurrent.futures import ThreadPoolExecutor**

**import copy**

**import time**

**import random![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.007.png)**

**def process\_booking\_requests(requests):**

**"""Procesa una lista de solicitudes de reserva concurrentemente.""" with ThreadPoolExecutor(max\_workers=5) as executor:**

**results = list(executor.map(handle\_request, requests))**

**return results**

**def handle\_request(request):**

**"""Maneja una solicitud individual simulando cierta lógica y tiempo de procesamiento."""**

- **Simulación de procesamiento: modificar según la lógica de negocio time.sleep(random.uniform(0.1, 0.5)) # Simular tiempo de**

**procesamiento**

**return f"Processed request {request['id']} with status: {request['status']}"**

**import asyncio**

**async def manage\_reservations(requests):**

**"""Gestiona reservas asincrónicamente."""**

**loop = asyncio.get\_running\_loop()**

**future = loop.run\_in\_executor(None, process\_booking\_requests, requests)**

**result = await future**

**print("resultado:",result)**

**async def simulate\_requests():**

**"""Simula la llegada de solicitudes de reserva."""**

**requests = [{'id': i, 'status': 'new'} for i in range(100)] # Simular 10 solicitudes**

**await manage\_reservations(requests)**

**if \_\_name\_\_ == "\_\_main\_\_":**

**asyncio.run(simulate\_requests())**

**RESULTADO:** Con 100 solicitudes

![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.008.jpeg)

Ejercicio 4: Sistema de análisis de sentimiento en tiempo real para redes sociales

import re![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.009.png)

import nltk

nltk.download('punkt')

from nltk.corpus import stopwords

from nltk.tokenize import word\_tokenize

stop\_words = set(stopwords.words('english'))

def clean\_text(text):

"""Limpia el texto eliminando caracteres especiales y convirtiéndolo a minúsculas."""

text = re.sub(r'\W', ' ', text)

text = text.lower()

return text

def remove\_stopwords(text):

"""Elimina las stopwords de un texto."""

words = word\_tokenize(text)

filtered\_words = [word for word in words if word not in stop\_words] return ' '.join(filtered\_words)

def preprocess\_text(text):

"""Combina todas las operaciones de preprocesamiento de texto.""" ![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.010.png)text = clean\_text(text)

text = remove\_stopwords(text)

return text

from textblob import TextBlob

def analyze\_sentiment(text):

"""Analiza el sentimiento de un texto dado y devuelve el resultado."""

analysis = TextBlob(text)

return analysis.sentiment

from concurrent.futures import ThreadPoolExecutor

def analyze\_texts\_concurrently(texts):

"""Analiza una lista de textos concurrentemente."""

with ThreadPoolExecutor(max\_workers=10) as executor:

results = list(executor.map(preprocess\_and\_analyze, texts)) return results

def preprocess\_and\_analyze(text):

"""Preprocesa y analiza el sentimiento de un texto.""" preprocessed\_text = preprocess\_text(text)

sentiment = analyze\_sentiment(preprocessed\_text) return sentiment

import asyncio

async def collect\_and\_process\_data(stream\_data):

"""Asíncronamente recolecta y procesa datos de un flujo."""

processed\_data = await asyncio.get\_event\_loop().run\_in\_executor(None, analyze\_texts\_concurrently, stream\_data)

print("Sentiment Analysis Results:", processed\_data)

async def simulate\_streaming\_data():

"""Simula la llegada de datos de texto de un flujo en tiempo real."""

sample\_data = [

"This video is amazing! I love it.",

"I'm fed up with this. I can't believe what's happening.", "Wow! I never expected to see something like this.", "This is so sad. I can't help but feel bad for them.", "Sending love and support from here. Stay strong!", "Incredible! You really left me speechless."

]![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.011.png)

await collect\_and\_process\_data(sample\_data)

if \_\_name\_\_ == "\_\_main\_\_":

asyncio.run(simulate\_streaming\_data())

**RESULTADOS:** De 6 comentarios de un video.

Sentiment Analysis Results: [Sentiment(polarity=0.55, subjectivity=0.75), Sentiment(polarity=0.0, subjectivity=0.0), Sentiment(polarity=0.07500000000000001, subjectivity=0.7), Sentiment(polarity=-0.5999999999999999, subjectivity=0.8333333333333333), Sentiment(polarity=0.4666666666666667, subjectivity=0.6666666666666666), Sentiment(polarity=0.45, subjectivity=0.45)]

Ejercicio 5: Plataforma de análisis de datos genómicos distribuidos

def filter\_variants(variants, min\_depth=10, min\_quality=20):![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.012.png)

"""Filtra variantes genéticas basadas en profundidad y calidad."""

return [variant for variant in variants if variant['depth'] >= min\_depth and variant['quality'] >= min\_quality]

def calculate\_allele\_frequencies(variants):

"""Calcula las frecuencias alélicas de un conjunto de variantes genéticas."""

allele\_counts = {}

for variant in variants:

alleles = variant['alleles']

for allele in alleles:

if allele in allele\_counts:

allele\_counts[allele] += 1

else:

allele\_counts[allele] = 1

total\_alleles = sum(allele\_counts.values())

return {allele: count / total\_alleles for allele, count in allele\_counts.items()}

from multiprocessing import Pool

def process\_genomic\_data(data):

"""Procesa datos genómicos en paralelo utilizando múltiples procesos."""

with Pool(processes=4) as pool:

results = pool.map(process\_sample, data)

return results![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.013.png)

def process\_sample(sample):

"""Procesa un único conjunto de datos genómicos."""

filtered\_variants = filter\_variants(sample['variants'])

allele\_frequencies = calculate\_allele\_frequencies(filtered\_variants)

return {'sample\_id': sample['id'], 'allele\_frequencies': allele\_frequencies}

import asyncio

async def load\_genomic\_data(file\_path):

"""Carga datos genómicos de forma asíncrona."""

- Simulación: en un caso real, se leerían los datos de un archivo return [

{'id': 'sample1', 'variants': [{'depth': 15, 'quality': 30, 'alleles': ['A', 'T']}, {'depth': 20, 'quality': 25, 'alleles': ['G', 'C']}]},

{'id': 'sample2', 'variants': [{'depth': 12, 'quality': 22, 'alleles': ['T', 'T']}, {'depth': 18, 'quality': 28, 'alleles': ['A', 'C']}]},

{'id': 'sample3', 'variants': [{'depth': 18, 'quality': 26, 'alleles': ['A', 'T']}, {'depth': 22, 'quality': 35, 'alleles': ['C', 'G']}]},

{'id': 'sample4', 'variants': [{'depth': 14, 'quality': 21, 'alleles': ['G', 'G']}, {'depth': 16, 'quality': 28, 'alleles': ['T', 'C']}]},

{'id': 'sample5', 'variants': [{'depth': 20, 'quality': 30, 'alleles': ['A', 'C']}, {'depth': 25, 'quality': 28, 'alleles': ['G', 'T']}]},

{'id': 'sample6', 'variants': [{'depth': 16, 'quality': 24, 'alleles': ['G', 'A']}, {'depth': 21, 'quality': 32, 'alleles': ['T', 'C']}]},

{'id': 'sample7', 'variants': [{'depth': 18, 'quality': 26, 'alleles': ['T', 'T']}, {'depth': 22, 'quality': 35, 'alleles': ['C', 'C']}]},

{'id': 'sample8', 'variants': [{'depth': 14, 'quality': 21, 'alleles': ['C', 'A']}, {'depth': 16, 'quality': 28, 'alleles': ['T', 'G']}]},

{'id': 'sample9', 'variants': [{'depth': 20, 'quality': 30, 'alleles': ['G', 'T']}, {'depth': 25, 'quality': 28, 'alleles': ['A', 'C']}]},

{'id': 'sample10', 'variants': [{'depth': 16, 'quality': 24, ![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.014.png)'alleles': ['T', 'T']}, {'depth': 21, 'quality': 32, 'alleles': ['C', 'A']}]},

{'id': 'sample11', 'variants': [{'depth': 18, 'quality': 26, 'alleles': ['A', 'C']}, {'depth': 22, 'quality': 35, 'alleles': ['T', 'G']}]},

{'id': 'sample12', 'variants': [{'depth': 14, 'quality': 21, 'alleles': ['G', 'A']}, {'depth': 16, 'quality': 28, 'alleles': ['C', 'T']}]}

]

async def analyze\_genomic\_data(file\_path):

"""Analiza datos genómicos utilizando funciones asincrónicas y paralelismo."""

data = await load\_genomic\_data(file\_path)

results = await asyncio.get\_event\_loop().run\_in\_executor(None, process\_genomic\_data, data)

for result in results:

print(result)

if \_\_name\_\_ == "\_\_main\_\_":

asyncio.run(analyze\_genomic\_data('path\_to\_genomic\_data.txt'))

**Resultados de 12 datos genómicos:**

{'sample\_id': 'sample1', 'allele\_frequencies': {'A': 0.25, 'T': 0.25, 'G': 0.25, 'C': 0.25}} {'sample\_id': 'sample2', 'allele\_frequencies': {'T': 0.5, 'A': 0.25, 'C': 0.25}} {'sample\_id': 'sample3', 'allele\_frequencies': {'A': 0.25, 'T': 0.25, 'C': 0.25, 'G': 0.25}} {'sample\_id': 'sample4', 'allele\_frequencies': {'G': 0.5, 'T': 0.25, 'C': 0.25}} {'sample\_id': 'sample5', 'allele\_frequencies': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}} {'sample\_id': 'sample6', 'allele\_frequencies': {'G': 0.25, 'A': 0.25, 'T': 0.25, 'C': 0.25}} {'sample\_id': 'sample7', 'allele\_frequencies': {'T': 0.5, 'C': 0.5}}

{'sample\_id': 'sample8', 'allele\_frequencies': {'C': 0.25, 'A': 0.25, 'T': 0.25, 'G': 0.25}} {'sample\_id': 'sample9', 'allele\_frequencies': {'G': 0.25, 'T': 0.25, 'A': 0.25, 'C': 0.25}} {'sample\_id': 'sample10', 'allele\_frequencies': {'T': 0.5, 'C': 0.25, 'A': 0.25}} {'sample\_id': 'sample11', 'allele\_frequencies': {'A': 0.25, 'C': 0.25, 'T': 0.25, 'G': 0.25}} {'sample\_id': 'sample12', 'allele\_frequencies': {'G': 0.25, 'A': 0.25, 'C': 0.25, 'T': 0.25}}

Ejercicio 6: Simulador de mercados financieros en tiempo real

def calculate\_moving\_average(prices, window\_size=14):![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.015.png)

"""Calcula la media móvil simple de los precios."""

if len(prices) < window\_size:

return None # No hay suficientes datos para calcular la media móvil

return sum(prices[-window\_size:]) / window\_size

def calculate\_rsi(prices, periods=8):

"""Calcula el índice de fuerza relativa (RSI) para una lista de precios."""

if len(prices) < periods:

return None # No hay suficientes datos para calcular el RSI

gains = [max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices))]

losses = [max(0, prices[i - 1] - prices[i]) for i in range(1, len(prices))]

average\_gain = sum(gains[-periods:]) / periods average\_loss = sum(losses[-periods:]) / periods

if average\_loss == 0:

return 100 # Evitar división por cero rs = average\_gain / average\_loss

rsi = 100 - (100 / (1 + rs))

return rsi

from concurrent.futures import ThreadPoolExecutor

def parallel\_analyze\_data(stock\_data):

"""Analiza datos bursátiles en paralelo."""

with ThreadPoolExecutor(max\_workers=10) as executor:

results = list(executor.map(analyze\_stock, stock\_data)) return results

def analyze\_stock(data):

"""Analiza los datos de un solo stock."""

moving\_average = calculate\_moving\_average(data['prices'])

rsi = calculate\_rsi(data['prices'])

return {'stock': data['stock'], 'moving\_average': moving\_average, 'RSI': rsi}

import asyncio

async def stream\_stock\_data():![](Aspose.Words.8290ba66-b50f-44fa-83c8-bc17d4ca0736.016.png)

"""Simula la recepción de datos bursátiles en tiempo real.""" example\_data = [

{'stock': 'AAPL', 'prices': [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164]},

{'stock': 'GOOGL', 'prices': [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134]},

{'stock': 'MSFT', 'prices': [250, 251, 249, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263]},

{'stock': 'AMZN', 'prices': [330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358]},

{'stock': 'TSLA', 'prices': [600, 605, 610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670]},

{'stock': 'NFLX', 'prices': [550, 552, 554, 556, 558, 560, 562, 564, 566, 568, 570, 572, 574, 576, 578]},

{'stock': 'FB', 'prices': [320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334]},

{'stock': 'NVDA', 'prices': [700, 702, 704, 706, 708, 710, 712, 714, 716, 718, 720, 722, 724, 726, 728]},

{'stock': 'V', 'prices': [220, 221, 222, 223, 224, 225, 226,

227, 228, 229, 230, 231, 232, 233, 234]},

{'stock': 'JPM', 'prices': [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164]}

]

while True:

await asyncio.sleep(1) # Simular la recepción de datos cada segundo

processed\_data = await asyncio.get\_event\_loop().run\_in\_executor(None, parallel\_analyze\_data, example\_data)

print("Processed Data:", processed\_data)

if \_\_name\_\_ == "\_\_main\_\_":

asyncio.run(stream\_stock\_data())

**Resultado con 10 datos bursátiles:**

Processed Data: [{'stock': 'AAPL', 'moving\_average': 157.5, 'RSI': 100}, {'stock': 'GOOGL', 'moving\_average': 127.5, 'RSI': 100}, {'stock': 'MSFT', 'moving\_average': 256.42857142857144, 'RSI': 100}, {'stock': 'AMZN', 'moving\_average': 345.0, 'RSI': 100}, {'stock': 'TSLA', 'moving\_average': 637.5, 'RSI': 100}, {'stock': 'NFLX', 'moving\_average': 565.0, 'RSI': 100}, {'stock': 'FB', 'moving\_average': 327.5, 'RSI': 100}, {'stock': 'NVDA', 'moving\_average': 715.0, 'RSI': 100}, {'stock': 'V', 'moving\_average': 227.5, 'RSI': 100}, {'stock': 'JPM', 'moving\_average': 157.5, 'RSI': 100}]
