from models import Book
from sql_base.base import BaseWorker


def get_book(book_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    book = base_worker.insert_data('select * from book where id=(?)', args=(int(book_id),))
    return book


def get_all_books():
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    book = base_worker.insert_data('select * from book', args=(), many=True)
    return book


def create_book(new_book):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    book = base_worker.insert_data('insert into book (name, author_id, year, page_count, publishing_house_id) values(?, ?, ?, ?,?)',
                                     args=(new_book.name,
                                           new_book.author_id,
                                           new_book.year,
                                           new_book.page_count,
                                           new_book.publishing_house_id),
                                     many=False)
    return book
def delete_book(book_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    reader = base_worker.insert_data('delete from reader where id=(?)',
                                     args=(book_id,),
                                     many=False)


    return book
def change_book(changed_book):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    book = base_worker.insert_data('update reader set (name, author_id, year, page_count, publishing_house_id) = (?, ?, ?, ?) where id=(?)',
                                     args=(changed_book.name, changed_book.author_id, changed_book.year, changed_book.page_count,changed_book.publishing_house_id,changed_book.id),
                                     many=False)

    return book


