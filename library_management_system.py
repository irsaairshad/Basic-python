class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_available = True

    def get_availability(self):
        return self.__is_available

    def set_availability(self, status):
        self.__is_available = status


class Member:
    borrow_limit = 1

    def __init__(self, name):
        self.name = name

    def borrow_book(self, book_object):
        if book_object.get_availability():
            book_object.set_availability(False)
            return "Book Issued"
        return "Out of Stock"


class StudentMember(Member):
    borrow_limit = 3


class TeacherMember(Member):
    borrow_limit = 6


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_object):
        self.books.append(book_object)


if __name__ == "__main__":
    library = Library()
    book1 = Book("Clean Code", "Robert Martin")
    book2 = Book("Python Crash Course", "Eric Matthes")
    library.add_book(book1)
    library.add_book(book2)

    student = StudentMember("Zain")
    teacher = TeacherMember("Dr. Umar")

    print(student.borrow_book(book1))
    print(teacher.borrow_book(book1))
    print(teacher.borrow_book(book2))

    print("Student borrow limit:", student.borrow_limit)
    print("Teacher borrow limit:", teacher.borrow_limit)
