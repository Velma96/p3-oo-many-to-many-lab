from datetime import datetime

class Book:
    all_books = []
    
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all_books.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return list(set(contract.author for contract in self.contracts()))
    
    def __repr__(self):
        return f"Book({self.title})"


class Author:
    all_authors = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all_authors.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return list(set(contract.book for contract in self.contracts()))
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    
    def __repr__(self):
        return f"Author({self.name})"


class Contract:
    all = []  # Renamed from all_contracts to match test expectations
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        filtered_contracts = [contract for contract in cls.all if contract.date == date]
        return sorted(filtered_contracts, key=lambda c: cls.all.index(c))  # Sorting by creation order
    
    def __repr__(self):
        return f"Contract(Author: {self.author.name}, Book: {self.book.title}, Date: {self.date}, Royalties: {self.royalties})"
