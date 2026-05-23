def delete_book():
    books = load_books()

    title = input("Название книги для удаления: ")

    new_books = []
    for b in books:
        if b["title"] != title:
            new_books.append(b)

    save_books(new_books)
    print("Удалено")