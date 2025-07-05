# script_noc_v1.py
# -----------------------------
# Proyecto: NOC IBM
# Versión: 1.1
# Autor: Néstor Vásquez
# Fecha: 2025-07-05
# ----------------------------


def ordenamiento(a,b,c):
    if a >= b and b >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

m = ordenamiento(10,2,80)
print(f'El número mayor es:', m)