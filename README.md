🐳 Tienda Online – Práctica 2.2 (Contenerización con Docker)

Este repositorio corresponde a la práctica 2.2 del módulo de DevOps.
El objetivo era contenerizar la aplicación de la práctica 1.3 (sistema básico de tienda online hecho en Python), crear un Dockerfile funcional y ejecutar todo dentro de un contenedor.

*** Construcción de la imagen ***

Para construir la imagen Docker, hay que situarse en la carpeta raíz del proyecto y ejecutar:

```bash
docker build -t tienda-online:latest .
```

Esto descarga la imagen base python:3.12-slim, copia los archivos del proyecto e instala las dependencias indicadas en requirements.txt.

*** Ejecución del contenedor ***

Una vez construida la imagen, la aplicación se ejecuta con:

```bash
docker run --rm tienda-online:latest
```


El flag --rm simplemente elimina el contenedor al finalizar su ejecución para no acumular contenedores innecesarios.

*** Variables de entorno ***

La aplicación no utiliza variables de entorno.
Aun así, dejo este apartado por si en futuras prácticas se añaden configuraciones.

*** Salida esperada *** 

Al ejecutar el contenedor, deberían mostrarse en la terminal:

El inventario inicial con los productos creados

Los pedidos simulados para los usuarios

El stock actualizado después de los pedidos

El histórico de pedidos del cliente “Isay”, ordenado por fecha

En resumen, la misma salida que genera el main.py cuando se ejecuta localmente, pero ahora dentro de Docker.

*** Estructura del proyecto ***

Tienda_online/
│
├── models/
├── Services/
├── main.py
├── dockerfile
├── .dockerignore
├── requirements.txt
└── README.md

