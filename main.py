#1. Feladat
#Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!

import random

lista = [random.randint(1, 10) for i in range(5) ]

paroslista = [i for i in lista if i % 2 == 0]


print(f"A mennyi szám van a listában:{len(paroslista)} és a páros számok: {paroslista}")

#2.1 Feladat
#A program számolja össze, hogy hány darab 'A' vagy 'a' betűvel kezdődő szó van a szavak listában.
#A képernyőre írja is ki a feltételnek megfelelő szavakat!
#szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

as_szavak = [szo for szo in szavak if szo[0] in {"a", "A"}]
print(len(as_szavak))
print(as_szavak)

#2.2 Feladat
#A program számolja össze, hogy hány darab 'E' vagy 'e' betűt tartalmazó szó van a szavak listában. 
#A képernyőre írja is ki a feltételnek megfelelő szavakat!

szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

es_szavak = [szo for szo in szavak if "e" in szo or "E" in szo]
print(len(es_szavak))
print(es_szavak)