def imprimir_ingredientes(postres, nombre_postre):
    for postre, ingredientes in postres:
        if postre == nombre_postre:
            print(f'Ingredientes de {postre}: {ingredientes}')
            return
    print(f'El postre {nombre_postre} no existe.')

def insertar_ingredientes(postres, nombre_postre, nuevos_ingredientes):
    for postre, ingredientes in postres:
        if postre == nombre_postre:
            ingredientes.extend(nuevos_ingredientes)
            print(f'Se han agregado nuevos ingredientes a {postre}.')
            return
    print(f'El postre {nombre_postre} no existe.')

def eliminar_ingredientes(postres, nombre_postre, ingredientes_a_eliminar):
    for postre, ingredientes in postres:
        if postre == nombre_postre:
            for ingrediente in ingredientes_a_eliminar:
                if ingrediente in ingredientes:
                    ingredientes.remove(ingrediente)
            print(f'Se han eliminado ingredientes de {postre}.')
            return
    print(f'El postre {nombre_postre} no existe.')

def dar_alta_postre(postres, nombre_postre, ingredientes):
    for postre, _ in postres:
        if postre == nombre_postre:
            print(f'El postre {nombre_postre} ya existe.')
            return
    postres.append((nombre_postre, ingredientes))
    print(f'Se ha dado de alta el postre {nombre_postre} con sus ingredientes.')

def dar_baja_postre(postres, nombre_postre):
    for postre, _ in postres:
        if postre == nombre_postre:
            postres.remove((postre, _))
            print(f'Se ha dado de baja el postre {nombre_postre}.')
            return
    print(f'El postre {nombre_postre} no existe.')

def eliminar_elementos_repetidos(postres):
    postres_sin_repetidos = []
    for postre, ingredientes in postres:
        if (postre, ingredientes) not in postres_sin_repetidos:
            postres_sin_repetidos.append((postre, ingredientes))
    return postres_sin_repetidos

# Estructura de datos POSTRES
POSTRES = [("Tarta de Manzana", ["manzanas", "harina", "azúcar", "mantequilla"]),
           ("Tarta de Fresa", ["fresas", "harina", "azúcar", "crema"]),
           ("Helado de Vainilla", ["leche", "crema", "azúcar", "vainilla"])]

# Ejemplos de uso
print("--- Ejemplos de uso ---")
imprimir_ingredientes(POSTRES, "Tarta de Manzana")
insertar_ingredientes(POSTRES, "Tarta de Manzana", ["canela", "limón"])
eliminar_ingredientes(POSTRES, "Tarta de Manzana", ["limón", "azúcar"])
dar_alta_postre(POSTRES, "Tiramisú", ["café", "bizcochos", "crema mascarpone"])
dar_baja_postre(POSTRES, "Tarta de Fresa")

# Eliminar elementos repetidos
POSTRES = eliminar_elementos_repetidos(POSTRES)
print("--- POSTRES sin elementos repetidos ---")
print(POSTRES)