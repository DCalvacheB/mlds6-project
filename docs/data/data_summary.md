# Data Report
Este reporte contiene los resultados del análisis exploratorio de los datos.

## General summary of the data
Son 31648 filas y 17 columnas.

## Data quality summary
No hay valores nulos ni repetidos.

## Target variable
Subscription. Variable binaria: ¿el cliente adquirió el producto?: "sí", "no".

## Individual variables

Son # variables categóricas:

Son # variables ordianles: 

Son # variables númericas: 

Son 4 variables binarias: 

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

Se adjunta el código utilizado:

```
from pandas_profiling import ProfileReport
profile = ProfileReport(data, minimal=True)
profile.to_file(output_file="Bank profiling.html")
```

Se adjunta [link](https://github.com/DCalvacheB/mlds6-project/blob/master/scripts/preprocessing/Bank%20profiling%20min.html) de pandas profiling con informe gráfico.
