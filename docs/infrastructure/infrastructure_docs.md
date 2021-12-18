# Infrastructura

Cloud Pak for Data es una plataforma integrada que permite a las organizaciones acelerar los procesos de adopción de estrategias basadas en datos a partir de la reducción de la operatividad y en consecuencia el aumento de la productividad. Es una plataforma basada completamente en la nube, por lo tanto su implementación se puede lograr de manera rápida y sencilla en las organizaciones. En este sentido, Unibank no requirió el aprovisionamiento de alguna infraestructura importante para la implementación de este proyecto.

En este sentido, para el uso de la plataforma por parte de los científicos de datos, sólo se requiere un computador con conexión a internet. En cuanto a la infraestructura del servicio, Unibank no cuenta con algún tipo de control ni administración. Sin embargo, como referencia, se adjunta diagrama de arquitectura de bloques de la implementación del servicio.
![Diagrama de Arquitectura](https://github.com/DCalvacheB/mlds6-project/blob/master/docs/infrastructure/infra_diagram.png)

* Configuración y administración de docker/kubernetes: No aplica. Si bien el servicio en la nube cuenta con estas plataformas, Unibank no las administra.

* Configuración de servidor: No aplica. Para la implementación de este proyecto no se cuenta con infraestructura basada en servidores propia de Unibank.

* Configuración del entorno: Poetry y Pyenv no fueron necesarios implementarlos. Cloud Pak for Data ya cuenta con Jupyter notebook como framework para la codificación. Otros servicios incluidos en la aplicación Watson Studio que también fueron usados en el desarrollo de este proyecto fueron IBM Cognos Analytics (dashboarding), AutoAI (exploración de modelos automáticos), Watson Machine Learning (despliegue del modelo).
