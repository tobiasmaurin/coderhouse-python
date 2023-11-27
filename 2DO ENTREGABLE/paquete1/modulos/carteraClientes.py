#2DO ENTREGABLE

class clientes():

    def __init__(self, nombre, edad, mail, interes):
        self.nombre = nombre
        self.edad = edad
        self.mail = mail
        self.interes = interes


    def __str__(self):
        return 'El cliente '+ self.nombre +' fue registrado en la base de datos'
    

    def elegir(self, producto, marca):
        self.producto = producto
        self.marca = marca
        print('El cliente '+ self.nombre +' eligió un/a '+ self.producto +' marca '+ self.marca + ' y se agregó al carrito exitosamente.')

    def pagar(self, forma_de_pago):
        self.forma_de_pago = forma_de_pago
        print('El pago fue realizado con '+ self.forma_de_pago)
        while True:
            print('Pago exitoso')
            break

    