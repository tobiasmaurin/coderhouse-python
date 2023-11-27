#PRIMER ENTREGABLE

base_de_datos = {}
def registro():
    print('REGISTRARSE')
    registro_ususario = input("Ingrese un nombre de usuario: ")
    registro_contrasena = input("ingrese una contraseña: ")
    base_de_datos [registro_ususario] = registro_contrasena
    print(f'Felicidades {registro_ususario}! Registro exitoso!')
registro()




def login():
    print('INICIAR SESION')
    usuario = input('Nombre de usuario: ')
    contrasena = input('Contraseña: ')
    while True:
        if usuario not in base_de_datos:
            print('Nombre de usuario o Contraseña incorrecta, intente nuevamente')
            usuario = input('Nombre de usuario: ')
            contrasena = input('Contraseña: ')
        elif contrasena != base_de_datos.get(usuario):
            print('Nombre de usuario o Contraseña incorrecta, intente nuevamente')
            usuario = input('Nombre de usuario: ')
            contrasena = input('Contraseña:')
        else:
            print(f'Bienvenido {usuario}!')
            break
login()



    