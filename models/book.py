from dataclasses import dataclass
from models.base_entity import BaseEntity


@dataclass
class Book(BaseEntity):
    title: str = ""
    author: str = ""
    isbn: str = ""
    year: str = ""
    status: str = ""

    def __str__(self):
        return f"{self.title}, {self.author}, {self.isbn}, {self.year}, {self.status}"