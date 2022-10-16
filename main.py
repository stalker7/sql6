import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from models import create_tables, Shop, Publisher, Book, Stock, Sale


DSN = 'postgresql://postgres:defender@localhost:5432/shop_book'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()
with open('list.json') as file:
    Data = json.load(file)

def add_data(data, **models):
    for record in data:
        model = models[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()



def command(publisher):
    query = session.query(Shop)
    query = query.join(Stock)
    query = query.join(Book)
    query = query.join(Publisher)
    if publisher.isdigit():
        query = query.filter(Publisher.id == publisher).all()
    else:
        query = query.filter(Publisher.name == publisher).all()
    if query:
        for record in query:
            print(record)

    else:
        print(f'издатель ({publisher}) не найден')


session.close()

if __name__ == '__main__':
    add_data(Data, publisher=Publisher, shop=Shop, book=Book, stock=Stock, sale=Sale)
    command(input(f'введите имя или id:'))


