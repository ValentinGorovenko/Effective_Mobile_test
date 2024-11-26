from library import Library


def main():
    library = Library("books.json")

    while True:
        print("\nДоступные команды:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите команду (1-6): ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == "3":
            query = input("Введите название, автора или год для поиска: ")
            library.search_books(query)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(book_id, new_status)

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
