
baza_danych = []

while True:
    print('Spis komend')
    print('1 | Dodaj Ucznia')
    print('2 | Wypisz Imiona')
    print('3 | Średnia Ocen Ucznia')
    print('4 | Średnia Wszystkich Ocen Uczniów')
    print('5 | Aktualizuj Wiek Na Podstawie Imiona')
    print('6 | Dodaj Ocene Uczniowi O Imieniu')
    print('7 | Wypisz Uczniów')
    print('8 | Opóść Program')

    nr_komendy = input("Podaj Nr Komendy: ")
    if nr_komendy.isdigit():
        nr_komendy = int(nr_komendy)
    else:
        print('Użyj Cyfry Imbecylu')
        continue

    if nr_komendy == 1:
        imie = input("Podaj Imie: ")
        wiek = input("Podaj Wiek: ")

        wiek_jest_liczba = wiek.isdigit()

        while not wiek_jest_liczba:
            print('Wiek To Tylko Liczba')
            wiek = input("Podaj Wiek: ")
            wiek_jest_liczba = wiek.isdigit()

            if wiek_jest_liczba:
                wiek = int(wiek)

        uczen = {
            "imie": imie,
            "wiek": wiek,
            "oceny": []
        }

        baza_danych.append(uczen)
        print(f'Uczen o imieniu {imie} i wieku {wiek} został dodany!')

    elif nr_komendy == 2:
        baza_imion = set()
        for uczen in baza_danych:
            imie = uczen['imie']
            baza_imion.add(imie)

        print(f'Imiona: ', end='')
        for imie in baza_imion:
            print(imie, ', ', end='', sep='')

        print('\n')

    elif nr_komendy == 7:
        print("\nWszyscy Uczniowie:")
        for uczen in baza_danych:
            imie = uczen['imie']
            wiek = uczen['wiek']
            oceny = uczen['oceny']

            print(f'Imie: {imie}')
            print(f'Wiek: {wiek}')
            print(f'Oceny: {oceny}\n')