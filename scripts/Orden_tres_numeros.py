"""
===========================================
 Ordenamiento de Tres Números (Descendente)
===========================================

Autor      : Néstor O. Vásquez C.
Proyecto   : DATA-ANALYTICS
Versión    : 1.0
Fecha      : 08/07/2025

Descripción:
    Este script recibe tres números enteros ingresados por el usuario y los ordena
    de mayor a menor utilizando estructuras condicionales anidadas. El resultado
    se muestra en consola indicando el orden descendente correspondiente.

Entradas:
    - A : Primer número entero
    - B : Segundo número entero
    - C : Tercer número entero

Salidas:
    - Impresión en consola del orden descendente de los tres números

Restricciones:
    - No se permite el uso de funciones de ordenamiento automático como `sort()`.

Uso:
    python ordenamiento_condicional.py
"""

# Solicitar los tres valores al usuario
A = int(input("Ingrese el primer número: "))
B = int(input("Ingrese el segundo número: "))
C = int(input("Ingrese el tercer número: "))

# Evaluar los casos para ordenar de mayor a menor
if A > B:
    if B > C:
        # Caso: A > B > C
        print('1. El orden es:', A, B, C)
    else:
        if A > C:
            # Caso: A > C > B
            print('2. El orden es:', A, C, B)
        else:
            # Caso: C > A > B
            print('3. El orden es:', C, A, B)
else:
    if B > C:
        if A > C:
            # Caso: B > A > C
            print('4. El orden es:', B, A, C)
        else:
            # Caso: B > C > A
            print('5. El orden es:', B, C, A)
    else:
        # Caso: C > B > A
        print('6. El orden es:', C, B, A)