"""
Ejercicio 5. Extraer valores de una estructura anidada

Un sistema recibe mediciones agrupadas en listas que pueden contener otras
listas, con distintos niveles de profundidad.

    def extraer_valores(datos):
        pass

La función devuelve una nueva lista plana con todos los números, en el orden en
que aparecen de izquierda a derecha. Las entradas contienen únicamente números
y listas, y no tienen referencias cíclicas.

Ejemplos

    extraer_valores([10, [20, 30], 40])     # [10, 20, 30, 40]
    extraer_valores([1, [2, [], [3]], 4])   # [1, 2, 3, 4]
    extraer_valores([[], [[], []]])         # []
    extraer_valores([])                     # []

Requisitos

- Utiliza un ciclo para recorrer los elementos del nivel actual.
- Si encuentras un número, incorpóralo al resultado.
- Si encuentras una lista, procésala mediante una llamada recursiva.
- Puedes utilizar append() y extend().
- No utilices cortes.
- No modifiques la estructura original.
- No dejes sublistas dentro del resultado.
"""


def extraer_valores(datos):
    resultado = []
    for dato in datos:
        if isinstance(dato, list):
            resultado.extend(extraer_valores(dato))
        else:
            resultado.append(dato)
    
    return resultado
pass 


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Qué devuelve la función cuando recibe una lista vacía?
# Una lista vacía.
#
# 2. ¿Qué diferencia hay entre incorporar un número e incorporar el
#    resultado de una llamada recursiva?
# Al incorporar un número, se agrega directamente a la lista de resultados. Al incorporar el resultado de una llamada recursiva, se extiende la lista de resultados con los elementos devueltos por la llamada recursiva.
#
# 3. Dibuja únicamente las llamadas a extraer_valores() para
#    [1, [2, [], [1]], 4]. ¿Cuántas llamadas se realizan, incluyendo las
#    de listas vacías?
# extraer_valores([1, [2, [], [1]], 4])
# extraer_valores([2, [], [1]])
# extraer_valores([])
# extraer_valores([1])
# Total de llamadas: 4
#
# 4. ¿Por qué cada llamada necesita su propia lista de resultados?
# Cada llamada necesita su propia lista de resultados para mantener la independencia de los resultados de cada nivel de profundidad. Si todas las llamadas compartieran la misma lista, se mezclarían los resultados y no se podría mantener el orden correcto de los elementos extraídos.
#


if __name__ == "__main__":
    print(extraer_valores([10, [20, 30], 40]))     # [10, 20, 30, 40]
    print(extraer_valores([1, [2, [], [3]], 4]))   # [1, 2, 3, 4]
    print(extraer_valores([[], [[], []]]))         # []
    print(extraer_valores([]))                     # []
