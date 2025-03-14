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


    elif nr_komendy == 2:
        baza_imion = set()
        for uczen in baza_danych:
            imie = uczen['imie']
            baza_imion.add(imie)

        print(f'Imiona: ', end='')
        for imie in baza_imion:
            print(imie.capitalize(), ', ', end='', sep='')

        print('\n')
    # 3 | Średnia Ocen Ucznia
    elif nr_komendy == 3:
        baza_imion = set()
        for uczen in baza_danych:
            imie = uczen['imie']
            baza_imion.add(imie)

        baza_nazwisk = set()
        for uczen in baza_danych:
            nazwisko = uczen['nazwisko']
            baza_nazwisk.add(nazwisko)

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


    elif nr_komendy == 4:
        suma_ocen = 0
        liczba_ocen = 0
        for uczen in baza_danych:
            suma_ocen += sum(uczen['oceny'])
            liczba_ocen += len(uczen['oceny'])

        if liczba_ocen == 0:
            print("Uczniowie nie posiadają żadnych ocen.")
            continue
        
        print(f"Srednia wszystkich uczniow wynosi {suma_ocen / liczba_ocen}")

    elif nr_komendy == 5:
        
        baza_imion = set()
        for uczen in baza_danych:
            imie = uczen['imie']
            baza_imion.add(imie)

        baza_nazwisk = set()
        for uczen in baza_danych:
            nazwisko = uczen['nazwisko']
            baza_nazwisk.add(nazwisko)

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



    elif nr_komendy == 6:

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