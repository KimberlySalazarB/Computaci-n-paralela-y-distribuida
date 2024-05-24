import concurrent.futures 
from collections import defaultdict
import time
def emiter(word):
    return word, 1


def counter(emitted):
    return emitted[0], sum(emitted[1])

def map_reduce_ultra_naive(my_input, mapper, reducer):
    map_results = map(mapper, my_input)

    distributor = defaultdict(list)
    for key, value in map_results:
        distributor[key].append(value)

    return map(reducer, distributor.items())

def map_reduce_ultra_naive_parallel(my_input, mapper, reducer):
    with concurrent.futures.ThreadPoolExecutor() as executor:
         map_results = list(executor.map(mapper, my_input))
         distributor = defaultdict(list)
         for key, value in map_results:
            distributor[key].append(value)
    
         reduce=list(executor.map(reducer, distributor.items()))
    return reduce

def main():
    words = 'Python es lo mejor Python rocks'.split(' ')
    

    start_time = time.time()
    a = list(map_reduce_ultra_naive_parallel(words, emiter, counter))
    sync_duration = time.time() - start_time
    print("Paralelo:",a)
    print(f" En {sync_duration:.4f} segundos")
    
    start_time1 = time.time()
    a = list(map_reduce_ultra_naive(words, emiter, counter))
    sync_duration1 = time.time() - start_time1
    print("sincronico:",a)
    print(f" En {sync_duration1:.4f} segundos")

if __name__ == "__main__":
    main()
