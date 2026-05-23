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

