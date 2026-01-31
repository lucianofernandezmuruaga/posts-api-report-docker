import config
import logging
import sqlite3

logger = logging.getLogger(__name__)


def conectar_db():
    return sqlite3.connect(config.DB_NAME)

def inicializar_db():
    try:
        with conectar_db() as conexion:
            cursor = conexion.cursor()

            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS posts (
                            id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            title TEXT,
                            body TEXT
                        )
                    ''')

            conexion.commit()

            logger.info("Base de datos inicializada correctamente.")

    except sqlite3.Error as e:
        logger.error(f"Error al inicializar la base de datos: {e}")


def guardar_posts(lista_posts):
    with conectar_db() as conexion:
        try:
            cursor = conexion.cursor()

            for post in lista_posts:
                cursor.execute('''
                    INSERT OR IGNORE INTO posts (id, user_id, title, body)
                    VALUES (?, ?, ?, ?)
                ''', (post['id'], post['userId'], post['title'], post['body']))

            conexion.commit()
            count = conexion.total_changes

            if count > 0:
                logger.info(f"Se guardaron {count} registros nuevos en la base de datos.")
            else:
                logger.debug("No hubo registros nuevos para guardar.")

        except sqlite3.Error as e:
            logger.error(f"Error al guardar en la base de datos: {e}")