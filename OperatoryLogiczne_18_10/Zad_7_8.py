import argparse
from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: str
    street: Optional[str]

    def __str__(self) -> str:
        return (
            f"Browar: {self.name}\n"
            f"ID: {self.id}\n"
            f"Typ: {self.brewery_type}\n"
            f"Adres: {self.address_1}\n"
            f"Miasto: {self.city}\n"
            f"Stan/region: {self.state_province}\n"
            f"Kod pocztowy: {self.postal_code}\n"
            f"Kraj: {self.country}\n"
            f"Długość geograficzna: {self.longitude}\n"
            f"Szerokość geograficzna: {self.latitude}\n"
            f"Telefon: {self.phone}\n"
            f"Strona internetowa: {self.website_url}\n"
            f"{'-' * 40}"
        )

    @classmethod
    def from_api(cls, data: dict) -> "Brewery":
        return cls(
            id=data["id"],
            name=data["name"],
            brewery_type=data["brewery_type"],
            address_1=data.get("address_1"),
            address_2=data.get("address_2"),
            address_3=data.get("address_3"),
            city=data["city"],
            state_province=data.get("state_province") or "",
            postal_code=data.get("postal_code") or "",
            country=data["country"],
            longitude=data.get("longitude"),
            latitude=data.get("latitude"),
            phone=data.get("phone"),
            website_url=data.get("website_url"),
            state=data.get("state") or "",
            street=data.get("street"),
        )


def pobierz_browary(city: Optional[str] = None) -> list[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries"

    params = {"per_page": 20}

    if city:
        params["by_city"] = city

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    dane = response.json()

    browary = [Brewery.from_api(item) for item in dane]

    return browary


parser = argparse.ArgumentParser(
    description="Pobieranie danych o browarach z Open Brewery DB"
)

parser.add_argument(
    "--city",
    type=str,
    help="Nazwa miasta, np. Berlin",
)

args = parser.parse_args()

try:
    browary = pobierz_browary(args.city)

    if not browary:
        print("Nie znaleziono browarów dla podanych kryteriów.")
    else:
        print(f"Liczba pobranych browarów: {len(browary)}\n")

        for browar in browary:
            print(browar)

except requests.RequestException as error:
    print(f"Błąd połączenia z API: {error}")