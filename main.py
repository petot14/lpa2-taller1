<<<<<<< HEAD
from recetas.recetas import pedir_datos, calcular_ingredientes, mostrar_resultados
=======
from recetas.recetas import *
>>>>>>> efcec4979a40ca8a37669e20aeae337a30064dfd

def principal():
    """
    Función principal que coordina el flujo del programa para calcular ingredientes
    de una receta según el número de porciones.
    """
    # Solicita al usuario el número de porciones deseado
    porciones = pedir_datos()
<<<<<<< HEAD

    # Calcula la cantidad de ingredientes necesarios
    ingredientes = calcular_ingredientes(porciones)

    # Muestra el resultado al usuario
    mostrar_resultados(porciones, ingredientes)

if __name__ == "__main__":
    # Puedes descomentar la siguiente línea si deseas ejecutar pruebas automáticamente
    # import pytest; pytest.main()
    
=======
    
    # Calcula la cantidad de ingredientes necesarios para las porciones especificadas
    ingredientes = calcular_ingredientes(porciones)
    
    # Muestra al usuario los resultados del cálculo
    mostrar_resultados(porciones, ingredientes)

# Verifica si este script se está ejecutando directamente (no importado como módulo)
if __name__ == "__main__":
    # Importa pytest para ejecutar pruebas unitarias
    # import pytest
    # Ejecuta pruebas automatizadas para verificar el funcionamiento del programa
    # pytest.main()
    
    # Ejecuta la función principal del programa
>>>>>>> efcec4979a40ca8a37669e20aeae337a30064dfd
    principal()

