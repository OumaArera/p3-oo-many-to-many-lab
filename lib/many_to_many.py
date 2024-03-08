import datetime

class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.__class__.all_books.append(self)


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contract_list = []
        self.__class__.all_authors.append(self)

    def contracts(self):
        return self.contract_list

    def books(self):
        return [contract.book for contract in self.contract_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book. Book should be an instance of the Book class.")

        if not isinstance(date, str):
            raise Exception("Invalid date. Date should be an instance of the str class.")

        # Check if date is in 'MM/DD/YYYY' format and convert it to 'YYYY-MM-DD'
        try:
            date_obj = datetime.datetime.strptime(date, "%m/%d/%Y")
            formatted_date = date_obj.strftime("%Y-%m-%d")
        except ValueError:
            raise Exception("Invalid date format. Use 'MM/DD/YYYY' format.")

        if not isinstance(royalties, (int, float)):
            raise Exception("Invalid royalties. Royalties should be an instance of the int class.")

        contract = Contract(author=self, book=book, date=formatted_date, royalties=royalties)
        self.contract_list.append(contract)  # Update the author's contract_list with the new contract
        return contract


    def total_royalties(self):
        return sum(contract.royalties for contract in self.contract_list)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author. Author should be an instance of the Author class.")

        if not isinstance(book, Book):
            raise Exception("Invalid book. Book should be an instance of the Book class.")

        if not isinstance(date, str):
            raise Exception("Invalid date. Date should be an instance of the str class.")

        if not isinstance(royalties, (int, float)):
            raise Exception("Invalid royalties. Royalties should be an instance of the int class.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]


