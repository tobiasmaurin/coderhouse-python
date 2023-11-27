

nombre = input("Registre nombre de usuario: ")
contrasenia= input("Registre contraseña de usuario: ")

dato_usu={nombre : contrasenia}

def login():
  while True:
    usuario= input("Ingrese usuario: ")
    clave_u = input("Ingrese contraseña: ")

    if (usuario == nombre) and (clave_u == contrasenia):
      print("Bienvenido!")
      break

    else:
      print("Usuario o contraseña incorrecta. Vuelve a intentarlo!")

login()


def informacion():
  print("La informacion almacenada en el login es la siguiente: ")
  for clave, valor in dato_usu.items():
    print(clave, valor)

informacion()