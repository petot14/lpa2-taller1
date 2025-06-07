# R1: pedir el número de porciones
def pedir_datos():
<<<<<<< HEAD
    """
    Solicita al usuario que ingrese un número de porciones.
    Valida que sea múltiplo de 4 y mayor o igual a cero.
    """
    while True:
        try:
            porciones = int(input("Ingrese el número de porciones (múltiplo de 4): "))
            if porciones >= 0 and porciones % 4 == 0:
                return porciones
            else:
                print(" El número debe ser un múltiplo de 4 y mayor o igual a 0.")
        except ValueError:
            print(" Entrada inválida. Ingrese un número entero.")


# R2: calcular la cantidad de los ingredientes
def calcular_ingredientes(porciones):
    """
    Calcula la cantidad necesaria de ingredientes para la cantidad de porciones dadas.
    Retorna una tupla: (arroz_g, leche_l, azucar_g, leche_condensada_g)
    """
    if porciones <= 0 or porciones % 4 != 0:
        return (0, 0, 0, 0)
    
    factor = porciones / 8  # Proporción respecto a 8 porciones base
    arroz = 450 * factor
    leche = 2 * factor
    azucar = 200 * factor
    leche_condensada = 400 * factor

    return (arroz, leche, azucar, leche_condensada)


# R3: mostrar los ingredientes necesarios
def mostrar_resultados(porciones, ingredientes):
    """
    Muestra los resultados en consola con unidades de medida.
    """
    arroz, leche, azucar, leche_condensada = ingredientes

    print("\n Ingredientes necesarios")
    print(f" Porciones: {porciones}")
    print(f" Arroz: {arroz:.2f} gramos")
    print(f" Leche: {leche:.2f} litros")
    print(f" Azúcar: {azucar:.2f} gramos")
    print(f" Leche condensada: {leche_condensada:.2f} gramos")
=======
    return -1
  

# R2: calcular la cantidad de los ingredientes
def calcular_ingredientes(porciones):
    return (1.0, 1.0, 1.0, 1.0)


# R3: mostrar los ingredientes necesarios
def mostrar_resultados (porciones, ingredientes):
    print("ok")

>>>>>>> efcec4979a40ca8a37669e20aeae337a30064dfd
