def stworz_baze_imion(
    baza_danych: list
) -> set:
    baza_imion = set()
    for uczen in baza_danych:
        imie = uczen['imie']
        baza_imion.add(imie)

    return baza_imion

def stworz_baze_nazwisk(
    baza_danych: list
) -> set:
    baza_nazwisk = set()
    for uczen in baza_danych:
        nazwisko = uczen['nazwisko']
        baza_nazwisk.add(nazwisko)
    return baza_nazwisk

def dodaj_ucznia(
    baza_danych: list
):
    imie = input("Podaj Imie: ")
    nazwisko = input("Podaj Nazwisko: ")
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
        "nazwisko": nazwisko,
        "wiek": wiek,
        "oceny": []
    }

    baza_danych.append(uczen)
    print(f'Uczen o imieniu {imie}, nazwisku {nazwisko} i wieku {wiek} został dodany!')

def wypisz_imiona(
    baza_danych: list
):
    baza_imion = stworz_baze_imion(baza_danych)

    print(f'Imiona: ', end='')
    for imie in baza_imion:
        print(imie.capitalize(), ', ', end='', sep='')

    print('\n')

def wylicz_średnią_ocen_ucznia(
    baza_danych: list
):
    baza_imion = stworz_baze_imion(baza_danych)

    baza_nazwisk = stworz_baze_nazwisk(baza_danych)

    imie_ucznia = input("Podaj imię ucznia, którego średnią chcesz zobaczyć: ")
    
    while imie_ucznia not in baza_imion:
        print(f'Imię {imie_ucznia} nie znajduje się w bazie danych')
        imie_ucznia = input("Podaj Poprawne Imię: ")

    nazwisko_ucznia = input("Podaj nazwisko ucznia, którego średnią chcesz zobaczyć: ")

    while nazwisko_ucznia not in baza_nazwisk:
        print(f'Nazwisko {nazwisko_ucznia} nie znajduje się w bazie danych')
        nazwisko_ucznia = input("Podaj Poprawne Nazwisko: ")

    for uczen in baza_danych:
        imie = uczen['imie']
        nazwisko = uczen['nazwisko']
        if imie == imie_ucznia and nazwisko == nazwisko_ucznia:
            if len(uczen['oceny']) == 0:
                    print("Uczeń nie posiada żadnych ocen.")
                    continue
            print(f"Średnia ocen ucznia {imie} {nazwisko} wynosi {sum(uczen['oceny']) / len(uczen['oceny'])}")
        else:
            print(f"Nie istnieje uczeń z podanym imieniem i nazwiskiem.")

def wylicz_średnią_ocen_wszystkich_uczniów(
    baza_danych: list
):
    suma_ocen = 0
    liczba_ocen = 0
    for uczen in baza_danych:
        suma_ocen += sum(uczen['oceny'])
        liczba_ocen += len(uczen['oceny'])

    if liczba_ocen == 0:
        return None
    else:
        return suma_ocen / liczba_ocen

def aktualizuj_wiek_na_podstawie_imiona(
    baza_danych: list
):
    baza_imion = stworz_baze_imion(baza_danych)
    baza_nazwisk = stworz_baze_nazwisk(baza_danych)

    imie_ucznia = input("Podaj imię ucznia, któremu chcesz zmienić wiek: ")

    while imie_ucznia not in baza_imion:
        print(f'Imię {imie_ucznia} nie znajduje się w bazie danych')
        imie_ucznia = input("Podaj Poprawne Imię: ")
    
    nazwisko_ucznia = input("Podaj nazwisko ucznia, któremu chcesz zmienić wiek: ")

    while nazwisko_ucznia not in baza_nazwisk:
        print(f'Nazwisko {nazwisko_ucznia} nie znajduje się w bazie danych')
        nazwisko_ucznia = input("Podaj Poprawne Nazwisko: ")

    nowy_wiek = input("Podaj wiek, na który chcesz zmienić: ")
    wiek_jest_liczba = nowy_wiek.isdigit()

    while not wiek_jest_liczba:
        print('Wiek To Liczba')
        nowy_wiek = input("Podaj wiek, na który chcesz zmienić: ")
        wiek_jest_liczba = nowy_wiek.isdigit()
        if wiek_jest_liczba:
            wiek = int(nowy_wiek)

    for uczen in baza_danych:
        if uczen['imie'] == imie_ucznia and uczen['nazwisko'] == nazwisko_ucznia:
            uczen['wiek'] = nowy_wiek
            print(f"Zmieniono wiek {imie_ucznia} na {nowy_wiek} lat")
        else:
            print("Podany uczeń nie istnieje.")

def dodaj_ocene_uczniowi_o_imieniu(
    baza_danych: list
):
    baza_imion = set()
    for uczen in baza_danych:
        imie = uczen['imie']
        baza_imion.add(imie)

    baza_nazwisk = set()
    for uczen in baza_danych:
        nazwisko = uczen['nazwisko']
        baza_nazwisk.add(nazwisko)

    imie_ucznia = input("Podaj imię ucznia, któremu chcesz dodać ocenę: ")

    while imie_ucznia not in baza_imion:
        print(f'Imię {imie_ucznia} nie znajduje się w bazie danych')
        imie_ucznia = input("Podaj Poprawne Imię: ")

    nazwisko_ucznia = input("Podaj nazwisko ucznia, któremu chcesz dodać ocenę: ")

    while nazwisko_ucznia not in baza_nazwisk:
        print(f'Nazwisko {nazwisko_ucznia} nie znajduje się w bazie danych')
        nazwisko_ucznia = input("Podaj Poprawne Nazwisko: ")

    nowa_ocena = input("Podaj ocenę, którą chcesz dodać: ")

    ocena_jest_liczba = nowa_ocena.isdigit()

    while not ocena_jest_liczba:
        print('Ocena To Liczba')
        nowa_ocena = input("Podaj ocenę, którą chcesz dodać: ")
        ocena_jest_liczba = nowa_ocena.isdigit()
        if ocena_jest_liczba:
            nowa_ocena = int(nowa_ocena)

    for uczen in baza_danych:
        imie = uczen['imie']
        nazwisko = uczen['nazwisko']
        if imie == imie_ucznia and nazwisko == nazwisko_ucznia:
            uczen["oceny"].append(int(nowa_ocena))
            print(f"Dodano uczniowi {imie_ucznia} ocenę {nowa_ocena}")
        else:
            print(f"Nie istnieje uczeń z podanym imieniem i nazwiskiem.")


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
    print('8 | Wypisz Nazwiska')
    print('9 | Opóść Program')

    nr_komendy = input("Podaj Nr Komendy: ")
    if nr_komendy.isdigit():
        nr_komendy = int(nr_komendy)
    else:
        print('Użyj Cyfry Imbecylu')
        continue

    if nr_komendy == 1:
        dodaj_ucznia(baza_danych)

    elif nr_komendy == 2:
        wypisz_imiona(baza_danych)

    elif nr_komendy == 3:
        wylicz_średnią_ocen_ucznia(baza_danych)

    elif nr_komendy == 4:
        średnia = wylicz_średnią_ocen_wszystkich_uczniów(baza_danych)
        if średnia == None:
            print("Uczniowie nie posiadają żadnych ocen.")
        else:
            print(f"Srednia wszystkich uczniow wynosi {średnia}")


    elif nr_komendy == 5:
        aktualizuj_wiek_na_podstawie_imiona(baza_danych)

    elif nr_komendy == 6:
        dodaj_ocene_uczniowi_o_imieniu(baza_danych)

    elif nr_komendy == 7:
        print("\nWszyscy Uczniowie:")
        for uczen in baza_danych:
            imie = uczen['imie']
            nazwisko = uczen['nazwisko']
            wiek = uczen['wiek']
            oceny = uczen['oceny']

            print(f'Imie: {imie}')
            print(f'Nazwisko: {nazwisko}')
            print(f'Wiek: {wiek}')
            print(f'Oceny: {oceny}\n')

    elif nr_komendy == 8:
        baza_nazwisk = set()
        for uczen in baza_danych:
            nazwisko = uczen['nazwisko']
            baza_nazwisk.add(nazwisko)

        print(f'Nazwiska: ', end='')
        for nazwisko in baza_nazwisk:
            print(nazwisko.capitalize(), ', ', end='', sep='')

        print('\n')

        
    elif nr_komendy == 9:
        print("wypierdalaj")
        break