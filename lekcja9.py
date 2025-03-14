

def nazwa_funkcji(paramtry):
    # cos robimy z parametrem
    return paramtry


def siema():
    print("Siema")

siema()

def siema(imie):
    print(f"Siema {imie}")

siema("bartosz")

def siema(imie, nazwisko):
    print(f"Siema {imie} {nazwisko}")

siema("bartosz", 'wielki')

def sformatuj_imie_i_naziwsko(
    imie,
    nazwisko
):
    return f"Imie: {imie}, Nazwisko: {nazwisko}"

sformatowane = sformatuj_imie_i_naziwsko('barabasz', 'wielki')
print(sformatowane)

def sformatuj_imie_i_naziwsko(
    imie,
    nazwisko = "Kowalski"
):
    return f"Imie: {imie}, Nazwisko: {nazwisko}"

sformatowane = sformatuj_imie_i_naziwsko('barabasz')
print(sformatowane)


sformatowane = sformatuj_imie_i_naziwsko(imie="Kacper", nazwisko="Głowacki")
print(sformatowane)

sformatowane = sformatuj_imie_i_naziwsko(nazwisko="Głowacki", imie="Kacper")
print(sformatowane)

sformatowane = sformatuj_imie_i_naziwsko('wielki', 'barabasz')
print(sformatowane)

def sformatuj_imie_i_naziwsko(
    imie: str,
    nazwisko: str
) -> str:
    return f"Imie: {imie}, Nazwisko: {nazwisko}"

# zsumuj liczby
def policz_liczby(
    liczby: set
):
    pass

print('a', 'b', 'c')

def nasz_print(*do_zprintowania):
    for argument_do_printa in do_zprintowania:
        print(argument_do_printa, end=' ')
    print('\n')


print('a', 'b', 'c')
nasz_print('a', 'b', 'c')

def daj_smieci(**smieci):
    for key, value in smieci.items():
        print(f"key: {key}, value: {value}")

daj_smieci(smiec="xd", laptop="gamingowowy")

kolory = ['czerwony', 'zolty', 'srakowy']

for i, kolor in enumerate(kolory):
    print(i, kolor)

def znajdz_kolor(kolory: list, szukany_kolor: str) -> tuple:
    for i, kolor in enumerate(kolory):
        if kolor == szukany_kolor:
            return i, szukany_kolor

    return None, szukany_kolor

kolory = ['czerwony', 'zolty', 'srakowy']
ktory_z_kolei, kolor = znajdz_kolor(kolory=kolory, szukany_kolor="czerwony")
print('\n\n\n')
print(ktory_z_kolei, kolor)
ktory_z_kolei, kolor = znajdz_kolor(kolory=kolory, szukany_kolor="xD")
print('\n')
print(ktory_z_kolei, kolor)



zmienna = 'xd'
print(zmienna)

del zmienna
# print(zmienna)

def dodaj_100(liczba: int):
    liczba_plus_100 = liczba + 100
    print(liczba_plus_100)

dodaj_100(100)


print('\n')


zmienna_xd = 'xd'

def losowa_funkcja():
    zmienna_xd = 'lol'
    print(zmienna_xd)

losowa_funkcja()

print(zmienna_xd)

ilosc_kartofli = 0

def dodaj_bulwe(ilosc_kartofli):
    return ilosc_kartofli + 1

ilosc_kartofli = dodaj_bulwe(ilosc_kartofli)
print(ilosc_kartofli)


def zewnetrzna():
    def wewnetrzna():
        print('jestem w srodku')

    wewnetrzna()

zewnetrzna()


