from Conexion import Conexion
from logger_base import log

class CursorPool:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug(f'Se ejecuta metodo __exit__')
        if exc_val:
            self._conn.rollback()
            log.error(f'Ocurrio una excepcion en la BD: {exc_val}')
        else:
            self._conn.commit()
            log.debug(f'Commit correcto de la transaccion')

        self._cursor.close()
        Conexion.liberarConexion(self._conn)
