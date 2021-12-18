# Deployment


Despliegue de la API
----
Se realizó el despliegue del modelo auto-generado por el servicio de Auo-AI de IBM Cloud Pak 4 Data. El mejor modelo descrito en baseline_model.md, se guardó como
modelo en el proyecto generado para Unibank bajo el siguiente nombre "propensionNuevoProducto - P8 Snap Random Forest ClassifierpropensionNuevoProducto - P8 Snap Random Forest ClassifierpropensionNuevoProducto - P8 Snap Random Forest Classifier". Posteriormente, 
con el espacio de despliegue llamado "openscale-express-path-ce74f6dd-11bd-48be-bcf2-d31071596680" el modelo escogido se puso en producción permitiendo 
la publicación de la API la cual se puede consultar con una consulta JSON que tiene la estructura que se describe en el archivo JSONstructureAPI.txt.

La API a dia de hoy (18/12/21) está asociada al servicio de Data Studio, sin embargo para los pasos siguientes se considera que se realice el desplieuge en un
ambiente productivo tipo Postman que permita hacer un seguimiento mucho más robusto de las consultas realizadas.


Tableros de control
----
En el proyecto se consideró la contrucción de un tablero de control para el análisis de los datos de entrada del modelo que quedó desplegado haciendo uso del
servicio Cognos Analytics embebido en el Cloud Pak 4 Data. En la siguiente ruta puede visualizar un pantallazo del tablero generado (Cognos Analytics dashboard)
![Tablero de Control - Unibank](https://github.com/DCalvacheB/mlds6-project/blob/master/docs/deployment/dashboard_example.jpeg)
Este tablero consta de 1 hoja, 2 KPIs correspondientes a los prestamos de vivienda y préstamo de gastos personales, y medidas correspondientes a los demográficos.


Credenciales de Cloud Pak 4 Data
----
En cuanto las credenciales para poder acceder al servicio, el encargado de la gestión de los accesos es Melissa de La Pava.
En caso de requerir acceso puede comunicarse con ella a través del siguiente correo:

- melissa.lp@prueba.com 


