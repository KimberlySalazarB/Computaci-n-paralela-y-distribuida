import threading
import time
import random
#from mpi4py import MPI



#Simulacion de latencia de red

#comm = MPI.COMM_WORLD
#rank = comm.Get_rank()

#if rank == 0:
#    start_time = time.time()
#    comm.send('ping', dest=1, tag=0)
#    comm.recv(source=1, tag=1)
#    end_time = time.time()
#    print(f"Latencia: {end_time - start_time} segundos")

#elif rank == 1:
#    msg = comm.recv(source=0, tag=0)
#    comm.send('pong', dest=0, tag=1)



#Algoritmo de consenso Raft gestionar consistencia


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = "follower"
        self.votes = 0

    def start_election(self):
        self.state = "candidate"
        self.votes = 1  # vote for self
        print(f"Nodo {self.node_id} inicia una eleccion")

    def receive_vote(self):
        self.votes += 1
        print(f"Nodo {self.node_id} recive un voto")

nodes = [Node(i) for i in range(5)]
leader_elected = threading.Event()

def run_node(node):
    while not leader_elected.is_set():
        if node.state == "follower" and random.random() < 0.05:
            node.start_election()
            for peer in nodes:
                if peer != node:
                    peer.receive_vote()
            if node.votes > len(nodes) / 2:
                node.state = "leader"
                leader_elected.set()
                print(f"Nodo {node.node_id} es elegido como lider")



#Simulaciòn configuraciones de particiones y curaciones en la red

# Configuración inicial
consistency_level = "CP"  # Modo de consistencia: CP, AP, o CA

# Variables de estado
data_store = {}  # Almacenamiento de datos compartido

# Función para simular la escritura de un nodo
def write_data(node_id, key, value):
    global data_store
    # Simulamos un tiempo de escritura
    time.sleep(random.uniform(0.5, 1.5))
    # Escribir en el almacenamiento
    data_store[key] = value
    print(f"Nodo {node_id} escribió {value} en clave {key}")

# Función para simular la lectura de un nodo
def read_data(node_id, key):
    global data_store
    # Simulamos un tiempo de lectura
    time.sleep(random.uniform(0.5, 1.5))
    # Leer del almacenamiento
    value = data_store.get(key, None)
    print(f"Nodo {node_id} leyó {value} de clave {key}")

# Función para simular caida de red y  la partición
def simulate_network_failure():
    time.sleep(random.uniform(2, 5))
    print("¡Se ha producido una partición de red!")

# Función para simular la curaciones de la red
def simular_prepa_red():
    time.sleep(random.uniform(2, 5))
    print("La red se ha recuperado.")

# Función para ejecutar un nodo simulado
def run_node(node_id):
    while True:
        key = random.choice(['A', 'B', 'C'])  # Claves aleatorias
        if random.random() < 0.6:  # Probabilidad de escritura
            write_data(node_id, key, random.randint(1, 100))
        else:  # Probabilidad de lectura
            read_data(node_id, key)
        
        if consistency_level == "CP" or consistency_level == "CA":
            simulate_network_failure()
            simular_prepa_red()

        time.sleep(random.uniform(0.5, 1))

# Función principal para iniciar los nodos
def start_simulation(num_nodes):
    threads = []
    for i in range(num_nodes):
        thread = threading.Thread(target=run_node, args=(i+1,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# Ejecutar la simulación
if __name__ == "__main__":
    num_nodes = 3  # Número de nodos en el sistema distribuido
    start_simulation(num_nodes)

    threads = [threading.Thread(target=run_node, args=(node,)) for node in nodes]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
        


