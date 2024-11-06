# Usa una imagen oficial de Python como imagen base
FROM python:3.12-slim AS builder

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias en un directorio de usuario
RUN pip install --no-cache-dir --user -r requirements.txt

# Inicia una nueva etapa para crear una imagen más pequeña
FROM python:3.12-slim

# Copia los paquetes instalados de la etapa anterior
COPY --from=builder /root/.local /root/.local

# Asegúrate de que los scripts en .local sean utilizables
ENV PATH=/root/.local/bin:$PATH

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el contenido del directorio actual al contenedor en /app
COPY . .

# Exponer el puerto que utiliza la aplicación
EXPOSE 8000

# Ejecutar la aplicación FastAPI cuando se inicie el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

