import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Base, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:sav2210x@localhost:5432/book_shop_db'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
print('Таблицы удалены')
Base.metadata.create_all(engine)
print('Таблицы созданы')

publisher1 = Publisher(name='Иванов Иван Иванович')
publisher2 = Publisher(name='Петров Петр Петрович')
publisher3 = Publisher(name='Сергеев Сергей Сергеевич')
publishers = [publisher1, publisher2, publisher3]
session.add_all(publishers)
session.commit()

shop1 = Shop(name='Магазин 1')
shop2 = Shop(name='Магазин 2')
shop3 = Shop(name='Магазин 3')
shop4 = Shop(name='Магазин 4')
shops = [shop1, shop2, shop3, shop4]
session.add_all(shops)
session.commit()


book1 = Book(title='Книга 1', id_publisher=publisher1.id)
book2 = Book(title='Книга 2', id_publisher=publisher2.id)
book3 = Book(title='Книга 3', id_publisher=publisher3.id)
books = [book1, book2, book3]
session.add_all(books)
session.commit()

stock1 = Stock(id_book=book1.id, id_shop=shop1.id, count=100)
stock2 = Stock(id_book=book1.id, id_shop=shop2.id, count=200)
stock3 = Stock(id_book=book1.id, id_shop=shop3.id, count=300)
stock4 = Stock(id_book=book1.id, id_shop=shop4.id, count=400)
stock5 = Stock(id_book=book2.id, id_shop=shop1.id, count=500)
stock6 = Stock(id_book=book2.id, id_shop=shop2.id, count=600)
stock7 = Stock(id_book=book2.id, id_shop=shop3.id, count=700)
stock8 = Stock(id_book=book2.id, id_shop=shop4.id, count=800)
stock9 = Stock(id_book=book3.id, id_shop=shop1.id, count=900)
stock10 = Stock(id_book=book3.id, id_shop=shop2.id, count=1000)
stock11 = Stock(id_book=book3.id, id_shop=shop3.id, count=1100)
stock12 = Stock(id_book=book3.id, id_shop=shop4.id, count=1200)
stocks = [stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10, stock11, stock12]
session.add_all(stocks)
session.commit()

sale1 = Sale(price=100, date_sale='2022-01-01', id_stock=stock1.id, count=10)
sale2 = Sale(price=200, date_sale='2022-01-02', id_stock=stock2.id, count=20)
sale3 = Sale(price=300, date_sale='2022-01-03', id_stock=stock3.id, count=30)
sale4 = Sale(price=400, date_sale='2022-01-04', id_stock=stock4.id, count=40)
sale5 = Sale(price=500, date_sale='2022-01-05', id_stock=stock5.id, count=50)
sale6 = Sale(price=600, date_sale='2022-01-06', id_stock=stock6.id, count=60)
sale7 = Sale(price=700, date_sale='2022-01-07', id_stock=stock7.id, count=70)
sale8 = Sale(price=800, date_sale='2022-01-08', id_stock=stock8.id, count=80)
sale9 = Sale(price=900, date_sale='2022-01-09', id_stock=stock9.id, count=90)
sale10 = Sale(price=1000, date_sale='2022-01-10', id_stock=stock10.id, count=100)
sale11 = Sale(price=1100, date_sale='2022-01-11', id_stock=stock11.id, count=110)
sale12 = Sale(price=1200, date_sale='2022-01-12', id_stock=stock12.id, count=120)
sales = [sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10, sale11, sale12]
session.add_all(sales)
session.commit()


publisher_input = input('Ведите имя или ID издателя: ')

try:
    publisher_id = int(publisher_input)
    publisher = session.query(Publisher).filter(Publisher.id == publisher_id).one()
except ValueError:
    publisher = session.query(Publisher).filter(Publisher.name == publisher_input).one()

if publisher is None:
    print('Такого издателя нет')
else:
    sales = (session.query(Sale)
             .join(Stock)
             .join(Stock.shop)
             .join(Book)
             .join(Publisher)
             .filter(Publisher.id == publisher.id)
             .all())

    for sale in sales:
        print(f'{sale.stock.book.title} | {sale.stock.shop.name} | {sale.price} | {sale.date_sale}')

session.close()









