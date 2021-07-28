"""
Un supermercado maneja el catálogo de los productos que vende. 
De cada producto se conoce su nombre, precio, y si el mismo es parte del programa Precios Cuidados o no. Por defecto, el producto no es parte del programa, a menos que se especifique lo contrario.

Para ayudar a los clientes, el supermercado quiere realizar 
descuentos en productos de Primera Necesidad. Es por eso que al calcular el precio de un producto de Primera Necesidad, se aplica un descuento del 10%. Es decir:

precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9

El supermercado, del cual se conoce el nombre y la dirección, desea conocer la 
cantidad total de productos que comercializa y la suma total de los precios de los mismos.

Implementar un programa en Python que resuelva este requerimiento.
Suponga ahora que el descuento a aplicar en cada producto de primera necesidad puede ser distinto y se debe poder definir al momento de crear el mismo. Por ejemplo, el arroz puede ser un producto de primera necesidad con un descuento del 8%, mientras que leche podría ser otro producto de primera necesidad con un decuento del 11%. Esto es sólo un ejemplo. El descuento a aplicar en cada producto de primera necesidad debe ser configurable al momento de crearlo.

Implementar un programa en Python basado en el anterior que ahora incorpore este nuevo requerimiento."""



from clases import producto, Menu_productos, cliente

while True:

    p1 = producto(nombre='cigarrillo', precio= 120)
    p2 = producto(nombre='shampoo', precio = 100, precios_cuidados= True)
    p3 = producto(nombre='cerveza', precio=120, productos_primera_necesidad=True)
    p4 = producto(nombre='frutilla', precio=120, descuento=0.2)
    Menu = Menu_productos(nombre='"CAREFURE"', direccion= 'av. Avalos N° 899', lista_productos=[p1, p2, p3, p4])
    clien = cliente(lista_precios= Menu.lista_precios)

    print('opciones:\n\t1. Ver menu de mercaderias \n\t2. Mostrar Listas de Precios:\n\t3. Mostrar precio total de la mercaderia del super \n\t4. Hacer compra \n\t5. salir')

    opcion = input('')
    if opcion == '1':
        Menu.ver_menu()
    elif opcion == '2':
        Menu.mostrar_listaPrecios()
    elif opcion == '3':
        Menu.mostrar_precio_total_mercaderia()

    elif opcion == '4':
        while True:
            opcion_cliente = input('Elegir opcion: \n\t1. Realizar compra\n\t2. Ver productos comprados\n\t3. Salir\n')
            if opcion_cliente == '1':
                Menu.mostrar_listaPrecios()
                op = int(input('Elija Producto: '))
                clien.opcion = op-1
                clien.eleccion()
            elif opcion_cliente == '2':
                clien.compra_total()
            elif opcion_cliente == '3':
                break
            else: print('elija una opcion valida')
    elif opcion == '5':
        print('Gracias vuelva pronto')
        break
    else: print('Elija una opcion valida')

