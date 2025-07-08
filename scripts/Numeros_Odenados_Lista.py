"""
Programa: Ordenar números de mayor a menor, se organizan dentro de una lista
Autor: Néstor Oswaldo Vásquez Castro
Fecha: 7 de julio de 2025
Descripción:
    Este script solicita al usuario tres valores numéricos enteros,
    los almacena en una lista y los ordena en orden descendente (de mayor a menor).
"""

def obtener_numeros():
    """
    Solicita al usuario tres números enteros mediante la consola.

    Returns:
        list: Lista de tres números enteros ingresados por el usuario.
    """
    A = int(input('Ingrese el valor 1: '))
    B = int(input('Ingrese el valor 2: '))
    C = int(input('Ingrese el valor 3: '))
    return [A, B, C]

def ordenar_descendente(lista):
    """
    Ordena una lista de números en orden descendente (mayor a menor).

    Args:
        lista (list): Lista de números a ordenar.

    Returns:
        list: Lista ordenada de mayor a menor.
    """
    lista.sort(reverse=True)
    return lista

def main():
    """
    Función principal del programa.
    """
    numeros = obtener_numeros()
    numeros_ordenados = ordenar_descendente(numeros)
    print("Números ordenados de mayor a menor:", numeros_ordenados)

if __name__ == "__main__":
    main()
