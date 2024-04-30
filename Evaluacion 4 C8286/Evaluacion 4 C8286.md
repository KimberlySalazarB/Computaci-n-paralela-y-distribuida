**Evaluación: Módulos 2 y 3 AWS Data Engineering**

**Módulos 2:**

**Crear un template y stack de CloudFormation:**

Para crear un template se hace uso del terminal de AWS Cloud9, para ello, se hace clic en la parte de Cloud9 IDE en **abrir.**

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.001.png)

Luego, de hacer clic en abrir se abre una nueva ventana donde muestra **AWS Cloud9 IDE.** Después, se hace clic en **File >New File** que tendrá como nombre **create\_bucket.yml.** Asimismo, contendrá el siguiente código que hace lo siguiente:

- Crear un bucket de S3
- Bloquea el acceso público al bucket
- Habilita el control de versiones para el bucket
- Habilita el cifrado server-side para el bucket

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.002.jpeg)

Para validar el template de CloudFormation, se ejecuta el siguiente comando y se obtiene el siguiente resultado que nos confirma que el template es válida.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.003.png)

1\. Ahora se crea un stack de CloudFormation a partir del template. Un stack implementa y administra el grupo de recursos que se describen en el template. Un template de CloudFormation como un modelo y el stack es la instancia real del template que crea los recursos.

- Con el siguiente comando se crea el stack. Luego de ejecutar se obtiene el resultado un nombre de recurso de Amazon (ARN) de CloudFormation, lo cual, confirma el stack se creó.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.004.png)

- Se ejecuta el siguiente comando para verificar que el stack creó los recursos necesarios y se debe tener el siguiente resultado.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.005.png)

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.006.jpeg)

Ahora se pasa a eliminar el bucket eliminando el stack, ya que cuando se elimina el stack, se eliminan todos los recursos que contiene.

Con el siguiente comando se elimina el stack.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.007.png)

Para confirmar que el stack y sus recursos se eliminaron. Buscamos CloudFormation y se elige Stack para verificar que el stack **ade-my-bucket** que se creó al inicio ya no está incluido en la lista de stacks activos.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.008.jpeg)

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.009.jpeg)Asimismo, se puede utilizar el siguiente comando para verificar que el stack se eliminó. El resultado proporciona información de varios stacks, pero la pila que se creó al inicio está con **StackStatus** de **DELETE\_COMPLETE.**

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.010.jpeg)

Por otra parte, se ejecuta el siguiente comando para verificar que el bucket que se creó al inicio se eliminó con la eliminación del stack. Como resultado se obtiene otro bucket pero no es lo que se creó al inicio.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.011.png)

**Cargar datos de muestra en un bucket de S3**

Se ejecuta los siguientes comandos para descargar el archivo **code.zip** que contiene los datos para ello se utiliza el comando **wget** y **unzip** para descomprimir el archivo .zip , creando un archivo llamado lab1.csv en la carpeta actual.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.012.jpeg)

Con el siguiente comando se hace una copia del archivo lab1.csv al bucket ade-s3lab-bucket–58000030.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.013.png)

Para confirmar que el archivo está en el bucket se ejecuta el siguiente comando.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.014.png)

**Consultar los datos:**

Dentro de bucket ade-s3lab-bucket–58000030 seleccionamos el archivo agregado lab1.csv y hacemos clic en **Acciones > Consultar con S3 Select.**

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.015.jpeg)

Luego de ello, en la sección de Consulta SQL, poner la siguiente consulta. Después elegimos Ejecutar consulta SQL.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.016.jpeg)

Se obtiene el siguiente resultado de la consulta que devolverá las columnas de los primeros cinco registros del conjunto de datos.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.017.jpeg)

Asimismo, se puede ver de la siguiente manera con datos en formato tabular (filas y columnas), con la opción Formateado.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.018.jpeg)

Ahora se hace otra consulta para ver solo los nombres de las tres primeras filas.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.019.jpeg)

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.020.jpeg)

**Modificar las propiedades de cifrado y el tipo de almacenamiento de un objeto:**

Para ello, hacemos clic en **Acciones> Editar clase de almacenamiento**.

En la sección Clase de almacenamiento, elija Niveles inteligentes. Luego, Guardar cambios.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.021.jpeg)

Al utilizar la clase de almacenamiento Intelligent-Tiering, se asegura de que los costos se optimicen para todos los datos almacenados dentro del objeto S3.

**Comprimir y consultar el conjunto de datos**

1. Para comprimir el archivo lab1.csv con formato ZIP ejecute el primer comando de zip lab lab1.csv.
1. Luego, para comprimir el archivo con formato GZIP, ejecute el segundo comando con gzip -v lab1.csv
1. Para enumerar los objetos en el directorio, ejecute ls -la

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.022.png)

El tamaño más pequeño reducirá el costo de almacenar el archivo en Amazon S3.

- Para cargar la versión GZIP del conjunto de datos en el depósito S3, ejecute el siguiente comando.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.023.png)

Verificamos que se puede usar S3 Select para consultar el archivo comprimido. Para ello, elige el enlace lab1.csv.gz. Luego, Acciones de objeto > Consultar con selección de S3.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.024.jpeg)

Asimismo, en la sección de Consulta SQL y hacemos la siguiente consulta.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.025.jpeg)

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.026.jpeg)

**Administrar y probar el acceso restringido para un miembro del equipo:**

Revise el grupo de IAM DataScienceGroup y la política de IAM adjunta al grupo:

En el enlace Política para científicos de datos que está dentro de la página de detalles de DataScienceGroup, se muestra detalles de la política.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.027.jpeg)

Ahora, determine si Paulo puede acceder a los datos en Amazon S3. Para ello, debe recuperar su ID de clave de acceso y su clave de acceso secreta. En CloudFormation, en el panel de navegación haga clic en Stacks. Elija el enlace para el nombre del stack donde la Descripción contiene ADE. En la página de detalles de la pila, elija la pestaña Salidas. Luego, se copia ambos valores y se los pone en variables bash (AK y SAK)

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.028.jpeg)

Para probar si el usuario paulo puede ejecutar un comando de AWS CLI para el servicio Amazon Elastic Compute Cloud (Amazon EC2), ejecute el siguiente comando

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.029.jpeg)

Pruebe si el usuario paulo puede ejecutar comandos de AWS CLI en un objeto S3. Ejecute el siguiente comando

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.030.jpeg)

Para ver el contenido del objeto S3, ejecute el siguiente comando.

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.031.png)

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.032.jpeg)

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.033.jpeg)

![](Aspose.Words.a0406ccf-5cf1-4b83-9fa7-28f4dbdce17c.034.jpeg)
