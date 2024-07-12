import threading
import time
import random


# Algoritmo de Dijkstra-Scholten en Python:

class Process:
    def __init__(self, process_id, neighbors):
        self.process_id = process_id
        self.neighbors = neighbors
        self.parent = None
        self.children = set()
        self.active = True

    def send_message(self, recipient):
        recipient.receive_message(self, self.process_id)

    def receive_message(self, sender, sender_id):
        if self.parent is None:
            self.parent = sender
        self.children.add(sender_id)
        self.process_task()

    def process_task(self):
        # Simulate task processing
        self.active = False
        self.check_termination()

    def check_termination(self):
        if not self.active and not self.children:
            if self.parent:
                self.parent.receive_termination(self.process_id)

    def receive_termination(self, child_id):
        self.children.remove(child_id)
        self.check_termination()


# Clase que implementa el algoritmo de Ricart-Agrawala
class RicartAgrawala:
    def __init__(self, pid, total_processes):
        self.pid = pid  # Identificador del proceso
        self.clock = 0  # Reloj lógico del proceso
        self.total_processes = total_processes  # Número total de procesos
        self.request_queue = []  # Cola de solicitudes
        self.deferred_replies = []  # Respuestas diferidas
        self.requesting_cs = False  # Indicador de solicitud de sección crítica
        self.lock = threading.Lock()  # Mutex para sincronización

    # Solicitar acceso a un recurso
    def request_resource(self):
        with self.lock:
            self.clock += 1  # Incrementar el reloj lógico
            self.requesting_cs = True  # Indicar que se está solicitando la sección crítica
            request = (self.clock, self.pid)  # Crear la solicitud
            self.request_queue.append(request)  # Añadir la solicitud a la cola
            self.request_queue.sort()  # Ordenar la cola de solicitudes
            return request

    # Recibir una solicitud de otro proceso
    def receive_request(self, timestamp, pid):
        with self.lock:
            self.clock = max(self.clock, timestamp) + 1  # Actualizar el reloj lógico
            request = (timestamp, pid)  # Crear la solicitud recibida
            self.request_queue.append(request)  # Añadir la solicitud a la cola
            self.request_queue.sort()  # Ordenar la cola de solicitudes
            # Verificar si se debe diferir la respuesta
            if self.requesting_cs and (timestamp, pid) < (self.clock, self.pid):
                self.deferred_replies.append(pid)
            else:
                return True
        return False

    # Recibir una respuesta de otro proceso
    def receive_reply(self, pid):
        with self.lock:
            self.deferred_replies.remove(pid)  # Eliminar el PID de las respuestas diferidas

    # Liberar el recurso
    def release_resource(self):
        with self.lock:
            self.request_queue.pop(0)  # Eliminar la primera solicitud de la cola
            self.requesting_cs = False  # Indicar que ya no se está solicitando la sección crítica
            replies = self.deferred_replies[:]  # Copiar las respuestas diferidas
            self.deferred_replies.clear()  # Limpiar la lista de respuestas diferidas
        return replies

    # Verificar si el proceso puede entrar en la sección crítica
    def can_enter_critical_section(self):
        with self.lock:
            if self.request_queue:
                return self.request_queue[0][1] == self.pid  # Verificar si la primera solicitud es del proceso actual
            return False

# Función para simular el comportamiento de un proceso
def simulate_process(process):
    while True:
        time.sleep(random.uniform(0.5, 2))  # Esperar un tiempo aleatorio antes de solicitar el recurso
        request = process.request_resource()
        print(f"Process {process.pid} requested resource at time {request[0]}")

        # Simular la recepción de solicitudes de otros procesos
        for i in range(process.total_processes):
            if i != process.pid:
                process.receive_request(random.randint(0, 10), i)

        # Esperar hasta que el proceso pueda entrar en la sección crítica
        while not process.can_enter_critical_section():
            time.sleep(0.1)
        
        print(f"Process {process.pid} entering critical section at time {process.clock}")
        time.sleep(random.uniform(0.5, 1.5))  # Simular el tiempo en la sección crítica
        print(f"Process {process.pid} leaving critical section at time {process.clock}")
        deferred_replies = process.release_resource()

        # Simular el envío de respuestas a los procesos diferidos
        for pid in deferred_replies:
            print(f"Process {process.pid} sending reply to process {pid}")




# Ejemplo de uso
processes = [Process(i, []) for i in range(5)]
for process in processes:
    process.neighbors = [p for p in processes if p != process]

# Iniciar la detección de terminación
initiator = processes[0]
initiator.send_message(processes[1])
