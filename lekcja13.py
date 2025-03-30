

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"marka: {self.brand}, model: {self.model}, year: {self.year}")


auto = Car(brand='kia', model='lol', year='1672')
auto.info()

marka = auto.brand
print(marka)

class KontoBankowe:
    def __init__(self, balans):
        self.__balans = balans
    
    def __str__(self):
        return f"KONTO BANKOWE: balans: {self.__balans}"

    def depozyt(self, ammount):
        self.__balans += ammount

    def get_balance(self):
        return self.__balans

konto = KontoBankowe(100)
print(str(konto))
print(konto.get_balance())
konto.depozyt(10)
print(konto.get_balance())


class Zwierz:
    def daj_glos(self):
        print('Daje głos...')

class Pies(Zwierz):
    def daj_glos(self):
        print('szczek!')

zwierz = Zwierz()
zwierz.daj_glos()

pies = Pies()
pies.daj_glos()


class Pies:
    def daj_glos(self):
        print('szczek!')

class Kot:
    def daj_glos(self):
        print('miał!')

class Ptak:
    def daj_glos(self):
        print('ćwir!')

zwierzaki = [Pies(), Kot(), Ptak()]

for zwierz in zwierzaki:
    zwierz.daj_glos()



class Uczen:
    nazwa_szkoly = "109 lo w krośnie"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pokaz_studenta(self):
        print(f"imie: {self.name}, wiek: {self.age}")

    @classmethod
    def zmien_szkole(cls, nowa_szkola):
        cls.nazwa_szkoly = nowa_szkola

    @staticmethod
    def ze_stringa(dane_ucznia):
        # dane_studenta = 'kasia, 12111'
        imie = dane_studenta.split(', ')[0]
        wiek = int(dane_studenta.split(', ')[1])
        return Uczen(imie, wiek)

print('\n\n\n')
student1 = Uczen('kasia', 12)
student2 = Uczen('karol', 76)

baza_danych = []
baza_danych.append(student1)
baza_danych.append(student2)

print(baza_danych)
szukany_uczen = 'karol'

for uczen in baza_danych:
    if uczen.name == szukany_uczen:
        print(uczen.pokaz_studenta())

print('\n\n\n')

student1.pokaz_studenta()

print(Uczen.nazwa_szkoly)

Uczen.zmien_szkole(nowa_szkola="10000 lo w jodłowie")
print(Uczen.nazwa_szkoly)

dane_studenta = 'kasia, 12111'
uczen_z_danych = Uczen.ze_stringa(dane_studenta)
print('\n\n\n')

uczen_z_danych.pokaz_studenta()

xd = 10
xd = None

print(bool(1))
print(bool(0))