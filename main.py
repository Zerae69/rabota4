import json

FILE = "books.json"

def load_books():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def add_book():
    books = load_books()

    author = input("Автор: ")
    title = input("Название: ")
    rating = int(input("Оценка (1-5): "))
    date = input("Дата: ")

def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def main():
    while True:
        print("1. Добавить книгу")
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
            average_rating()
        elif choice == "4":
            author_stats()
        elif choice == '5':
            delete_book()
        elif choice == "6":
            break
def show_books():
    books = load_books()
    for b in books:
        print(b)

def avg_rating():
    books = load_books()
    if len(books) == 0:
        print("Нет книг")
        return

    total = 0
    for b in books:
        total += b["rating"]

    print("Средняя оценка:", total / len(books))

def stats():
    books = load_books()
    authors = {}
    for b in books:
        if b["author"] in authors:
            authors[b["author"]] += 1
        else:
            authors[b["author"]] = 1

    print(authors)

if __name__ == "__main__":
    main()
    for book in books:
        if book["author"] == author and book["title"] == title:
            print("Такая книга уже есть!")
            return

    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    })

    save_books(books)
    print("Книга добавлена")