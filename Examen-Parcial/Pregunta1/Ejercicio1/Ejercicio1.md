1.- La primera simulacion se va ejecutar en 30 unidades de tiempo  en completarse
 con una utilizaciòn de CPU de 100%.

2.- Al aumentar el tamaño de l caché al rededor de 20 unidades de tiempo.
Al ejecutar el comando con la bandera -c se obtiene que el tiempo de finalización de 20.
Asimismo, que la CPU es de 100% [caliente 50.00]. Lo cual, con 
respecto a lo anterior se puede observar que se reduce el tiempo en 10 unidades de tiempo.


3.- Al hacer el rastreo con la bandera -T  se puede observar
que la segunda columna que disminuye cada una unidad de 29 pero esto
solo sucede en la unidad de tiempo de  0 a 9, pero de la unidad
10 al 19 se reduce cada dos comienza de 18 hasta 0.

4.- El cache se calienta en la unidad de tiempo 9  hasta el 19. Cuando se
cambia el parametro de tiempo de calentamiento a valores mayores como 100 ya
 no hay  ninguna de las unidades de tiempo con la cache que esta caliente. 
Mientras, con valores mas bajos como 1 se observa que en cada unidad de tiempo
esta la cache caliente.
