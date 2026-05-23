import json

FILE = "books.json"

def load_books():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

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

if __name__ == "__main__":
    main()