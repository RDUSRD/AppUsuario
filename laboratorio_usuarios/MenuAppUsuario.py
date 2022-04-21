from UsuarioDAO import UsuarioDao
from Usuario import Usuario

N = 0
opcion = None

print(f'Bienvenido al menu de usuario'.center(50,'-'))

while N == 0:
    print('''
          Menu:
            1) Listar Usuarios
            2) Agregar Usuario
            3) Actualizar usuario
            4) Eliminar usuario
            5) Salir
            ''')
    opcion = int(input('Coloque su opcion: '))

    if opcion == 1:
        print('Imprimiendo usuarios:\n')
        personas = UsuarioDao.seleccionar()
        for persona in personas:
            print(persona)
        print('Volviendo al menu...')

    elif opcion == 2:
        username = input('Indique el username del nuevo usuario: ')
        password = input('Indique la password del nuevo usuario: ')

        persona = Usuario(username = username, password = password)

        UsuarioDao.insertar(persona)
    elif opcion == 3:
        Id = int(input('Indique el id del usuario a actualizar: '))

        persona = Usuario(id_usuario = Id)

        x = UsuarioDao.revisarId(persona.getId_usuario)

        if x == 0:
            print('Usuario no encontrado, volviendo al menu...')
        else:
            username = input('Indique el nuevo username:  ')
            password = input('Indique el nuevo password: ')

            persona = Usuario(id_usuario=Id, username=username, password=password)

            UsuarioDao.actualizar(persona)

    elif opcion == 4:
        Id = int(input('Digite el id del usuario a eliminar: '))

        persona = Usuario(id_usuario = Id)

        UsuarioDao.eliminar(persona)
    elif opcion == 5:
        N = 1
        print('Saliendo... ')

    else:
        print('No existe tal opcion, volviendo al menu\n')