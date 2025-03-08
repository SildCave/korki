

owoce = ["japko", "grużka", "banan", "pomarańcza", "japko"]

print(owoce[2])

print('\n\n')

owoce = {"japko", "gyrużyka", "pomarancza"}

print('set:')
print(owoce)

owoce = {"japko", "gyrużyka", "pomarancza", "japko"}

print('set:')
print(owoce)


liczby = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6]

szukana = 4
znaleziona = False
for liczba in liczby:
    if liczba == szukana:
        znaleziona = True
        break

znaleziona = (szukana in liczby)
print(f"znaleziona: {znaleziona}")

liczby_nie_powtarzajace = set(liczby)
print('liczby_nie_powtarzajace:')
print(liczby_nie_powtarzajace)

# print(liczby_nie_powtarzajace[1]) # tak nie mozna

szukana = 4
znaleziona = (szukana in liczby_nie_powtarzajace)

print(f"znaleziona: {znaleziona}")

liczby = set([1, 2, 3, 4, 5, 6, 6, 6, 6, 6]) # 1, 2, 3, 4, 5, 6

liczby.add(10)

print(f"liczby: {liczby}") # 1, 2, 3, 4, 5, 6, 10

nowe_liczby = [40, 80, 55]
liczby.update(nowe_liczby)

print(f"liczby: {liczby}")

liczby.remove(10)
print(f"liczby: {liczby}")

# wazne
# liczby.remove(10) <= gad sie zesra

liczby.discard(40)
liczby.discard(40)

print(f"liczby: {liczby}")


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B) # <= SUMA

print(A & B) # <= CZ WSP

print(A - B) # <= RONICA

print(A ^ B) # <= wywala wspolne


zdanie = 'Ala ma kota , kota ma Ala'

words = set(zdanie.split())

print(f"words: {words}")

# deklaracja pustego

nowy_set = set([])
