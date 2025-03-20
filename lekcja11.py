

file = open('test.txt', "r")


# 'r': czytaj plik
# 'w': otwiera plik albo go tworzy ale jak istnieje plik to go nadpisuje
# 'a': ustawia nas na koncu pliku i umozliwia pisanie
# 'b': tryb binarny: 'rb' 'wb'
# 'x': tworzy nam plik tylko jezeli nie istnieje

content = file.read()

print(content)

file.close()

print('\n\n\n')

file = open('test.txt', "r")
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()

print('\n\n\n')

file = open('test.txt', "r")

#content = file.read()

lines = file.readlines()

print(lines)


file.close()

print('\n\n\n'* 10)

file = open('test1.txt', "w")
file.write("skibidi")
file.close()

linie = ['xd\n', 'sq\n', 'siogma\n']

file = open('test2.txt', "w")
file.writelines(linie)
file.close()


file = open('test2.txt', "a")
file.write('\nsiema z apenda')
file.close()

with open('test2.txt', 'r') as file:
    content = file.read()
    print(content)

with open('sample_1280x720_surfing_with_audio.mkv', 'rb') as file:
    binarne_dane = file.read()
    print(binarne_dane[:100]) # pierwsze 100 bajtow
    with open('trol.mvk', 'wb') as file_zdjecie:
        file_zdjecie.write(binarne_dane[:50000000])

with open('erm/lol/xd.lol', 'r') as file:
    content = file.read()
    print(content)
# /home/usia/Documents/korki/erm/lol/xd.lol\\

import os
os.rename('trol.mvk', 'trol.mp4')

os.remove('trol.mp4')

import datetime

data_i_godzina = datetime.datetime.now()
wpis = input("Wprowadź notatkę: ")

with open('Notatka.txt', "a") as file:
    file.write(f"{data_i_godzina.strftime("%x"), data_i_godzina.strftime("%X")} {wpis}\n")

print("Pomyślnie dodano notatkę!")

