
class producto:
    def __init__(self, nombre, precio, precios_cuidados = False, productos_primera_necesidad = False, descuento = False):
        self.nombre = nombre
        self.precio = precio
        self.precios_cuidados = precios_cuidados
        self.primera_nec = productos_primera_necesidad
        self.descuento = descuento

            
    def  __str__(self):
        return f'Nombre: {self.nombre}, precio: {self.precio}, precios cuidados: {("SI" if self.precios_cuidados else "NO")}, producto primera necesidad: {("SI" if self.primera_nec else "NO")}'


class superMercado:
    def __init__(self, nombre, direccion, lista_productos):
        self.nombre, self.direccion, self.lista_productos = nombre, direccion, lista_productos
  
class Menu_productos(superMercado):
    
    # descuento por prod primera necesidad
    descuento_primeraNecesidad = 0.1
    lista_precios = []
    
    def __init__(self, nombre, direccion, lista_productos):
        super().__init__(nombre, direccion, lista_productos)

          

    def ver_menu(self):
        print(f'\nMENU SUPERMERCADO {self.nombre}\n')
        for e, p in enumerate(self.lista_productos):
            print(e+1, p)
            print(f'Tiene descuento precios cuidados: %{self.descuento_primeraNecesidad*100}' if p.primera_nec else 'No tiene descuentos por precios cuidados' )
            print(f'Tiene descuento adicional: %{p.descuento*100}' if p.descuento else 'No tiene descuentos adicionales' )
            print(f'PRECIO FINAL: {p.precio-((p.precio*(p.descuento if p.descuento else 0))+(p.precio*(self.descuento_primeraNecesidad if p.primera_nec else 0)))}\n')
            self.lista_precios.append([f'{p.nombre}:', p.precio-((p.precio*(p.descuento if p.descuento else 0))+(p.precio*(self.descuento_primeraNecesidad if p.primera_nec else 0)))])

    def mostrar_listaPrecios(self):
        print('Lista de precios con descuentos: ')
        for i, lista in enumerate(self.lista_precios):
            print(i+1, ' '.join(map(str, lista)))

    def mostrar_precio_total_mercaderia(self):
        return print('El precio total de la mercaderia es: $', sum([x for x in self.lista_precios for x in x if type(x) == float or type(x) == int]))
        

class cliente:
    
    lista_compra = []

    def __init__(self, lista_precios, opcion = None, valor_compra_total = 0):
        self.lista_precios = lista_precios
        self.opcion = opcion
        self.valor_compra_total= valor_compra_total
    def eleccion(self):
        
        self.valor_compra_total += [x for x in self.lista_precios][self.opcion][1]
        self.lista_compra.append("".join(map(str, self.lista_precios[self.opcion])))
        # print([x for x in Menu.lista_precios][self.opcion][0],'$', [x for x in Menu.lista_precios][self.opcion][1])

    def compra_total(self):
        print(f'La lista de compras: \n')
        for i, p in enumerate(self.lista_compra):
            print(f'{i+1}: {p}')
        print(f'\nel valor de la compra total es: ${self.valor_compra_total}')



    