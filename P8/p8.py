def combinaciones(distancias, actual, visitados):
  if len(visitados) == len(distancias): 
    if distancias[visitados[-1]][visitados[0]] is not None:
      print(f"{visitados}: {sum(distancias[visitados[i]][visitados[(i+1) % len(visitados)]] for i in range(len(visitados)))}")
    return
  for i in range(len(distancias)):
    if distancias[actual][i] is not None and i not in visitados:
      combinaciones(distancias, i, [*visitados, i])


distancias = [
  [None, 20, 10, 30, None, None, None, None],
  [20, None, None, None, 15, None, None, None],
  [10, None, None, 25, None, None, None, None],
  [30, None, 25, None, None, 35, None, None],
  [None, 15, None, None, None, 40, 45, None],
  [None, None, None, 35, 40, None, None, 50],
  [None, None, None, None, 45, None, None, 55],
  [None, None, None, None, None, 50, 55, None]
]

print("No todos los nodos estan conectados")

for i in range(len(distancias)):
  combinaciones(distancias, i, [i])

print("Todos los nodos estan conectados")

distancias = [
  [0, 1, 2, 3, 4, 5, 6, 7],
  [1, 0, 8, 9, 10, 11, 12, 13],
  [2, 8, 0, 14, 15, 16, 17, 18],
  [3, 9, 14, 0, 19, 20, 21, 22],
  [4, 10, 15, 19, 0, 23, 24, 25],
  [5, 11, 16, 20, 23, 0, 26, 27],
  [6, 12, 17, 21, 24, 26, 0, 28],
  [7, 13, 18, 22, 25, 27, 28, 0]
]

for i in range(len(distancias)):
  combinaciones(distancias, i, [i])
