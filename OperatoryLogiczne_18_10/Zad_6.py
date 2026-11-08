
def czy_zawiera(lista: list, liczba: int) -> bool:
    return liczba in lista


wynik = czy_zawiera([1, 5, 8, 12], 8)
print(wynik)
