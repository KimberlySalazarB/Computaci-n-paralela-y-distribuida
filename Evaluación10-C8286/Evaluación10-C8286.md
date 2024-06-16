**Procesamiento de registros mediante Amazon EMR**

Apache Hadoop es un marco de código abierto que admite el procesamiento masivo de datos en un grupo de instancias. Hadoop se puede ejecutar en una única instancia de Amazon Elastic Compute Cloud (Amazon EC2) o en miles de instancias. Hadoop utiliza el sistema de archivos distribuido de Hadoop (HDFS) para almacenar datos en múltiples instancias, que Hadoop llama nodos. Hadoop también puede leer y escribir datos en Amazon Simple Storage Service (Amazon S3).

**Tarea 1: Lanzamiento de un clúster de Amazon EMR Crear un clúster EMR (Software):**

Asegúrese de que estas aplicaciones estén seleccionadas: Hadoop 2.8.5

Colmena 2.3.6

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.001.jpeg)

Hadoop instalará y configurará el HDFS interno del clúster, así como el programador y coordinador de recursos YARN para procesar trabajos en el clúster. Hive es un marco de código abierto que se puede utilizar para almacenar y consultar grandes conjuntos de datos. Hive es una capa de abstracción que traduce consultas SQL en trabajos YARN que se ejecutan y extraen resultados de los datos almacenados en HDFS.

**Configuración del clúster (Hardware):**

En la sección Configuración del clúster, establezca el tipo de instancia y la cantidad de nodos que se usarán:

Verifique que en Escalado y aprovisionamiento del clúster, el tamaño de la instancia principal esté establecido en 2.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.002.jpeg)

El nodo principal coordina los trabajos que se ejecutarán en el clúster. El nodo principal ejecuta HDFS NameNode así como YARN ResourceManager. Los nodos centrales actúan como HDFS DataNodes y son donde los datos HDFS se replican y almacenan en el disco.

**En la sección Redes:**

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.003.jpeg)

**Terminación del clúster/registros del clúster:**

Para la terminación del clúster, desmarque (anule la selección) la opción Usar protección de terminación.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.004.jpeg)

Para la ubicación de Amazon S3, elija Examinar S3 y seleccione el depósito de S3 para la salida de Hive.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.005.jpeg)

**Configuración de seguridad y par de claves EC2:**

Para el par de claves de Amazon EC2 para SSH al clúster, elija el par de claves vockey.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.006.jpeg)

Para la función de servicio, confirme que se haya elegido EMR\_DefaultRole.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.007.jpeg)

En Perfil de instancia EC2 para Amazon EMR y perfil de instancia, confirme que se haya elegido EMR\_EC2\_DefaultRole.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.008.jpeg)

**Configuración de grupo de seguridad**

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.009.jpeg)

En esta tarea, aprovisionó un clúster de EMR con Hive ejecutándose en él. También configuró el grupo de seguridad para el nodo principal del clúster para que acepte conexiones SSH.

**Confirme que el clúster ya está disponible.**

En la sección Instancias (Hardware), verifique que el estado de los tipos de nodo principal y principal sea En ejecución.

Importante: No continúe con la siguiente tarea hasta que el estado del clúster muestre En espera y el estado de los nodos muestre En ejecución.

**Tarea 2: Conexión al nodo principal de Hadoop mediante SSH**

Conéctese al IDE de AWS Cloud9.

En el IDE, elija Archivo > Nuevo archivo.

Pegue el valor de DNS público de su portapapeles en el archivo.

En el panel que se abre, elija Descargar PEM y guarde el archivo en el directorio de su elección.

Regrese al IDE de AWS Cloud9.

Elija Archivo > Cargar archivos locales....

Cargue el archivo labsuser.pem en el IDE de AWS Cloud9.

A continuación, para modificar los permisos en el archivo del par de claves para que el software SSH le permita usarlo, ejecute el siguiente comando en la pestaña del terminal IDE:

**chmod 400 labsuser.pem**

Establezca una conexión SSH con el nodo principal del clúster.

Ejecute el siguiente comando. Reemplácela con la dirección DNS pública del nodo principal que copió anteriormente.

ssh -i labsuser.pem hadoop@<PUBLIC-DNS>

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.010.jpeg)

Ahora está conectado al nodo principal de Amazon EMR, que se ejecuta en una instancia EC2, mediante SSH desde la instancia de AWS Cloud9.

**Tarea 3: ejecutar Hive de forma interactiva**

En esta tarea, configurará un directorio de registro para Hive y luego iniciará una sesión interactiva de Hive en el nodo principal del clúster de EMR.

Para crear un directorio de registro para Hive, ejecute los siguientes comandos:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.011.png)

**Configurar Hive**

Para recuperar el nombre del depósito de S3 donde desea almacenar la salida de Hive, ejecute el siguiente comando:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.012.png)

Ejecuta el siguiente comando. Reemplácelo con el nombre completo del depósito de salida.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.013.png)

**Tarea 4: Crear tablas a partir de datos de origen mediante Hive**

En esta tarea, creará dos tablas de Hive que formarán su almacén de datos. Las tablas harán referencia a los datos almacenados en Amazon S3. Estas tablas servirán como datos de entrada para consultas que ejecutará más adelante en el laboratorio. En esta tarea, utilizará HiveQL, un lenguaje similar a SQL, para cargar datos y ejecutar consultas.

Para crear una tabla externa llamada impresiones, ejecute el siguiente código en la terminal AWS Cloud9:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.014.png)

Observe que este comando creó una tabla externa. Cuando crea una tabla externa, los datos de la tabla no se copian en HDFS. Si no especificó externo, los datos de la tabla se copiarán en HDFS. Los datos de esta tabla permanecen en Amazon S3. Si alguna vez se eliminara esta tabla externa, los datos no se eliminarían de Amazon S3.

Actualice los metadatos de Hive para la tabla de impresiones para incluir todas las particiones.

Para ver cuántas particiones tiene actualmente la tabla de impresiones, ejecute el siguiente comando:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.015.jpeg)

El resultado describe los nombres de las columnas, la ubicación de los datos, el número de particiones y otros metadatos sobre la tabla.

Para inspeccionar los datos de entrada y aplicar particiones al metastore, ejecute el siguiente comando:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.016.jpeg)

El comando MSCK REPAIR TABLE escanea Amazon S3 en busca de particiones compatibles con Hive que se agregaron al sistema de archivos después de crear la tabla. Si se encuentran particiones, se agregan a los metadatos de la tabla. Este comando es una extensión que se encuentra en la versión AWS de Hive.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.017.jpeg)

El resultado ahora debería indicar que existen 241 particiones en la tabla.

Análisis: las particiones almacenan datos organizándolos lógicamente para mejorar el rendimiento de las consultas. Normalmente, los datos se segmentan en particiones para proporcionar un acceso más rápido a subconjuntos específicos de datos.

Crea otra tabla externa y descubre nuevamente sus particiones. Esta tabla se denominará clics y hace referencia a los registros de flujo de clics.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.018.png)

Para devolver todas las particiones de los datos de registro de flujo de clics, ejecute el siguiente comando:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.019.jpeg)

Verifique que las dos tablas ahora existan. Ejecute el siguiente comando:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.020.png)

El resultado devuelve los nombres de ambas tablas externas almacenadas en Amazon S3:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.021.jpeg)

**Tarea 5: unir tablas mediante Hive**

Tanto las tablas de clics como de impresiones son tablas particionadas. Cuando los dos estén unidos, el comando CREATE TABLE le indicará a la nueva tabla que se particione.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.022.png)

Para crear una nueva tabla temporal en HDFS llamada tmp\_impressions para almacenar datos intermedios, ejecute el siguiente comando:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.023.png)

Para insertar datos del registro de impresiones durante el período de tiempo al que se hace referencia, ejecute el siguiente comando:

Este comando ejecuta un trabajo MapReduce para procesar la solicitud. El resultado es similar a la siguiente imagen:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.024.jpeg)

Para crear una combinación externa izquierda de tmp\_clicks y tmp\_impressions que escriba el conjunto de datos resultante en la tabla join\_impressions en su depósito de salida de S3, ejecute el siguiente comando:

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.025.jpeg)

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.026.png)

**Tarea 6: Consultar el conjunto de datos resultante**

En esta tarea, utilizará Hive para ejecutar consultas similares a SQL sobre los datos que ahora existen en la tabla join\_impressions. Esto le permitirá analizar qué impresiones generaron clics en los anuncios.

set hive.cli.print.header=true;

Para devolver las primeras 10 filas de datos en la tabla join\_impressions, ejecute el siguiente comando SELECT:

SELECT \* FROM joined\_impressions LIMIT 10;

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.027.png)

Utilice consultas similares a SQL para consultar el conjunto de datos resultante.

Para indicarle al cliente HiveSQL que imprima los nombres de las columnas como encabezados en los conjuntos de resultados, ejecute el siguiente comando:

SELECT adid, count(\*) AS hits FROM joined\_impressions WHERE clicked = true GROUP BY adid ORDER BY hits DESC LIMIT 10;

Continúe ejecutando consultas SQL en el conjunto de datos.

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.028.png)

**Module 9 Knowledge Check**

![](Aspose.Words.3ec85341-fa5a-4450-9385-b585762d25d1.029.jpeg)
