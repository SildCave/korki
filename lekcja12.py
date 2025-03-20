
try:
    # cos ryzykownego aka cos co moze sie zjebac
    pass
except:
    # co ma sie stac jak sie zjebie cos
    pass


try:
    liczba = 60 #int(input('podaj liczbe: '))
    nowa_liczba = 1 / liczba
except ZeroDivisionError:
    print('dzielenie przez 0')
except ValueError:
    print('liczba nie jest liczbą')
else:
    print('nie ma żadnego błędu')
finally:
    print('program skonczyl pracowac')

# crtl + shift + a daje """ """

wiek = 50 #int(input('podaj wiek: '))
if wiek < 0:
    raise ValueError('wiek nie moze byc miejszy niz 0')

try:
    liczba = 50
    nowa_liczba = 1 / liczba
except Exception as e:
    print(e)

import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='logi.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

root.addHandler(handler)
root.addHandler(file_handler)

#logging.basicConfig(filename="logi.log", level=logging.NOTSET)

logging.info('zainicjowano logowanie')

try:
    liczba = int(input('podaj liczbe: '))
    nowa_liczba = 1 / liczba
except ZeroDivisionError:
    logging.error('Wystopilo dzielenie przez 0')
except ValueError:
    logging.error('Liczba jaka wpisal ziomek nie jest liczba')
else:
    logging.info('nie ma żadnego błędu')
finally:
    logging.debug('program skonczyl pracowac')