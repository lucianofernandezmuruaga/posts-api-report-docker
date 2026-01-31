import logging
import requests
import time

# Este logger se llamará "api_client"
logger = logging.getLogger(__name__)


def chequear_usuario(user_id, BASE_URL):
    posts = []

    try:
        logger.debug(f"Enviando solicitud GET a /posts?userId={user_id}")
        start_time = time.time()

        response = requests.get(f"{BASE_URL}/posts?userId={user_id}")
        latency = time.time() - start_time

        logger.info(f"Respuesta recibida en {latency:.2f}s (Status: {response.status_code})")

        if response.status_code == 200:
            posts = response.json()

            if not posts:
                logger.warning(f"El usuario {user_id} existe pero no tiene publicaciones.")
            else:
                logger.info(f"Éxito: Se encontraron {len(posts)} publicaciones.")

        else:
            logger.error(f"Error de API: El servidor respondió con código {response.status_code}")

    except requests.exceptions.ConnectionError:
        logger.critical("FALLO TOTAL DE CONEXIÓN: No se puede alcanzar el servidor de APIs.")

    time.sleep(1)
    return posts