from clases.modelos import Modelos

class TipoCalzados(Modelos):
    def __init__(self, id_tipo_calzado = 0, nom_tipo_calzado ='', id_modelo= 0):
        super.__init__(id_modelo)
        self.id_tipo_calzado = id_tipo_calzado
        self.nom_tipo_calzado = nom_tipo_calzado
        