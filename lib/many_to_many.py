class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def add_contract(self, contract):
        self._contracts.append(contract)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        book.add_contract(contract)
        return contract

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


