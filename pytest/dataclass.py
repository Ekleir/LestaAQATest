from dataclasses import dataclass


@dataclass
class Website:
    website: str
    popularity: str
    frontend: str
    backend: str
    database: str
    notes: str


