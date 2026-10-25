# Zadanie 3

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = int(rooms)
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Adres: {self.address}. "
            f"Powierzchnia: {self.area} m². "
            f"Liczba pokoi: {self.rooms}. "
            f"Cena: {self.price} zł."
        )


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = int(plot)

    def __str__(self):
        return (
            f"Dom. {super().__str__()} "
            f"Powierzchnia działki: {self.plot} m²."
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie. {super().__str__()} "
            f"Piętro: {self.floor}."
        )


dom1 = House(area="150m2",
             rooms="5",
             price=750000,
             address="Tytoniowa 123",
             plot=1)
print(dom1)

mieszkanie1 = Flat(area="68m2",
                   rooms="3",
                   price=350000,
                   address="Marmurowa 15",
                   floor=15)
print(mieszkanie1)
