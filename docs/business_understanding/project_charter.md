# Project Charter
 
## Business background

* Who is the client, what business domain the client is in.
El cliente, Unibank, un banco muy importante del sector financiero de Alemania, se encuentra ubicado a lo largo del territorio, y se caracteriza por ser el primer 
banco en realizar la completa transformación digital de todo el servicio de atención al cliente.

* What business problems are we trying to address?
Quieren promocionar el nuevo producto desarrollado denominado "Billetera virtual". Para lo cual resulta esencial identificar a los clientes tendrían un mayor interés
en adquirir este producto cuando sea lanzado al mercado.


## Scope
* What data science solutions are we trying to build?
De acuerdo a la información disponible del objetivo de negocio planteado el equipo de data science propone realizar un modelo de propensión de compra.

* What will we do?
Siguiendo la metodología de Team Data Science Process (TDSP), se  establece el objetivo de negocio descrito anteriormente. Luego, se realiza el preprocesamiento y
preparación de los datos para obtener insumos de alta calidad. Se procederá a realizar el modelado de los datos incluyendo técnicas analíticas que permitan
establecer una probabilidad de compra por parte de los usuarios. Posteriormente, se dispondrá el modelo en la nube de IBM  a través de una API a los usuarios finales
del banco que serán los analistas de mercadeo.

* How is it going to be consumed by the customer?
El modelo se desplegará en el servicio Watson Studio en la nube de IBM Cloud Pak 4 Data. En este servicio se permite el aprovisionamiento de un API, que podrá ser
consumido por las aplicaciones internas del banco en el área usuaria.

## Personnel
* Who are on this project:
	* JDK Consulting Services:
		* Project lead: Juan Sebastian Lara, Melissa De La Pava
		* PM: Juan Sebastian Lara, Melisssa De La Pava
		* Data scientist(s): 
			- Krystian Marentes
			- Jorge Suarez
			- Daniela Calvache
		* Account manager: 
	* Client:
		* Data administrator: Hans Landa
		* Business contact: +49 503-544-54-42
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn)
Aumentar la probabilidad de adquisición por parte del cliente durante las campañas de adquisición del producto.

* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
Posicionar el producto dentro del Top 5 de los productos del banco.

* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%) 
Posicionar el producto "Billetera virtual" en el 20% de los clientes de Unibank.

* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
No aplica por que es un producto nuevo dentro del portafolio de Unibank.

* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
6 meses después del lanzamiento de "Billetera virtual" se realizará un estudio cuantitativo para evaluar la cantidad de clientes que adquirieron el producto.

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.


Plan de trabajo:

- Entendimiento del negocio: Identificación del problema de negocio, alineación con la estrategia organizacional y definición del objetivo del proyecto.
- Entendimiento de los datos: Definición de los origenes de datos, exploración inicial de los datos y definición de calidad y completitud de los mismos.
- Preparación de los datos: Extracción de los datos, integración de las fuentes, transformación de las variables(ajuste de los formatos de las variables, generación
de nuevas varibles, etc) y carga a una única fuente de información.
- Modelado: Desarrollo de la ténica de Machine Leraning  que solucionará el objetivo propuesto.
- Evaluación: Análisis de las métricas del modelo para determinar el desempeño del modelo en producción.
- Despliegue: Puesta en producción del modelo, y definición de los métodos de consumo del mismo.
- Documentación: Registro escrito del desarrollo propuesto a lo largo del proyecto. 

El cronograma de trabajo se encuentra disponible en la carpeta 'docs' con el nombre de 'Unibank - plan de trabajo'. 

## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
	- Los datos del cliente se encuentran en archivos de texto plano en formato CSV.
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
	- Los archivos de los datos se cargarán de manera manual a este sistema de archivos y se alojrán en la carpeta 'scripts/data_adquisition'

* What tools and data storage/analytics resources will be used in the solution e.g.,
	- Python, Google Colab Notebooks, IBM CP4D.
 
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo
 code for the APIs of the web service calls.
	- El modelo de propensión de compra se consumirá a través de una API, para cual le entregarán al cliente las credenciales y la estructura de la llamada
a la API.

* How will the customer use the model results to make decisions
	- El area usuaria calificará las listas de los clientes para identificar a los que tienen mayor probabilidad de adquirir el producto, y podrán enfocar las 
estrategias de las campañas de ofrecimiento a estas personas de acuerdo a la puntuación.

  * Data movement pipeline in production
* Make a 1 slide diagram showing the end to end data flow and decision architecture. If there is a substantial change in the customer's business workflow, make 
a before/after diagram showing the data flow.
El esquema de la arquitectura propuesta esta disponible en la carpeta de 'tdsp_template/docs' con el nombre de 'Unibank - Arquitectura' 


## Communication
* How will we keep in touch? Weekly meetings? 
El equipo se comunicará para los dailys a través de Whatsapp, y para las reuniones semanles a través de Google Meet.

* Who are the contact persons on both sides?
	* Krystian Marentes. Gerente de la cuenta.
	* Hans Landa. Product Owner.
