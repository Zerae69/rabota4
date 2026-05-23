import json

FILE = "books.json"


def load_books():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)


def add_book():
    books = load_books()

    author = input("Автор: ")
    title = input("Название: ")
    rating = int(input("Оценка (1-5): "))
    date = input("Дата: ")

    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    })

    save_books(books)
    print("Книга добавлена")


def show_books():
    books = load_books()
    for b in books:
        print(b)


def avg_rating():
    books = load_books()

    if not books:
        print("Нет книг")
        return

    total = sum(b["rating"] for b in books)
    print("Средняя оценка:", total / len(books))


def stats():
    books = load_books()
    authors = {}

    for b in books:
        authors[b["author"]] = authors.get(b["author"], 0) + 1

    print(authors)


def delete_book():
    books = load_books()

    title = input("Название книги для удаления: ")

    new_books = [b for b in books if b["title"] != title]

    save_books(new_books)
    print("Удалено")


def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Средняя оценка")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            avg_rating()
        elif choice == "4":
            stats()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            break


if __name__ == "__main__":
    main()