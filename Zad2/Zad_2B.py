#pdpkt B

def pomnoz_przez_dwa(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik


print(pomnoz_przez_dwa([1, 2, 3, 4, 5]))


def pomnoz_przez_dwa(liczby):
    return [liczba * 2 for liczba in liczby]


print(pomnoz_przez_dwa([1, 2, 3, 4, 5]))
