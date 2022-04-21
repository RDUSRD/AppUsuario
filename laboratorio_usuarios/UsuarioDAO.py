from Conexion import Conexion
from Usuario import Usuario
from CursorDelPool import CursorPool
from logger_base import log

class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY usu_id'
    _INSERTAR = 'INSERT INTO usuarios(usu_username, usu_password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuarios SET usu_username = %s, usu_password = %s WHERE usu_id = %s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE usu_id = %s'

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                persona = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(persona)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            cursor.execute(cls._INSERTAR, (usuario.getUsername, usuario.getPassword))
            log.debug('Insercion exitosa')

    @classmethod
    def revisarId(cls, id):
        with CursorPool() as cursor:
            n = 0
            x = None
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            for registro in registros:
                if id != registro[0]:
                    continue
                else:
                    n = 1
                    break
            if n == 0:
                log.debug('Usuario no encontrado')
                x = 0
            else:
                log.debug(f'Usuario encontrado')
                x = 1
            return x


    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.getUsername, usuario.getPassword, usuario.getId_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug('Actualizacion completa')

    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            cursor.execute(cls._ELIMINAR, (usuario.getId_usuario,))
            log.debug('Eliminar completado')

if __name__ == '__main__':

    personas = UsuarioDao.seleccionar()
    for persona in personas:
        print(persona)
