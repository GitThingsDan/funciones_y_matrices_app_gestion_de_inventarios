from clases.marcas import Marcas

class Modelos(Marcas):
    def __init__(self, id_modelo = 0, nom_modelo ='', precio = 0, cantidad = 0, genero ='', talla = 0, id_marca = 0):
        super.__init__(id_marca)
        self.id_modelo = id_modelo
        self.nom_modelo = nom_modelo
        self.precio = precio
        self.cantidad = cantidad
        self.genero = genero
        self.talla = talla