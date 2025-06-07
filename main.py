from recetas.recetas import pedir_datos, calcular_ingredientes, mostrar_resultados

def principal():
    """
    Función principal que coordina el flujo del programa para calcular ingredientes
    de una receta según el número de porciones.
    """
    # Solicita al usuario el número de porciones deseado
    porciones = pedir_datos()

    # Calcula la cantidad de ingredientes necesarios
    ingredientes = calcular_ingredientes(porciones)

    # Muestra el resultado al usuario
    mostrar_resultados(porciones, ingredientes)

if __name__ == "__main__":
    # Puedes descomentar la siguiente línea si deseas ejecutar pruebas automáticamente
    # import pytest; pytest.main()
    
    principal()

