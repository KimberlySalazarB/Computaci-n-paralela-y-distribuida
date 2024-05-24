#### Ejercicio 1: Modificar el número de procesos
Modifica el código para cambiar dinámicamente el número de procesos en el pool (mp.Pool()). Realiza pruebas con diferentes configuraciones (p. ej., 1, 2, 4, 8 procesos) y mide cómo afecta al tiempo de ejecución del proceso de MapReduce.
Resultados esperados: Documentar cómo el incremento en el número de procesos afecta la eficiencia del procesamiento, identificando el punto de saturación donde más procesos no resultan en mejoras significativas.

##### Con 1 proceso
Operacion map: 9/16794
Operacion map: 4844/16794
Operacion map: 10437/16794
Operacion map: 15386/16794
Operacion map: 16794/16794
Operacion reduce: 12/5576
Operacion reduce: 4334/5576
Operacion reduce: 5576/5576
Operacion map: 0/1680
Operacion map: 972/1680
Operacion map: 1680/1680
Operacion reduce: 0/558
Operacion reduce: 558/558
Operacion map: 0/168
Operacion map: 168/168
Operacion reduce: 0/56
Operacion reduce: 56/56
Operacion map: 0/17
Operacion map: 17/17
Operacion reduce: 0/6
Operacion reduce: 6/6
Operacion map: 0/2
Operacion map: 2/2
Operacion reduce: 0/1
Operacion reduce: 1/1
Tam fragmentacion | Duracion
--------------------
1          | 4.77 segundos
10         | 2.68 segundos
100        | 2.10 segundos
1000       | 2.08 segundos
10000      | 2.07 segundos

##### Con 2 procesos 

Operacion map: 14/16794
Operacion map: 4523/16794
Operacion map: 8943/16794
Operacion map: 13357/16794
Operacion map: 16794/16794
Operacion reduce: 8/5576
Operacion reduce: 5043/5576
Operacion reduce: 5576/5576
Operacion map: 0/1680
Operacion map: 1111/1680
Operacion map: 1680/1680
Operacion reduce: 0/558
Operacion reduce: 558/558
Operacion map: 0/168
Operacion map: 168/168
Operacion reduce: 0/56
Operacion reduce: 56/56
Operacion map: 0/17
Operacion map: 17/17
Operacion reduce: 0/6
Operacion reduce: 6/6
Operacion map: 0/2
Operacion map: 2/2
Operacion reduce: 0/1
Operacion reduce: 1/1
Tam fragmentacion | Duracion
--------------------
1          | 4.77 segundos
10         | 2.67 segundos
100        | 2.09 segundos
1000       | 2.09 segundos
10000      | 2.11 segundos

##### Con 4 procesos
Operacion map: 43/16794
Operacion map: 3051/16794
Operacion map: 5405/16794
Operacion map: 8827/16794
Operacion map: 13131/16794
Operacion map: 16425/16794
Operacion map: 16794/16794
Operacion reduce: 329/5576
Operacion reduce: 1067/5576
Operacion reduce: 1717/5576
Operacion reduce: 2307/5576
Operacion reduce: 4649/5576
Operacion reduce: 5576/5576
Operacion map: 0/1680
Operacion map: 1155/1680
Operacion map: 1680/1680
Operacion reduce: 0/558
Operacion reduce: 558/558
Operacion map: 0/168
Operacion map: 168/168
Operacion reduce: 0/56
Operacion reduce: 56/56
Operacion map: 0/17
Operacion map: 17/17
Operacion reduce: 0/6
Operacion reduce: 6/6
Operacion map: 0/2
Operacion map: 2/2
Operacion reduce: 0/1
Operacion reduce: 1/1
Tam fragmentacion | Duracion
--------------------
1          | 9.35 segundos
10         | 2.72 segundos
100        | 2.16 segundos
1000       | 2.10 segundos
10000      | 2.13 segundos
##### Con 8 procesos 
```
Operacion map: 22/16794
Operacion map: 1881/16794
Operacion map: 4105/16794
Operacion map: 6340/16794
Operacion map: 9481/16794
Operacion map: 13349/16794
Operacion map: 16794/16794
Operacion reduce: 4/5576
Operacion reduce: 3625/5576
Operacion reduce: 5576/5576
Operacion map: 0/1680
Operacion map: 716/1680
Operacion map: 1680/1680
Operacion reduce: 0/558
Operacion reduce: 558/558
Operacion map: 0/168
Operacion map: 168/168
Operacion reduce: 0/56
Operacion reduce: 56/56
Operacion map: 0/17
Operacion map: 17/17
Operacion reduce: 0/6
Operacion reduce: 6/6
Operacion map: 0/2
Operacion map: 2/2
Operacion reduce: 0/1
Operacion reduce: 1/1
Tam fragmentacion | Duracion
--------------------
1          | 6.26 segundos
10         | 2.78 segundos
100        | 2.17 segundos
1000       | 2.19 segundos
10000      | 2.27 segundos
```
### Documentación:
Respecto a los resultado obtenidos:
En el fragmento (1) se obtine lo siguiente:
Numero proceso: 1 | Duration: 4.77 segundos
Numero proceso: 2 | Duration: 4.77 segundos
Numero proceso: 4 | Duration: 9.35 segundos
Numero proceso: 8 | Duration: 6.26 segundos

Se ve en los procesos de (1 y 2) comienza con un duración  alta pero a comparación 
de los procesos (4 y 8) que se ve que son más altos que los procesos (1 y 2), esto se debe
a la sobrecarga, ya que se maneja muchos fragmentos pequeños. 

Asimismo, se ve en el fragmento (10000):
Numero proceso: 1 | Duration: 2.07 segundos
Numero proceso: 2 | Duration: 2.11 segundos
Numero proceso: 4 | Duration: 2.13 segundos
Numero proceso: 8 | Duration: 2.27 segundos

Se ve que el el proceso (8) aumento ligeramente la duración esto se debe  a que hay menos fragmentos 
que debe paralizar, lo cual hace reducir la eficacia.  