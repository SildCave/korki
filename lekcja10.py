lista_uczniow = []
def dodaj_ucznia(uczniowie: list, **uczen):
    lista_uczniow.append(uczen)

dodaj_ucznia(uczniowie = lista_uczniow, wiek=10, imie='maciek', plec='m', placi_podatki=False)
print(lista_uczniow)


kwadrat = lambda x: x * x
print(kwadrat(2))

def zaaplikuj_funkje(func, x):
    return func(x)

def kwadrat(x):
    return x ** 2

def szescian(x):
    return x ** 3

print(zaaplikuj_funkje(kwadrat, 10))
print(zaaplikuj_funkje(szescian, 10))


# kwiat
# taiwk

def reverse_string(tekst):
    odwrocony = ""
    for znak in tekst:
        # 1 iter: odwrocony = k + "" => odwrocony = "k"
        # 2 iter: odwrocony = w + "k" => => odwrocony = "wk"
        # 3 iter: odwrocony = i + "wk" => => odwrocony = "iwk"
        # 4 iter: odwrocony = a + "iwk" => => odwrocony = "aiwk"
        # 5 iter: odwrocony = t + "tiwk" => => odwrocony = "taiwk"
        odwrocony = znak + odwrocony
    return odwrocony

print(reverse_string("kwiat"))
# kwiat len(kwiat) = 5
# index = len(kwiat) -1
# odworcone = [None * (len(kwiat))]
# for znak in tekst => odworcone[index] = znak

