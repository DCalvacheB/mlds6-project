# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each data, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. 
If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts 
that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided. 

_**For ease of modifying this report, placeholder links are included in this page, for example a link to dataset 1, but they are just placeholders pointing to a non-existent page. These should be modified to point to the actual location.**_

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Dataset 1 | Concurso Privado de Kaggle: Los datos provistos son para fines académicos unicamente. |  | [preparacionDatos.ipynb](tdsp_template/scripts/data_adquisition/) | [Reporte 1 DatosClieente]()|


* Dataset1 summary. Contiene los datos de la última campaña realizada por el banco de un producto similar. Contiene los datos sociodemográficos de los clientes 
actuales de Unibank, la forma en que se realizó el contacto durante la campaña y la decisión final del cliente con respecto al producto.


## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset 1 | [Dataset1](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/Train%20bank.csv) | [processed_data.py](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/processed_data.py) | [Processed Dataset 1 Report](https://github.com/DCalvacheB/mlds6-project/blob/master/docs/data/data_summary.md)|

* Processed Data1 summary. Se arreglo el nombre de las variables, dada la presencia de problemas ortográficos de comillas "" adicionales. Se borraron comillas "" adicionales presentes tambien en los valores y los datos nulos. En dependencia del tipo de variable del conjunto de datos, se procesaron por grupos en categórica, ordinal, númerica y binaria.


## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
|"featuretrainbank.csv" | [ processtrainbank.csv ](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/processtrainbank.csv) | [featuring.py](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/featuring.py) | [featuretrainbank Report](https://github.com/DCalvacheB/mlds6-project/blob/master/docs/data/data_summary.md))|

*"featuretrainbank.csv". Recibe como insumo "processtrainbank.csv" y utiliza un objeto ColumnTransformer de sklearn para dejar las variables numéricas. 

