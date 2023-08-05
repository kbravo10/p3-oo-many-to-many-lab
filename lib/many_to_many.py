class Author:
    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        con = []
        for contract in Contract.contracts:
            if self in contract:
                con.append(contract[0])
        return con
        
    def books(self):
        books_list = []
        for contract in Contract.contracts:
            if self in contract:
                books_list.append(contract[2])
        return books_list

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        sum_royalties = 0
        for contract in Contract.contracts:
            if self in contract:
                sum_royalties += contract[4]
        return sum_royalties


class Book:
    def __init__(self, title):
        self.title = title
    
    def contracts(self):
        con = []
        for contract in Contract.contracts:
            if self in contract:
                con.append(contract[0])
        return con

    def authors(self):
        author_list = []
        for contract in Contract.contracts:
            if self in contract:
                author_list.append(contract[1])
        return author_list

class Contract:
    contracts = []
    def __init__(self, author, book, date, royalties):
        if(isinstance(author, Author) & isinstance(book, Book) & (type(date) == str) & (type(royalties) == int)):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.contracts.append([self, author, book, date, royalties])
        else:
            raise Exception("Not valid")
        
    def contracts_by_date():
        new_list = [Contract.contracts[-1],Contract.contracts[-2], Contract.contracts[-3]]
        print(new_list)
        sort = sorted(new_list,key=lambda contract: contract[3])
        
        new_con = []
        for contracts in sort:
            new_con.append(contracts[0])
        return(new_con)