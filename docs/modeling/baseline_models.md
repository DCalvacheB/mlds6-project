# Baseline Model Report



. 

## Analytic Approach

* El propósito del modelo generado es predecir quienes son los clientes del banco que serían más propensos a adquirir el nuevo producto "Billetera Virtual".
* Con el objetivo de tener una idea inicial para el modelo base, se usó el servicio "AutoAI" de Cloud Pak for Data de IBM, el cual arrojó un modelo base con el cual se partió para hacer el modelo de clasificación.
* Se utilizó el set de datos "processtrainbank.csv" en la experimentación con "AutoAI" que contenía las variables descritas en el data_summary.md
* Se configuró la ejecución del servicio para optimizar la construcción del modelo en función de la precisión.

## Model Description

* Detalles de la experimentación ejecutada con AutoAI

	* Link al flujo de resultado de AutoAI:(AutoAI-exp1.png) []
	* Experimento de entrenamiento: Clasificación binaria
	* Algortimo con la mejor precisión: Snap Random Forest Classifier de SnapML lib.
	* Precisión del mejor modelo obtenido: 0.96
	* Modelos contemplados para la experimentación: 
		*Decision Tree Classifier
		*Extra Trees Classifier
		*Gradient Boosting Classifier
		*LGBM Classifier
		*Logistic Regression
		*Random Forest Classifier
		*Snap Decision Tree Classifier
		*Snap Logistic Regression
		*Logistic regression.
		*Snap Random Forest Classifier
		*Snap SVM Classifier
		*XGB Classifier
	*Hiperparámetros escogidos por el modelo:
		- Profundidad del árbol(max_depth): 5,
		- Número de características a considerar(max_features): 0.1019932223477134,
		- Cantidad de árboles a considerar(n_estimators):27
		- random_state: 33
		

## Results (Model Performance)
* Gráfica de desempeño del mejor modelo: (curvaROC-AutoAI.png)[]

* Tabla de resultados de métricas de desempeño del mejor modelo: (tabla-resultados-AutoAI.png)[] 

* Se almacenó el cuaderno de Jupyter generado con experimento ejecutado de AutoAI: (propensionNuevoProducto-ntb.ipynb)[]


## Model Understanding

* Importancia de las variables escogidas por el mejor modelo: (ImportanciaVariables-AutoAI.png)[]

* 

## Conclusion and Discussions for Next Steps

* La experimentación con Auto AI arrojó que la familia de modelos adecuada para este caso, es la de Random Forests. Con los resultados obtenidos y el cuaderno generado se podría depurar las variables que de acuerdo al modelo
construido presentan una menor importancia para realizar la extracción de características.

* Dada la cantidad de variables tenidas en cuenta para la experimentación, se obtuvo como resultado que es recomendable utilizar PCA para realizar la reducción de la dimensionalidad.


