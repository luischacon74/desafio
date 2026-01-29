# Imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar requirements.txt y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo Python al contenedor
COPY app.py .

# Ejecutar el script cuando el contenedor inicie
CMD ["python", "app.py"]