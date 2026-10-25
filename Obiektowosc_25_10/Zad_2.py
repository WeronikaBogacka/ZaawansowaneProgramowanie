# Zadanie 2 Klasy

from Zad_1 import Student


class Library:
    def __init__(
        self,
        city,
        street,
        zip_code,
        open_hours,
        phone,
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka w {self.city} na ulicy {self.street}, "
            f"Kod pocztowy: {self.zip_code}. "
            f"Godziny otwarcia: {self.open_hours}. "
            f"Numer telefonu: {self.phone}."
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        email,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Imię i nazwisko: {self.first_name} {self.last_name}. "
            f"Email: {self.email}. "
            f"Data zatrudnienia: {self.hire_date}. "
            f"Data urodzenia: {self.birth_date}. "
            f"Adres: {self.street}, {self.city}, "
            f"Kod pocztowy: {self.zip_code}. "
            f"Numer telefonu: {self.phone}."
        )


class Book:
    def __init__(
        self,
        library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka napisana przez {self.author_name} "
            f"{self.author_surname}, "
            f"Data opublikowania {self.publication_date}. "
            f"Ilość stron: {self.number_of_pages}. "
            f"Znajduje się w bibliotece: {self.library}."
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_description = ", ".join(
            str(book) for book in self.books
        )

        return (
            f"Data zamówienia: {self.order_date}. "
            f"Pracownik: {self.employee}. "
            f"Student: {self.student}. "
            f"Zamówione książki: {books_description}."
        )


biblioteka1 = Library(
    city="Katowice",
    street="Bogucicka",
    zip_code="40-277",
    open_hours="8-15",
    phone="32 566 776",
)

biblioteka2 = Library(
    city="Chorzów",
    street="Jana",
    zip_code="40-689",
    open_hours="12-18",
    phone="32 123 567",
)

ksiazka1 = Book(
    biblioteka1,
    publication_date="2020-09",
    author_name="Boleslaw",
    author_surname="Prus",
    number_of_pages=400,
)

ksiazka2 = Book(
    biblioteka2,
    publication_date="2026-03-20",
    author_name="Kowalski",
    author_surname="Jan",
    number_of_pages=250,
)

ksiazka3 = Book(
    biblioteka1,
    publication_date="2024-05-24",
    author_name="Nowak",
    author_surname="Bartek",
    number_of_pages=340,
)

ksiazka4 = Book(
    biblioteka1,
    publication_date="2023-02-12",
    author_name="Wiaderko",
    author_surname="Jolanta",
    number_of_pages=850,
)

ksiazka5 = Book(
    biblioteka2,
    publication_date="1978-03-20",
    author_name="Kawka",
    author_surname="Marta",
    number_of_pages=200,
)

student1 = Student(name="Maksymilian", marks=[60, 45, 32])
student2 = Student(name="Marta", marks=[44, 22, 80])
student3 = Student(name="Liliana", marks=[60, 45, 32])

pracownik1 = Employee(
    first_name="Jadwiga",
    last_name="Buk",
    email="jbuk@example.com",
    hire_date="2026-03-02",
    birth_date="1978-03-20",
    city="Krakow",
    street="bukowa",
    zip_code="40-123",
    phone="32 566 776",
)

pracownik2 = Employee(
    first_name="Jacek",
    last_name="Miły",
    email="JM@example.com",
    hire_date="2020-03-02",
    birth_date="1970-03-20",
    city="Szczebrzeszyn",
    street="chrzaszczowa",
    zip_code="20-567",
    phone="32 123 456",
)

pracownik3 = Employee(
    first_name="Oliwia",
    last_name="Bruk",
    email="OB@example.com",
    hire_date="2015-08-04",
    birth_date="1980-12-30",
    city="Tychy",
    street="lesna",
    zip_code="30-167",
    phone="32 987 534",
)

zamowienie1 = Order(
    pracownik1,
    student1,
    [ksiazka2, ksiazka1, ksiazka4],
    order_date="2020-09-01",
)

zamowienie2 = Order(
    pracownik3,
    student2,
    [ksiazka3, ksiazka5, ksiazka1],
    order_date="2026-12-02",
)

print(zamowienie1)
print(zamowienie2)
