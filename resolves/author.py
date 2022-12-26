from models import Author
from sql_base.base import BaseWorker


def get_author(author_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    author = base_worker.insert_data('select * from author where id=(?)', args=(int(author_id),))
    return author


def get_all_authors():
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    author = base_worker.insert_data('select * from author', args=(), many=True)
    return author


def create_author(new_author):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    author = base_worker.insert_data('insert into author(name, surname, born_year, dead_year) values(?, ?, ?, ?)',
                                     args=(new_author.name,
                                           new_author.surname,
                                           new_author.born_year,
                                           new_author.ead_year),
                                     many=False)
    return author


def delete_author(author_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    author = base_worker.insert_data('delete from author where id=(?)',
                                     args=(author_id,),
                                     many=False)

    return author


def change_author(changed_author):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    author = base_worker.insert_data('update author set (name, surname, born_year, dead_year) = (?, ?, ?, ?) where id=(?)',
                                     args=(changed_author.name, changed_author.surname, changed_author.born_year, changed_author.dead_year, changed_author.id),
                                     many=False)

    return author