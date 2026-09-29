print("==========================================")
print("         LIBRARY MANAGEMENT SYSTEM")
print("==========================================")

books = []

while True:
    print("\n--------------- MENU ----------------")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Remove Book")
    print("7. Exit")
    print("--------------------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "status": "Available"
        }

        books.append(book)
        print("Book added successfully.")

    elif choice == "2":
        if len(books) == 0:
            print("No books available in the library.")
        else:
            print("\n========== BOOK LIST ==========")

            for book in books:
                print("\nBook ID   :", book["id"])
                print("Title     :", book["title"])
                print("Author    :", book["author"])
                print("Status    :", book["status"])

    elif choice == "3":
        search_title = input("Enter book title to search: ").lower()
        found = False

        for book in books:
            if search_title in book["title"].lower():
                print("\nBook Found")
                print("Book ID :", book["id"])
                print("Title   :", book["title"])
                print("Author  :", book["author"])
                print("Status  :", book["status"])
                found = True

        if not found:
            print("Book not found.")

    elif choice == "4":
        book_id = input("Enter book ID to issue: ")
        found = False

        for book in books:
            if book["id"] == book_id:
                found = True

                if book["status"] == "Available":
                    book["status"] = "Issued"
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")

                break

        if not found:
            print("Book ID not found.")

    elif choice == "5":
        book_id = input("Enter book ID to return: ")
        found = False

        for book in books:
            if book["id"] == book_id:
                found = True

                if book["status"] == "Issued":
                    book["status"] = "Available"
                    print("Book returned successfully.")
                else:
                    print("This book was not issued.")

                break

        if not found:
            print("Book ID not found.")

    elif choice == "6":
        book_id = input("Enter book ID to remove: ")
        found = False

        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                found = True
                print("Book removed successfully.")
                break

        if not found:
            print("Book ID not found.")

    elif choice == "7":
        print("\nThank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
