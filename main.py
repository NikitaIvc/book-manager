from pathlib import Path
from uuid import uuid4
from storage.json_storage import JsonStorage


def main():
    storage = JsonStorage(Path("storage/book.json"))

    data = [
        {
            "id": uuid4(),
            "title": "Clean Code",
            "author": "Robert Martin",
        },
        {
            "id": uuid4(),
            "title": "1984",
            "author": "George Orwell",
        },
    ]

    storage.save_data(data)
    print("Данные сохранены\n")

    loaded_data = storage.load_data()

    print("Загруженные данные:\n")
    for item in loaded_data:
        print(item)


if __name__ == "__main__":
    main()
