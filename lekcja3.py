
# wazne                  |
zdanie = "Next privilege at 856 rep: Set bounties."
idx = zdanie.find("at ")
koncowka = zdanie[(idx + 3)::]
print(f"koncowka: {koncowka}")

idx = koncowka.find(" rep")
final = koncowka[0:idx]
print(f"Finalna liczba: {final}")


zdanie = "Next privilege at 856 rep: Set bounties."

słowa = zdanie.split(' ')
print(słowa) # ['Next', 'privilege', 'at', '856', 'rep:', 'Set', 'bounties.']


kolory = ["czarny", "biały"]
kolor_pierwszy = kolory[0]
print(kolor_pierwszy)

ilosc_elementow = len(kolory)
print(f"ilosc elementow: {ilosc_elementow}")

ostatni_kolor = kolory[ilosc_elementow - 1]
print(f"ostatni_kolor: {ostatni_kolor}")

# wazne
zdanie = "Next privilege at 856 rep: Set bounties."

czesci = zdanie.split('Next privilege at ')
print(f"czesci 1: {czesci}")

part_2 = czesci[1]
print(f"part 2: {part_2}")

czesci = part_2.split(' rep: Set bounties.')
print(f"czesci 2: {czesci}")

liczba = czesci[0]
print(f"finalna licba: {liczba}")

# wazne
zdanie_brzydkie = "Ala zarąbała grzegorzowi"

brzydkie_slowo = "zarąbała"
zdanie_ocenzurowane = zdanie_brzydkie.replace(brzydkie_slowo, '*' * len(brzydkie_slowo))

print(f"ocenzurowane: {zdanie_ocenzurowane}")


zdanie = "Next privilege at 856 rep: Set bounties."

liczba = int(zdanie.replace('Next privilege at ', '').replace(' rep: Set bounties.', ''))
print(f"liczba: {liczba}")



brakujace = 1000 - liczba
print(f"brakujace: {brakujace}")



# liczba_uzytkownika = input("podaj liczbe: ")
# print(f"nie wyjebie sie: {liczba_uzytkownika.isdigit()}")

# liczba_uzytkownika = int(liczba_uzytkownika) + 1

liczba = 100
liczba -= 10
print(liczba)


liczba = 100
liczba /= 10 # liczba = liczba / 10

print(liczba)


liczba = 100
liczba *= 10 # liczba = liczba * 10

print(liczba)


liczba = 100
liczba //= 10 # liczba = liczba * 10

print(liczba)


liczba = 10
reszta = liczba % 4
print(f"reszta: {reszta}")

liczba_float = 2.5
print(liczba_float * 4)


# wazne/dziwne
print(1/11)

# 0.0909090909
# 0.09090909090909091


jedna_trzecia = 1 / 3
print(round(jedna_trzecia, 2))

liczba = 2
liczba_do_pot_5 = liczba ** 5
print(liczba_do_pot_5)

prawda = True
print(type(prawda))

#################

wynik = ( 100 == 100 ) # jest rowne
print(f"wynik: {wynik}")

wynik = ( 100 == 101 )
print(f"wynik: {wynik}")


wynik = ( 100 != 100 ) # nie jest rowne
print(f"wynik: {wynik}")

wynik = ( 100 != 101 )
print(f"wynik: {wynik}")


###########
print('\n\n\n')

wynik = ( 5 > 3 )
print(f"wynik: {wynik}")

wynik = ( 3 > 5 )
print(f"wynik: {wynik}")

print('\n\n')

wynik = ( 5 >= 5 )
print(f"wynik: {wynik}")

wynik = ( 3 <= 5 )
print(f"wynik: {wynik}")

## dziwne / wazne i to bardzzo
print('\n\n')

zdanie = "ala ma kota"
print(bool(zdanie))

zdanie = ""
print(bool(zdanie))

# Wniosek: w pythonie empty string jest False a string z czyms jest True

print('\n\n')

liczba = 0
print(bool(liczba))

liczba = -781236
print(bool(liczba))


print('\n\n')

zbior = ["ala", "ma", "kota"]
print(bool(zbior))

zbior = []
print(bool(zbior))


if 10 > 5:
    print("10 jest wieksze od 5")

wiek = 6
if wiek >= 18:
    print('jestes pelnoletni')
else:
    print('nie jestes pelnoletni')


procent_z_testu = 33
if procent_z_testu >= 90:
    print('dostajesz 5')
elif procent_z_testu >= 50:
    print('zdajesz')
else:
    print('nie zdajesz')


pijany = False
wiek = 16

if pijany == False and wiek >= 18:
    print('mozna sprzedac')
else:
    print('nie mozna sprzedac')

ma_kase_na_karcie = True
ma_gotowke = False

if ma_kase_na_karcie or ma_gotowke:
    print('moze zaplacic')

warunek = False
if not warunek:
    print('ok')


