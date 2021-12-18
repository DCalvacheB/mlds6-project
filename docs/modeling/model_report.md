# Final Model Report

## Analytic Approach
*El propósito del modelo generado es predecir cuantos clientes del banco serían propensos a adquirir el nuevo producto "Billetera Virtual".

*Se utilizó el set de datos "processtrainbank.csv" en la experimentación con "AutoAI" que contenía las variables descritas en el data_summary.md

*El modelo que se construyo fue un modelo de clasificación, se usó el servicio "AutoAI" de Cloud Pak for Data de IBM, y se optimizo en función de la precisión.

## Solution Description
La fuente de datos fue la última campaña realizada por el banco de un producto similar

Los componentes de la solución son:
Experimento de entrenamiento: Clasificación binaria
Modelos contemplados para la experimentación: *Decision Tree Classifier *Extra Trees Classifier *Gradient Boosting Classifier *LGBM Classifier *Logistic Regression *Random Forest Classifier *Snap Decision Tree Classifier *Snap Logistic Regression *Logistic regression. *Snap Random Forest Classifier *Snap SVM Classifier *XGB Classifier 

Hiperparámetros escogidos por el modelo.

El flujo de datos inicial se presenta en la gráfica del algoritmo.

Resultado: 
Algoritmo con la mejor precisión, Snap Random Forest Classifier de SnapML lib.

## Data

La fuente de datos fue la última campaña realizada por el banco. Contiene los datos sociodemográficos de los clientes actuales de Unibank, la forma en que se realizó el contacto durante la campaña y la decisión final del cliente con respecto al producto.

Se adjunta el link del Data Report

[Data Report](https://user-images.githubusercontent.com/92881375/146647194-9a867936-9e9a-4e0e-bceb-a9b92c0d75ff.png)

Son 31648 filas y 17 columnas.

![](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/Overview.png)

Se dividio en un set de entrenamiento de 70% y prueba del 30%.


## Features
En dependencia del tipo de variable del conjunto de datos, se procesaron por grupos en categórica, ordinal, númerica y binaria.

Las variables principales serian en orden:

Credito

Balance.euros

Housing.Loan

Personal.Loan

Campaign

## Algorithm

Data flow graph

![](https://github.com/DCalvacheB/mlds6-project/blob/master/docs/modeling/AutoAI-exp1.PNG)

Algortimo con la mejor precisión: Snap Random Forest Classifier de SnapML lib

Hiperparámetros escogidos por el modelo:

Profundidad del árbol(max_depth): 5,

Número de características a considerar(max_features): 0.1019932223477134,

Cantidad de árboles a considerar(n_estimators):27

random_state: 33


## Results
Gráfica de desempeño del mejor modelo: ![](https://github.com/DCalvacheB/mlds6-project/blob/master/docs/modeling/curvaROC-AutoAI.PNG)

Tabla de resultados de métricas de desempeño del mejor modelo: ![](https://github.com/DCalvacheB/mlds6-project/blob/master/docs/modeling/tabla-resultados-AutoAI.PNG) 
