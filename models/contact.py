from dataclasses import dataclass

from models.base_entity import BaseEntity


@dataclass
class Contact(BaseEntity):
    name: str = ""
    phone: str = ""
    email: str = ""

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}"
