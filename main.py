
def add_book():
    books = load_books()

    author = input("Автор: ")
    title = input("Название: ")
    rating = int(input("Оценка (1-5): "))
    date = input("Дата: ")

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