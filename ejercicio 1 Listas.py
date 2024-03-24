class PostresManager:
    def __init__(self):
        self.postres = {}

    def imprimir_ingredientes(self, nombre_postre):
        if nombre_postre in self.postres:
            print(f'Ingredientes de {nombre_postre}: {self.postres[nombre_postre]}')
        else:
            print(f'El postre {nombre_postre} no existe.')

    def agregar_ingredientes(self, nombre_postre, nuevos_ingredientes):
        if nombre_postre in self.postres:
            self.postres[nombre_postre].extend(nuevos_ingredientes)
            print(f'Se han agregado nuevos ingredientes a {nombre_postre}.')
        else:
            print(f'El postre {nombre_postre} no existe.')

    def eliminar_ingredientes(self, nombre_postre, ingredientes_a_eliminar):
        if nombre_postre in self.postres:
            for ingrediente in ingredientes_a_eliminar:
                if ingrediente in self.postres[nombre_postre]:
                    self.postres[nombre_postre].remove(ingrediente)
            print(f'Se han eliminado ingredientes de {nombre_postre}.')
        else:
            print(f'El postre {nombre_postre} no existe.')

    def dar_alta_postre(self, nombre_postre, ingredientes):
        if nombre_postre not in self.postres:
            self.postres[nombre_postre] = ingredientes
            print(f'Se ha dado de alta el postre {nombre_postre} con sus ingredientes.')
        else:
            print(f'El postre {nombre_postre} ya existe.')

    def dar_baja_postre(self, nombre_postre):
        if nombre_postre in self.postres:
            del self.postres[nombre_postre]
            print(f'Se ha dado de baja el postre {nombre_postre}.')
        else:
            print(f'El postre {nombre_postre} no existe.')


# Ejemplo de uso
pm = PostresManager()

# Dar de alta un postre
pm.dar_alta_postre("Tarta de Manzana", ["manzanas", "harina", "azúcar", "mantequilla"])

# Imprimir ingredientes de un postre
pm.imprimir_ingredientes("Tarta de Manzana")

# Agregar nuevos ingredientes a un postre
pm.agregar_ingredientes("Tarta de Manzana", ["canela", "limón"])

# Imprimir ingredientes de un postre después de agregar nuevos ingredientes
pm.imprimir_ingredientes("Tarta de Manzana")

# Eliminar ingredientes de un postre
pm.eliminar_ingredientes("Tarta de Manzana", ["limón", "azúcar"])

# Imprimir ingredientes de un postre después de eliminar ingredientes
pm.imprimir_ingredientes("Tarta de Manzana")

# Dar de baja un postre
pm.dar_baja_postre("Tarta de Manzana")

# Intentar imprimir ingredientes de un postre dado de baja
pm.imprimir_ingredientes("Tarta de Manzana")