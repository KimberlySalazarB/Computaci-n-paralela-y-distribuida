from collections import defaultdict  # Importa la clase defaultdict para crear diccionarios con valores predeterminados
import multiprocessing as mp  # Importa el módulo multiprocessing para la programación concurrente
import sys  # Importa el módulo sys para manipular la configuración del sistema
import time  # Importa el módulo time para medir el tiempo de ejecución
from time import sleep  # Importa la función sleep del módulo time para pausar la ejecución

def report_progress(map_returns, tag, callback):
    done = 0  # Inicializa el contador de tareas completadas
    num_jobs = len(map_returns)  # Obtiene el número total de tareas
    while num_jobs > done:  # Mientras haya tareas pendientes
        done = 0  # Reinicia el contador de tareas completadas
        for ret in map_returns:  # Itera sobre los resultados del mapeo
            if ret.ready():  # Si la tarea ha finalizado
                done += 1  # Incrementa el contador de tareas completadas
        sleep(0.5)  # Espera un corto periodo de tiempo antes de volver a verificar
        if callback:  # Si se proporciona una función de callback
            callback(tag, done, num_jobs - done)  # Llama a la función de callback con el progreso actual

def chunk0(my_list, chunk_size):
    for i in range(0, len(my_list), chunk_size):  # Itera sobre la lista en incrementos del tamaño del fragmento
        yield my_list[i:i + chunk_size]  # Produce fragmentos de la lista de tamaño especificado

def chunk(my_iter, chunk_size):
    chunk_list = []  # Inicializa una lista para contener los elementos del fragmento
    for elem in my_iter:  # Itera sobre los elementos del iterable
        chunk_list.append(elem)  # Agrega el elemento al fragmento
        if len(chunk_list) == chunk_size:  # Si el fragmento alcanza el tamaño especificado
            yield chunk_list  # Produce el fragmento
            chunk_list = []  # Reinicia el fragmento
    if len(chunk_list) > 0:  # Si quedan elementos en el fragmento
        yield chunk_list  # Produce el fragmento

def chunk_runner(fun, data):
    ret = []  # Inicializa una lista para almacenar los resultados
    for datum in data:  # Itera sobre los datos del fragmento
        ret.append(fun(datum))  # Ejecuta la función en cada dato y agrega el resultado a la lista
    return ret  # Devuelve la lista de resultados

def chunked_async_map(pool, mapper, data, chunk_size):
    async_returns = []  # Inicializa una lista para almacenar los resultados asincrónicos
    for data_part in chunk(data, chunk_size):  # Itera sobre los fragmentos de datos
        async_returns.append(pool.apply_async(chunk_runner, (mapper, data_part)))  # Aplica la función de manera asincrónica a cada fragmento
    return async_returns  # Devuelve los resultados asincrónicos

def map_reduce(pool, my_input, mapper, reducer, chunk_size, callback=None):
    map_returns = chunked_async_map(pool, mapper, my_input, chunk_size)  # Realiza el mapeo en paralelo
    report_progress(map_returns, 'map', callback)  # Informa sobre el progreso del mapeo
    map_results = []  # Inicializa una lista para almacenar los resultados del mapeo
    for ret in map_returns:  # Itera sobre los resultados del mapeo
        map_results.extend(ret.get())  # Obtiene los resultados y los agrega a la lista
    distributor = defaultdict(list)  # Crea un diccionario con valores predeterminados como listas
    for key, value in map_results:  # Itera sobre los resultados del mapeo
        distributor[key].append(value)  # Agrupa los valores por clave
    returns = chunked_async_map(pool, reducer, distributor.items(), chunk_size)  # Realiza la reducción en paralelo
    report_progress(returns, 'reduce', callback)  # Informa sobre el progreso de la reducción
    results = []  # Inicializa una lista para almacenar los resultados finales
    for ret in returns:  # Itera sobre los resultados de la reducción
        results.extend(ret.get())  # Obtiene los resultados y los agrega a la lista
    return results  # Devuelve los resultados finales

def emitter(word):
    return word, 1  # Emite cada palabra con un conteo inicial de 1

def counter(emitted):
    return emitted[0], sum(emitted[1])  # Suma los conteos de cada palabra

def reporter(tag, done, not_done):
    print(f'Operacion {tag}: {done}/{done+not_done}')  # Imprime el progreso de la operación

def run_map_reduce(words, chunk_size):
    pool = mp.Pool(4)  # Crea un grupo de procesos
    start_time = time.time()  # Obtiene el tiempo de inicio
    counts = map_reduce(pool, words, emitter, counter, chunk_size, reporter)  # Ejecuta el proceso MapReduce
    pool.close()  # Cierra el grupo de procesos
    pool.join()  # Espera a que todos los procesos terminen
    end_time = time.time()  # Obtiene el tiempo de finalización
    duration = end_time - start_time  # Calcula la duración del proceso
    return duration  # Devuelve la duración

if __name__ == '__main__':
    file_path = 'C:/Users/Asus/Documents/Computación Paralela/Computaci-n-paralela-y-distribuida/Evaluación7-C8286/PARTE4/Ejercicio1/tempestad.txt'
    words = [word
             for word in map(lambda x: x.strip().rstrip(),
                             ' '.join(open(file_path, 'rt', encoding='utf-8').readlines()).split(' '))
             if word != '' ]  # Lee las palabras de un archivo de texto y las almacena en una lista

    chunk_sizes = [1, 10, 100, 1000, 10000]  # Tamaños de fragmentación a probar
    results = []  # Inicializa una lista para almacenar los resultados

    for size in chunk_sizes:  # Itera sobre los tamaños de fragmentación
        duration = run_map_reduce(words, size)  # Ejecuta el proceso MapReduce con el tamaño de fragmentación actual
        results.append((size, duration))  # Agrega el tamaño de fragmentación y la duración a la lista de resultados

    print("Tam fragmentacion | Duracion")  # Imprime la cabecera de la tabla de resultados
    print("-" * 20)  # Imprime una línea divisoria
    for size, duration in results:  # Itera sobre los resultados
        print(f"{size:<10} | {duration:.2f} segundos")