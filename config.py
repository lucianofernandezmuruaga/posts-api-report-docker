import os
import sys
from dotenv import load_dotenv

def get_env_variable(var_name, default=None, obligatorio=False):
    valor = os.getenv(var_name, default)
    if obligatorio and valor is None:
        raise ValueError(f"❌ Error Crítico: La variable de entorno '{var_name}' es obligatoria y no está definida.")
    return valor

load_dotenv()

if not load_dotenv():
    print("⚠️  ADVERTENCIA: No se encontró el archivo '.env'; se usará un valor de tabla por defecto")

try:
    BASE_URL = get_env_variable("BASE_URL", obligatorio=True)
    DB_NAME = get_env_variable("DB_NAME", default="historico_posts.db")
    MODO = get_env_variable("ENV_TYPE", default="PRODUCCION")
except ValueError as e:
    print(e)
    sys.exit(1)

USUARIOS_MONITOREO = [1, 5, 999, 2]