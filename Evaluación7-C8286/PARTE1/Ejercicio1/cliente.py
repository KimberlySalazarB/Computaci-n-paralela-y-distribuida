import dill as pickle
import socket
from time import sleep

def numero_list(numbers):
    conn = None
    try:
        conn = socket.create_connection(('127.0.0.1', 1936))
        conn.send(b'\x00')  
        numbers_data = pickle.dumps(numbers)
        conn.send(len(numbers_data).to_bytes(4, 'little'))
        conn.send(numbers_data)
        job_id = int.from_bytes(conn.recv(4), 'little')
        print(f'Enviada lista de números al servidor. job_id: {job_id}')
        return job_id
    finally:
        if conn:
            conn.close()

def resultado(job_id):
    result = None
    while result is None:
        try:
            conn = socket.create_connection(('127.0.0.1', 1936))
            conn.send(b'\x01')
            conn.send(job_id.to_bytes(4, 'little'))
            result_size = int.from_bytes(conn.recv(4), 'little')
            result = pickle.loads(conn.recv(result_size))
        finally:
            if conn:
                conn.close()
        sleep(1)
    print(f'El resultado de la suma es: {result}')

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]  
    job_id = numero_list(numbers)
    if job_id:
        resultado(job_id)