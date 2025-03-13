
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
    # 3 | Średnia Ocen Ucznia
    elif nr_komendy == 3:
        baza_imion = set()
        for uczen in baza_danych:
            imie = uczen['imie']
            baza_imion.add(imie)

        imie_ucznia = input("Podaj imię ucznia, któremu chcesz dodać ocenę: ")
        while imie_ucznia not in baza_imion:
            print(f'Imię {imie_ucznia} nie znajduje się w bazie danych')
            imie_ucznia = input("Podaj Poprawne Imię: ")

        for uczen in baza_danych:
            imie = uczen['imie']
            if imie == imie_ucznia:
                print(f"Średnia ocen ucznia {imie} wynosi {sum(uczen['oceny']) / len(uczen['oceny'])}")

    elif nr_komendy == 6:
        imie_ucznia = input("Podaj imię ucznia, któremu chcesz dodać ocenę: ")
        nowa_ocena = input("Podaj ocenę, którą chcesz dodać: ")

        ocena_jest_liczba = nowa_ocena.isdigit()

        baza_imion = set()
        for uczen in baza_danych:
            imie = uczen['imie']
            baza_imion.add(imie)

        while not ocena_jest_liczba:
            print('Ocena To Liczba')
            nowa_ocena = input("Podaj ocenę, którą chcesz dodać: ")
            ocena_jest_liczba = nowa_ocena.isdigit()
            if ocena_jest_liczba:
                nowa_ocena = int(nowa_ocena)

        while imie_ucznia not in baza_imion:
            print(f'Imię {imie_ucznia} nie znajduje się w bazie danych')
            imie_ucznia = input("Podaj Poprawne Imię: ")

        for uczen in baza_danych:
            imie = uczen['imie']
            if imie == imie_ucznia:
                uczen["oceny"].append(int(nowa_ocena))
                print(f"Dodano uczniowi {imie_ucznia} ocenę {nowa_ocena}")

    elif nr_komendy == 7:
        print("\nWszyscy Uczniowie:")
        for uczen in baza_danych:
            imie = uczen['imie']
            wiek = uczen['wiek']
            oceny = uczen['oceny']

            print(f'Imie: {imie}')
            print(f'Wiek: {wiek}')
            print(f'Oceny: {oceny}\n')