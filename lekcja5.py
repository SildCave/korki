

for i in range(6 + 1):
    print(i)

print('\n')

i = 0
while i <= 6:
    print(i)

    i += 1


count = 0

while count <= 10:
    print(f"liczba teraz: {count}")
    # szukamy 6
    if count == 6:
        print('znalezione 6')
        break

    count += 1



# zprintuj wszystkie liczby nieparzyste uzywajac while loopa 

while (1 == 1):
    print('jsdfcvhsdjghbcv')
    break

import random

print('losowa cyfra:', random.randint(1, 10))

# najmiejsza liczbe do zgadywania
# najwieksza liczbe do zzgadniecia
# i bedzie pytac o liczby dopoki user nie zgadnie daja w miedzy czasie wskazowki czy liczba jkest za mala zczy za duza

# słowo => znaczenie
# trawa => roslina zielona do koszenia


print('\n' * 4)

słownik = {
    'trawa': 'nazwa niektórych gatunków roślin należących do rodziny o tej samej nazwie',
    'wąż': 'drapieżny gad lądowy lub wodny'
}

print(f'definicja wąż: {słownik['wąż']}')
print(f'definicja trawa: {słownik['trawa']}')

nic = None
print(f'bool(None), {bool(None)}')

print(0 == None)

nic = int(bool(None)) + 1
print(nic)

print('\n' * 2)

# print(f'definicja serce: {słownik['serce']}')
print(słownik.get('serce'))
print(słownik.get('trawa'))

if słownik.get('trawa') != None:
    print('mamy słowo')

słownik = {
    'trawa': 'nazwa niektórych gatunków roślin należących do rodziny o tej samej nazwie',
    'wąż': 'drapieżny gad lądowy lub wodny'
}

print(słownik)

słownik['trawa'] = 'Nie Wiem xD'

print(słownik)


słownik['serce'] = 'narząd zapewniający krążenie w układzie krwionośnym ssaków i ptaków'

print(słownik)


del słownik['serce']

print(słownik)

usuniete = słownik.pop('trawa')
print(f'usniety itemek: {usuniete}')
print(słownik)

print('\n\n\n')
słownik = {
    'trawa': 'nazwa niektórych gatunków roślin należących do rodziny o tej samej nazwie',
    'wąż': 'drapieżny gad lądowy lub wodny'
}
słownik['serce'] = 'narząd zapewniający krążenie w układzie krwionośnym ssaków i ptaków'

for key, value in słownik.items():
    print(f'key: {key}, val: {value}')

print('\n')
for klucz in słownik:
    print(f'key: {klucz}')

print('\n')
for val in słownik.values():
    print(f'key: {val}')


print('\n')

ludzie = {
    "Alicja": {
        "wiek": 64,
        "punkty_karne": 11,
        'posiada_prawo_jazdy': True,
        'rodzina': ['kasia', 'marta']
    },
    "Jackek": {
        "wiek": 12,
        "punkty_karne": 0,
        'posiada_prawo_jazdy': False,
        'rodzina': ['karol', 'elzbieta']
    }
}

wiek_jacka = ludzie['Jackek']['wiek']
print(f'wiek jacka: {wiek_jacka}')

pierwsza_krewna_alicji = ludzie['Alicja']['rodzina'][0]
print(f'pierwsza_krewna_alicji: {pierwsza_krewna_alicji}')


print('klucze')
print(ludzie.keys())

print('\nwartosci')
print(ludzie.values())

print('\nitemki')
print(ludzie.items())


osoba = {
        "wiek": 64,
        "punkty_karne": 11,
        'posiada_prawo_jazdy': True,
        'rodzina': ['kasia', 'marta']
    }

adres = {
    'nr_domu': 122,
    'miejscowowsc': 'wwa'
}

osoba.update(adres)

print(osoba)

# {
#   "wiek": 64,
#   "punkty_karne": 11,
#   "posiada_prawo_jazdy": true,
#   "rodzina": ["kasia", "marta"],
#   "nr_domu": 122,
#   "miejscowowsc": "wwa"
# }
