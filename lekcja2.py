name = "kacper"
nazwisko = 'kulmacz'

print("imie: " + name + " nazwisko: " + nazwisko)
print("imie:", name, "nazwisko:", nazwisko)

print("imie:", name, "nazwisko:", nazwisko, sep=' xd ')

print("imie:", name, ' ', end='')
print("nazwisko:", nazwisko, end='\n')

# importent

print(f"imie: {name}, nazwisko: {nazwisko}")  # !!!!!!!
full_name = f"{name} {nazwisko}" # !!!!
print("Full name: " + full_name)


imie = input("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")

full_name = f"{imie} {nazwisko}" # !!!!
print("Full name: " + full_name)

# wazne
napis = "Polska"
pierwsza_litera = napis[0]

print(f"pierwsza litera: {pierwsza_litera}")

# wazne
napis = "Polska"
ostatnia_litera = napis[-1]

print(f"ostatnia litera: {ostatnia_litera}")

# wazne
napis = "Polska"
# od o do k
skrawek = napis[1:5] # <x; y)
print(f"skrawek: {skrawek}")

# wazne
napis = "Polskapwtghunipervpuni42vun89p"
koncowka = napis[1::]
print(f"koncowka: {koncowka}")

# nie wazne
napis = "xD"
reverse = napis[::-1]
print(f"reverse: {reverse}")


# lekko wazne

nazwa = "usa"
nazwa = nazwa.upper()
print(f"nazwa: {nazwa}")

nazwa = "DIS STREAM"
nazwa = nazwa.lower()
print(f"nazwa: {nazwa}")

# bardziej wazne

imie = 'kACPER'
imie = imie.capitalize() #More specifically, make the first character have upper case and the rest lowercase.
print(f"imie: {imie}")

# bardzo wazne
komurka = '645'
print(f"komurka: {komurka} jest liczba: {komurka.isdigit()}")

# wazne                  |
zdanie = "Next privilege at 856 rep: Set bounties."
idx = zdanie.find("at ")
koncowka = zdanie[(idx + 3)::]
print(f"koncowka: {koncowka}")

idx = koncowka.find(" rep")
final = koncowka[0:idx]
print(f"Finalna liczba: {final}")