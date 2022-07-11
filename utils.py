import json


def load_books_from_json() -> list[dict]:
    """
    Загружает книжки из файла.
    :return: список словарей
    """
    with open("books.json", encoding="utf-8") as file:
        books = json.load(file)
    return books


def save_books_to_json(books) -> None:
    """
    Сохраняет список словарей в json файл
    """

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=2, ensure_ascii=False)


def get_books() -> list[dict]:
    """
    Получить все книжки из json файла.
    :return: список словарей
    """
    books = load_books_from_json()
    return books


def get_book_by_id(book_id) -> dict:
    """
    Получает книгу по ее id.
    :param book_id: значение поля id книги
    :return: словарь с данными книги
    """
    books = load_books_from_json()
    for book in books:
        if book["id"] == book_id:
            return book


def add_book(book_data: dict) -> dict:
    """
    Записывает новую книгу в файл.
    :param book_data: словарь с данными книги.
    :return: вновь добавленный словарь
    """

    books = load_books_from_json()
    last_book = books[-1]
    last_id = last_book["id"]
    book_data["id"] = last_id + 1

    books.append(book_data)
    save_books_to_json(books)
    return book_data


def update_book(book_id: int, book_data: dict) -> None:
    """
    Обновляет книгу с нужным book_id
    :param book_id: id книги
    :param book_data: новые данные книги
    """

    books = load_books_from_json()
    for book in books:
        if book["id"] == book_id:
            book.update(book_data)
            break
    save_books_to_json(books)


def delete_book(book_id: int) -> None:
    """
    Удаляет книгу с указанным book_id
    :param book_id: id книги
    """

    books = load_books_from_json()
    for index, book in enumerate(books):
        if book["id"] == book_id:
            del books[index]
            break
    save_books_to_json(books)
