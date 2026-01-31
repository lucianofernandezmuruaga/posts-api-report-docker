import logging.config
import yaml
import config
from api_client import chequear_usuario
from validador import validar_posts
from database import inicializar_db, guardar_posts


with open('logging_config.yaml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger(__name__)

def ejecutar_auditoria():
    logger.info("--- Iniciando Auditoría de Usuarios ---")

    inicializar_db()

    for u in config.USUARIOS_MONITOREO:
        logger.info(f"--- Iniciando chequeo para Usuario ID: {u} ---")

        posts = chequear_usuario(u, config.BASE_URL)

        if posts:
            guardar_posts(posts)

            validar_posts(posts, u)

        logger.info("\n")

    logger.info("\n\n\n\n")


if __name__ == "__main__":
    ejecutar_auditoria()

