"""Newquay Airport (NQY) destinations — April 2026."""

DESTINATIONS = {
    "NQY": {
        "name": "Newquay",
        "routes": {
            "ABZ": "Aberdeen",
            "AGP": "Malaga",
            "ALC": "Alicante",
            "BHD": "Belfast City",
            "DUB": "Dublin",
            "DUS": "Dusseldorf",
            "EDI": "Edinburgh",
            "ENF": "Enontekio",
            "EXT": "Exeter",
            "FAO": "Faro",
            "GLA": "Glasgow",
            "IOM": "Isle of Man",
            "ISC": "Isles of Scilly",
            "LGW": "London Gatwick",
            "MAN": "Manchester",
            "NCL": "Newcastle",
            "STN": "London Stansted",
            "ZRH": "Zurich",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
