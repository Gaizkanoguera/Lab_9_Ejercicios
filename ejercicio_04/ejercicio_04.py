"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    if codigos[medio] == objetivo:
        return medio
    elif codigos[medio] > objetivo:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)
    else:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
# Respuesta: 
#   1. Cuando se encuentra el objetivo (caso exitoso: codigos[medio] == objetivo).
#   2. Cuando el rango de búsqueda se invalida (caso fallido: izquierda > derecha).
#
# 2. ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
# Respuesta: 
#   Porque la posición central (medio) ya fue evaluada. Volver a incluirla es 
#   redundante y provocaría un bucle/recursión infinita cuando izquierda == derecha.
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
#    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |     0     |    6    |   3   | 415 > 300 -> ir a la izquierda (derecha = 2)
#       2    |     0     |    2    |   1   | 205 < 300 -> ir a la derecha (izquierda = 2)
#       3    |     2     |    2    |   2   | 310 > 300 -> ir a la izquierda (derecha = 1)
#       4    |     2     |    1    |   —   | 2 > 1 -> caso base, retornar -1
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de
#    contar_desde_limite()?
# Respuesta:
#   contar_desde_limite() avanza de forma lineal reduciendo el problema en 1 en cada paso (O(n)).
#   buscar_codigo() avanza de forma logarítmica dividiendo el tamaño del problema a la mitad en cada paso (O(log n)).
#

if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0