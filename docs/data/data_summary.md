# Data Report
Este reporte contiene los resultados del análisis exploratorio de los datos.

Se adjunta [link html](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/Bank%20profiling%20min.html) de pandas profiling con informe gráfico.

Se adjunta [link del pdf](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/Pandas%20Profiling%20Report.pdf) del reporte de pandas profiling.

[Script](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/datasummary.py)

## General summary of the data
Son 31648 filas y 17 columnas.

## Data quality summary
No hay valores nulos ni repetidos.

## Target variable
Subscription. Variable binaria: ¿el cliente adquirió el producto?: "sí", "no".

## Individual variables

Son 7 variables categóricas:

Son 10 variables númericas: 

```
1 - Age
2 - Job: tipo de trabajo (categórico: "admin.", "Desconocido", "desempleado", "gerencia", "empleada doméstica", "emprendedor", "estudiante", "obrero", "autónomo" , "jubilado", "técnico", "servicios")
3 – Marital Status: estado civil (categórico: "casado", "divorciado", "soltero"; nota: "divorciado" significa divorciado o viudo)
4 - Education (categórica: "desconocida", "secundaria", "primaria", "terciaria")
5 - Credit: ¿tiene un crédito con incumplimiento? (binario: "sí", "no")
6 – Balance.euros: saldo medio anual, en euros
7 – Housing.Loan: ¿tiene préstamo para vivienda? (binario: "sí", "no")
8 – Personal.Loan: ¿tiene préstamo personal? (binario: "sí", "no")
Relacionado con el último contacto:
9 - Contact: tipo de comunicación de contacto (categórico: "desconocido", "teléfono", "celular")
10 – Last.Contact.Day: último día de contacto del mes.
11 - Last.Contact.Month: último mes de contacto del año (categórico: "jan", "feb", "mar",…, "nov", "dec")
12 - Last.Contact.Duration: duración del último contacto, en segundos.
Otros:
13 - Campaign: número de contactos realizados durante esta campaña y para este cliente (incluye el último contacto)
14 - pdays: número de días que pasaron después de que el cliente fue contactado por última vez desde una campaña anterior (-1 significa que el cliente no fue contactado previamente)
15 - Previous número de contactos realizados antes de esta campaña y para este cliente.
16 - poutcome: resultado de la campaña de marketing anterior (categórico: "desconocido", "otro", "fracaso", "éxito").
````

## Variable ranking
Las variables principales serian en orden:

Credito

Balance.euros

Housing.Loan

Personal.Loan

Campaign

## Relationship between explanatory variables and target variable

Correlación de la variable Subscription con las demás variables.

```[('Age', 0.01978331931739655),
 ('Last.Contact.Day', -0.032758728230326266),
 ('Campaign', -0.07447319499535197),
 ('Previous', 0.09021659134469255),
 ('Pdays', 0.10912924335766083),
 ('Balance..euros.', 0.055392299759917454),
 ('Last.Contact.Duration', 0.39277123377297957),
 ('Credit', -0.02275449590400965),
 ('Housing.Loan', -0.1369194817428766),
 ('Personal.Loan', -0.06948658523878946)]
 ```
 
 ![](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/correlacion.png)
 




