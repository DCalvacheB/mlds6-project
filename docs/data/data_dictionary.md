# Data Dictionary

In this document you must describe the tables, collections or files that you are using in the project. You can describe each database and provide UML diagrams for a better design description.

# Database Name 1

Description of the database.

## Table 1

Here you must describe the table

| column | type | description |
| --- | --- | --- |
| Age | STR | Edad del cliente |
| Job | STR | Tipo de trabajo((categórico: "admin.", "Desconocido", "desempleado", "gerencia", "empleada doméstica", "emprendedor", "estudiante", "obrero", "autónomo" , "jubilado", "técnico", "servicios"))|
| Marital status | STR | Estado civil(categórico: "casado", "divorciado", "soltero"; nota: "divorciado" significa divorciado o viudo)|
| Education | STR | Nivel de educación (categórica: "desconocida", "secundaria", "primaria", "terciaria")|
| Credit | STR | Presenta incumplimeinto con un producto creditivio ("si" o "no")|
| Balance.euros | STR | Salario anual en euros.|
| Housing.loan | STR | Indica si el cliente tiene o no un préstamo de vivienda("si" o "no")|
| Personal.loan | STR |  Indica si el cliente tiene o no un préstamo personal("si" o "no")|
| Contact | STR | Tipo de contacto para comunicación con el cliente("desconocido", "telefono", "celular")|
| Last contact day | STR | Último día de contacto en el mes |
| Last connection Month | STR | Último mes que se contactó a la persona |
| Last contact duration | STR | Duración en segundos del último contacto |
| Campaign | STR | Número de veces que se contactó al cliente durante esta campaña(incluyen el último contacto)|
| pdays | STR | Número de días desde el último contacto(-1 significa que no ha sido contactado previamente)|
| Previous | STR | Número de contactos realizados previamente| 
| poutcome | STR | Resultado de la campaña anterior("desconocido", "otro", "fracaso", "éxito")|
| suscription | STR | Adquirió el producto o no ("si" o "no")|
