import logging

logger = logging.getLogger(__name__)


def validar_posts(posts, user_id):
    logger.debug(f"Iniciando validación de {len(posts)} posts para el usuario {user_id}")

    titulos_cortos = 0
    for post in posts:
        if len(post.get('title', '')) < 15:
            titulos_cortos += 1
            logger.debug(f"Post ID {post.get('id')} tiene título muy corto.")

    if titulos_cortos > 0:
        logger.warning(f"Usuario {user_id}: Se encontraron {titulos_cortos} posts con títulos demasiado cortos.")
    else:
        logger.info(f"Usuario {user_id}: Todos los títulos cumplen con la extensión mínima.")

    return titulos_cortos