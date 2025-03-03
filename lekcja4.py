# mega wazne

kolory = ["czarny", "biały"]
print(f"kolory: {kolory}") # kolory: ['czarny', 'biały']

kolory.append('zielony')
print(f"kolory: {kolory}") # kolory: ['czarny', 'biały', 'zielony']

kolory.insert(1, 'niebieski')
print(f"kolory: {kolory}") # kolory: ['czarny', 'niebieski', 'biały', 'zielony']

kolory.remove('czarny')
print(f"kolory: {kolory}") # kolory: ['niebieski', 'biały', 'zielony']

kolory.pop()
print(f"kolory: {kolory}") # kolory: ['niebieski', 'biały']

kolory.append('czerwony') # kolory: ['niebieski', 'biały', 'czerwony']

kolory.pop(1)
print(f"kolory: {kolory}") # kolory: ['niebieski', 'czerwony']

del kolory[1]
print(f"kolory: {kolory}")

liczba = 100
print(liczba)


liczby = [4, 1, 7, 3, 99]
print(f"lista: {liczby}")
print(f"max: {max(liczby)}")
print(f"min: {min(liczby)}")

liczby.sort()
liczby.reverse()
print(f"rev sort: {liczby}")

print('\n\n\n')

liczby = [4, 1, 7, 3, 99]

for liczba in liczby:
    print(f"liczba: {liczba}")

print('\n\n\n')

kolory = ["czarny", "biały", "zielony", "czerwony"]
kolory.sort()
kolory.reverse()
for kolor in kolory:
    print(f"kolor: {kolor}")

print('\n\n\n')


word = "Karol"
for char in word:
    print(f"char: {char}")

print('\n\n\n')


# naiwna impl
numery = [1, 2, 3, 4, 5, 6]
for num in numery:
    print(f"num: {num}")

#                      <   )
#                      range(a, b)
#                      od a do b-1
od_1_do_6 = list(range(1, 7))
print(f"od_1_do_6: {od_1_do_6}")


#       od 0 do n-1
cos = list(range(6))
print(f"cos: {cos}")

parzyste_od_2_do_8 = list(range(2, 8 + 1, 2))
print(f"parzyste_od_2_do_8: {parzyste_od_2_do_8}")


print('\n\n\n')


kolory = ["czarny", "biały", "zielony", "czerwony"]


for i in range(len(kolory)):
    print(kolory[i])


print('\n\n\n')


kolory = ["czarny", "biały", "zielony", "czerwony"]
lubialność = [0.5, 0.9, 0.8, 0.8]

for index, kolor in enumerate(kolory):
    print(f"index: {index}")
    print(f"kolor: {kolor}, lubialność: {lubialność[index]}\n")

print('\n\n\n')


kolory = ["czarny", "biały", "zielony", "czerwony"]
lubialność = [0.5, 0.9, 0.8, 0.8]

for kolor, lubialność in zip(kolory, lubialność):
    print(f"kolor: {kolor}, lubialność: {lubialność}\n")


szukana_liczba = 20
liczby = [1, 6, 8, 18, 19, 20, 100, 55, 64]

print(f"liczby: {liczby}\nszukana: {szukana_liczba}")

for liczba in liczby:
    print(f"liczba: {liczba}")
    if liczba == szukana_liczba:
        print("znaleziona")
        break


print('\n\n\n')


unikana_liczba = 20
liczby = [1, 6, 8, 18, 19, 20, 100, 55, 64]

print(f"liczby: {liczby}\nszukana: {szukana_liczba}")

for liczba in liczby:
    if liczba == unikana_liczba:
        continue

    print(f"liczba: {liczba}")


# input: liczba dla ktorej zrobimy tabliczke
# input: len tabliczki
# out:
# tabliczka dla liczzby:
# 1 x 2 = 2
# 2 x 2 = 4
# 2 x 3 = 6