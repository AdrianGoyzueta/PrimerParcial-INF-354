from kanren import Relation, facts, run, conde, var
from kanren.constraints import neq

familia = [
  ("David", "Gonzalo"), ("Teresa G", "Gonzalo"),
  ("David", "Abel"), ("Teresa G", "Abel"),
  ("David", "Chaly"), ("Teresa G", "Chaly"),
  ("David", "Omar"), ("Teresa G", "Omar"),
  ("David", "Carla"), ("Teresa G", "Carla"),
  ("Gonzalo", "Gustabo"), ("Miriam", "Gustabo"),
  ("Gonzalo", "Marcelo"), ("Miriam", "Marcelo"),
  ("Gonzalo", "Marco"), ("Miriam", "Marco"),
  ("Abel", "Gisela"), ("Claudia M", "Gisela"),
  ("Abel", "Adrian"), ("Claudia M", "Adrian"),
  ("Abel", "Matheo"), ("Claudia M", "Matheo"),
  ("Chaly", "Gianina"), ("Rosmery", "Gianina"),
  ("Omar", "Alejandro"), ("Claudia T", "Alejandro"),
  ("Omar", "Gabriel"), ("Claudia T", "Gabriel"),
  ("Carla", "Cecilia"), ("Samy", "Cecilia"),
  ("Carla", "Camila"), ("Samy", "Camila"),
  ("Arturo", "Horacio"), ("Teresa C", "Horacio"),
  ("Arturo", "Claudia M"), ("Teresa C", "Claudia M"),
  ("Arturo", "Jorge"), ("Ana Maria", "Jorge"),
  ("Arturo", "Daniel"), ("Ana Maria", "Daniel"),
  ("Jorge", "Luciana"), ("Raquel", "Luciana"),
  ("Jorge", "Adriana"), ("Raquel", "Adriana"),
  ("Jorge", "Natalia"), ("Raquel", "Natalia"),
]


papa = Relation()
mama = Relation()


facts(papa, *familia[::2])
facts(mama, *familia[1::2])


def abuelos(abuelo, nieto):
  padre = var()
  return conde((papa(abuelo, padre), papa(padre, nieto)), (papa(abuelo, padre), mama(padre, nieto)))


def abuelas(abuela, nieto):
  padre = var()
  return conde((mama(abuela, padre), papa(padre, nieto)), (mama(abuela, padre), mama(padre, nieto)))


def padres(padre, hijo):
  return conde((papa(padre, hijo),) , (mama(padre, hijo),))


def hermanos(hermano, hijo):
  padre = var()
  return conde((padres(padre, hermano), papa(padre, hijo), neq(hermano, hijo)))


def tios(tio, sobrino):
  padre = var()
  return conde((hermanos(padre, tio), padres(padre, sobrino)))


def primos(primo, hijo):
  padre = var()
  return conde((tios(padre, primo), padres(padre, hijo)))


def tios2(tio, sobrino):
  primo = var()
  return conde((padres(tio, primo), primos(primo, sobrino)))


x = var()
print("Abuelos de Adrian:", run(0, x, abuelos(x, "Adrian")))
print("Abuelas de Adrian:", run(0, x, abuelas(x, "Adrian")))
print("Padres de Adrian:", run(0, x, padres(x, "Adrian")))
print("Hermanos de Adrian:", set(run(0, x, hermanos(x, "Adrian"))))
print("Tios de Adrian:", set(run(0, x, tios(x, "Adrian"))))
print("Primos de Adrian:", set(run(0, x, primos(x, "Adrian"))))
print("Tios de Adrian:", set(run(0, x, tios2(x, "Adrian"))))
