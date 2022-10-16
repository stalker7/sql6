import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(90), unique=True)

    def __str__(self):
        return f'Shop {self.id}: {self.name}'


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), unique=True)

    def __str__(self):
        return f'Publisher {self.id}: {self:name}'


class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(100), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='book')

    def __str__(self):
        return f'Book {self.id}: ({self.title}, {self.id_publisher})'


class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    book = relationship(Book, backref='book')
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    shop = relationship(Shop, backref='shop')
    count = sq.Column(sq.Integer, nullable=False)

    def __str__(self):
        return f'Stock {self.id}: ({self.id_book}, {self.id_shop}, {self.count})'

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.DECIMAL(6, 2), nullable=False)
    date_sale = sq.Column(sq.DateTime)
    count = sq.Column(sq.Integer, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    stock = relationship(Stock, backref='sale')

    def __str__(self):
        return f'Sale {self.id}: ({self.price}, {self.date_sale}, {self.count}, {self.id_stock})'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)



