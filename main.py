from datetime import datetime


# ===== BOOK CLASS =====
class Book:

    def __init__(self, book_id, title, author):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


# ===== MEMBER CLASS =====
class Member:

    def __init__(self, member_id, name, email):

        self.member_id = member_id
        self.name = name
        self.email = email


# ===== LOAN CLASS =====
class Loan:

    def __init__(self, loan_id, book, member):

        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.date_borrowed = datetime.now()
        self.is_active = True

    def return_book(self):

        self.is_active = False
        self.book.is_available = True


# ===== LIBRARY CLASS =====
class Library:

    def __init__(self):

        self.books = []
        self.members = []
        self.loans = []

        self.next_book_id = 1
        self.next_member_id = 1
        self.next_loan_id = 1

    # ===== HELPER FUNCTIONS =====
    def get_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:
                return book

        return None

    def get_member(self, member_id):

        for member in self.members:

            if member.member_id == member_id:
                return member

        return None

    def get_loan(self, loan_id):

        for loan in self.loans:

            if loan.loan_id == loan_id:
                return loan

        return None

    # ===== FEATURE 1 : ADD BOOK =====
    def add_book(self):

        try:

            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            new_book = Book(
                self.next_book_id,
                title,
                author
            )

            self.books.append(new_book)

            print(
                f"Book added successfully! "
                f"Book ID: {self.next_book_id}"
            )

            self.next_book_id += 1

        except Exception as e:

            print("Error:", e)

    # ===== FEATURE 2 : REGISTER MEMBER =====
    def register_member(self):

        try:

            name = input("Enter Member Name: ")
            email = input("Enter Member Email: ")

            new_member = Member(
                self.next_member_id,
                name,
                email
            )

            self.members.append(new_member)

            print(
                f"Member registered successfully! "
                f"Member ID: {self.next_member_id}"
            )

            self.next_member_id += 1

        except Exception as e:

            print("Error:", e)

    # ===== FEATURE 3 : BORROW BOOK =====
    def borrow_book(self):

        try:

            book_id = int(input("Enter Book ID: "))
            member_id = int(input("Enter Member ID: "))

            book = self.get_book(book_id)

            if book is None:
                raise Exception("Book not found.")

            member = self.get_member(member_id)

            if member is None:
                raise Exception("Member not found.")

            if book.is_available == False:
                raise Exception("Book is already borrowed.")

            loan = Loan(
                self.next_loan_id,
                book,
                member
            )

            self.loans.append(loan)

            book.is_available = False

            print(
                f"{member.name} borrowed "
                f"{book.title}"
            )

            self.next_loan_id += 1

        except ValueError:

            print("Please enter valid numbers.")

        except Exception as e:

            print("Error:", e)

    # ===== FEATURE 4 : RETURN BOOK =====
    def return_book(self):

        try:

            loan_id = int(input("Enter Loan ID: "))

            loan = self.get_loan(loan_id)

            if loan is None:
                raise Exception("Loan not found.")

            if loan.is_active == False:
                raise Exception("Book already returned.")

            loan.return_book()

            print(
                f"{loan.member.name} returned "
                f"{loan.book.title}"
            )

        except ValueError:

            print("Please enter a valid number.")

        except Exception as e:

            print("Error:", e)

    # ===== FEATURE 5 : VIEW BOOKS =====
    def view_books(self):

        if len(self.books) == 0:

            print("No books found.")

        else:

            print("\n===== BOOK LIST =====")

            for book in self.books:

                status = (
                    "Available"
                    if book.is_available
                    else "Borrowed"
                )

                print(
                    f"ID: {book.book_id} | "
                    f"Title: {book.title} | "
                    f"Author: {book.author} | "
                    f"Status: {status}"
            