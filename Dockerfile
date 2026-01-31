# 1. Usamos una imagen de Python oficial y ligera
FROM python:3.11-slim

# 2. Definimos dónde va a vivir el código dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de requerimientos primero (para optimizar cache)
# Nota: Asegúrate de tener un requirements.txt con requests, pyyaml y python-dotenv
COPY requirements.txt .

# 4. Instalamos las librerías
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todo nuestro código al contenedor
COPY . .

# 6. Comando para ejecutar el bot
CMD ["python", "main.py"]