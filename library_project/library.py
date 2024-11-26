import os
import json
from book import Book


class Library:
    """Класс, представляющий библиотеку."""

    def __init__(self, filename: str):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Загружает книги из файла JSON."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.books = [Book.from_dict(item) for item in data]

    def save_books(self):
        """Сохраняет книги в файл JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False)

    def add_book(self, title: str, author: str, year: str):
        """Добавляет новую книгу в библиотеку."""
        try:
            year = int(year)
        except ValueError:
            print("Некорректный ввод. Год издания должен быть числом.")
            return
        if year < 868:
            print("Некорректная дата издания. Самая старая книга в мире датирована 11 мая 868 года.")
            return

        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {book_id}.")

    def remove_book(self, book_id: int):
        """Удаляет книгу по ID."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с ID {book_id} удалена.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, query: str):
        """Ищет книги по заголовку, автору или году издания."""
        results = [book for book in self.books if query.lower() in book.title.lower() or
                   query.lower() in book.author.lower() or
                   str(book.year) == query]

        if results:
            for book in results:
                print(f"{book.id}: '{book.title}' автор {book.author}, {book.year}, статус: {book.status}")
        else:
            print("Книги не найдены.")

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
            return

        for book in self.books:
            print(f"{book.id}: '{book.title}' автор {book.author}, {book.year}, статус: {book.status}")

    def change_status(self, book_id: int, new_status: str):
        """Изменяет статус книги по ID."""
        if new_status not in ["в наличии", "выдана"]:
            print("Некорректный статус. Используйте 'в наличии' или 'выдана'.")
            return

        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")
