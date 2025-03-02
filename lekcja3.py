
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
