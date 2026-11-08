
import re
import unicodedata


# 1. Sprawdzanie palindromu
def is_palindrome(text: str) -> bool:
    text = text.casefold()
    text = "".join(char for char in text if char.isalnum())

    return text == text[::-1]


# 2. Ciąg Fibonacciego
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n nie może być ujemne")

    if n == 0:
        return 0

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


# 3. Zliczanie samogłosek
def count_vowels(text: str) -> int:
    vowels = "aeiouy"

    # Zamiana polskich znaków na ich podstawowe odpowiedniki
    normalized = unicodedata.normalize("NFD", text.casefold())

    normalized = "".join(
        char for char in normalized
        if unicodedata.category(char) != "Mn"
    )

    return sum(1 for char in normalized if char in vowels)


# 4. Obliczanie zniżki
def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("Zniżka musi być z zakresu 0-1")

    return price * (1 - discount)


# 5. Spłaszczanie listy
def flatten_list(nested_list: list) -> list:
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


# 6. Częstotliwość występowania słów
def word_frequencies(text: str) -> dict:
    words = re.findall(r"[^\W\d_]+", text.casefold())

    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


# 7. Sprawdzanie liczby pierwszej
def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
