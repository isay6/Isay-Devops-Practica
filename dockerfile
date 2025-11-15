# Imagen base ligera
FROM python:3.12-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias sin caché
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Ejecutar la aplicación
CMD ["python", "main.py"]
