# Propiedades de los Alpes

## Estructura del proyecto

Este proyecto consta de dos microservicios y sigue una arquitectura hexagonal como se explica a continuación:

* src
	* bff:
		* api: Esta carpeta contiene las diferentes versiones del API, routers, esquemas, mutaciones y consultas.
		* dispatchers.py: Este archivo contiene el código con la lógica para publicar comandos al broker de eventos.
 	* contracts: Esta carpeta contiene el microservicio de gestión contractual
		* api: Esta carpeta contiene la definición de los endpoints expuestos por el microservicio
		* config: Esta carpeta tiene la configuración del microservicio como ambiente de ejecución, URL de conexión a la base de datos, etc.
		* modules: Esta carpeta contiene los módulos del microservicio
			* sagas: Esta carpeta contiene el módulo de sagas
				* application: Esta carpeta contiene la lógica del módulo (casos de uso) que implementa las reglas de negocio de la aplicación y coordina las interacciones entre los diferentes componentes.
				* domain: Esta carpeta contiene la lógica del dominio del módulo, incluyendo las entidades, objetos de valor, servicios del dominio, etc.
				* infrastructure: Esta carpeta contiene las implementaciones concretas de los componentes, externos, como repositorios a bases de datos.
			* sales: Esta carpeta contiene el módulo de ventas
				* application: Esta carpeta contiene la lógica del módulo (casos de uso) que implementa las reglas de negocio de la aplicación y coordina las interacciones entre los diferentes componentes.
				* domain: Esta carpeta contiene la lógica del dominio del módulo, incluyendo las entidades, objetos de valor, servicios del dominio, etc.
				* infrastructure: Esta carpeta contiene las implementaciones concretas de los componentes, externos, como repositorios a bases de datos.
		* seedwork: Esta carpeta contiene componentes reutilizables y genéricos que pueden ser compartidos entre diferentes partes de la aplicación.
 	* properties: Esta carpeta contiene el microservicio de propiedades
		* api: Esta carpeta contiene la definición de los endpoints expuestos por el microservicio
		* config: Esta carpeta tiene la configuración del microservicio como ambiente de ejecución, URL de conexión a la base de datos, etc.
		* modules: Esta carpeta contiene los módulos del microservicio
			* sales: Esta carpeta contiene el módulo de ventas
				* application: Esta carpeta contiene la lógica del módulo (casos de uso) que implementa las reglas de negocio de la aplicación y coordina las interacciones entre los diferentes componentes.
				* domain: Esta carpeta contiene la lógica del dominio del módulo, incluyendo las entidades, objetos de valor, servicios del dominio, etc.
				* infrastructure: Esta carpeta contiene las implementaciones concretas de los componentes, externos, como repositorios a bases de datos.
		* seedwork: Esta carpeta contiene componentes reutilizables y genéricos que pueden ser compartidos entre diferentes partes de la aplicación.
	* listings: Esta carpeta contiene el microservicio de gestión de listados
		* api: Esta carpeta contiene la definición de los endpoints expuestos por el microservicio
		* config: Esta carpeta tiene la configuración del microservicio como ambiente de ejecución, URL de conexión a la base de datos, etc.
		* modules: Esta carpeta contiene los módulos del microservicio
			* sales: Esta carpeta contiene el módulo de ventas
				* application: Esta carpeta contiene la lógica del módulo (casos de uso) que implementa las reglas de negocio de la aplicación y coordina las interacciones entre los diferentes componentes.
				* domain: Esta carpeta contiene la lógica del dominio del módulo, incluyendo las entidades, objetos de valor, servicios del dominio, etc.
				* infrastructure: Esta carpeta contiene las implementaciones concretas de los componentes, externos, como repositorios a bases de datos.
		* seedwork: Esta carpeta contiene componentes reutilizables y genéricos que pueden ser compartidos entre diferentes partes de la aplicación.

## Despliegue

### Requisitos previos

Debes tener Docker Engine y Docker Compose en tu máquina. Para ello, puedes realizar cualquiera de las siguientes acciones:

* Instalar Docker Engine y Docker Compose como archivos binarios independientes.
* Instalar Docker Desktop, que incluye Docker Engine y Docker Compose.

> No necesitas instalar Python o PostgreSQL ya que estos son proporcionados por las imágenes de Docker.

### Instrucciones

1. Desde el directorio raiz de la aplicación inicia la aplicación ejecutando el siguiente comando:

 ```
 docker compose --profile "*" up
 ```

 Compose crea las imágenes necesarias para el código de la aplicación e inicia los servicios que se definieron. En este caso, el código se copia estáticamente en las imágenes en el momento de la compilación.

 Si quieres desplegar en modo detach (en segundo plano) utiliza:

 ```
 docker compose --profile "*" up --detach
 ```

2. Ya puedes empezar a utilizar los Servicios Web de la aplicación.

3. Para detener la aplicación y todos sus servicios, simplemente ejecuta el siguiente comando:

 ```
 docker compose --profile "*" down
 ```
