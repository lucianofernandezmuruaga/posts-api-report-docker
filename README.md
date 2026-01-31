# Sistema de Monitoreo y Auditoría de APIs

Este proyecto es un bot automatizado desarrollado en Python que consulta publicaciones de usuarios, valida la integridad de los datos y mantiene un registro histórico persistente.

## 🚀 Características
- **Modularización**: Estructura dividida en cliente de API, validador de lógica de negocio (en este caso sólo se chequea la longitud de los títulos) y gestión de base de datos (se almacenan los registros históricos).
- **Persistencia**: Almacenamiento automático en SQLite con prevención de duplicados (`INSERT OR IGNORE`).
- **Logging Avanzado**: Configuración jerárquica mediante YAML con salida dual (Consola/Archivo) y diferentes niveles de criticidad.
- **Configuración Segura**: Manejo de variables de entorno para URLs y credenciales sensibles.

## 🛠️ Requisitos
- Python 3.11+
- Librerías listadas en `requirements.txt`

## ⚙️ Configuración
1. Clonar el repositorio.
2. Crear un archivo `.env` basado en el siguiente esquema:
   ```env
   BASE_URL=[https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)
   DB_NAME=historico_posts.db
   ENV_TYPE=PRODUCCION

## 🐳 Docker

Este proyecto está preparado para ejecutarse en contenedores, lo que garantiza que funcione en cualquier entorno sin instalar dependencias manualmente.

1. **Construir la imagen**:
   ```bash
   docker build -t api-monitor .
   ```

2. **Ejecutar el contenedor**: (Es necesario pasar el archivo .env para que el contenedor tenga las variables de configuración)

   ```bash
   docker run --env-file .env api-monitor
   ```

## 📂 Estructura del Proyecto
**main.py**: Orquestador del flujo principal.

**api_client.py**: Gestión de solicitudes HTTP y manejo de latencia.

**database.py**: Lógica de persistencia en SQLite.

**validador.py**: Reglas de negocio y validación de datos.

**config.py**: Centralización de variables de entorno y constantes.

**logging_config.yaml**: Configuración profesional de registros (logs)


