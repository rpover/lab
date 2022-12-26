from models import Reader, Auth
from sql_base.base import BaseWorker


def get_reader(reader_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    reader = base_worker.insert_data('select * from reader where id=(?)', args=(int(reader_id),))
    return reader


def get_all_readers():
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    reader = base_worker.insert_data('select * from reader', args=(), many=True)
    return reader


def create_reader(new_reader):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    reader = base_worker.insert_data('insert into reader(name, surname, phone, address) values(?, ?, ?, ?)',
                                     args=(new_reader.name,
                                           new_reader.surname,
                                           new_reader.phone,
                                           new_reader.address),
                                     many=False)
    return reader
def delete_reader(reader_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    reader = base_worker.insert_data('delete from reader where id=(?)',
                                     args=(reader_id,),
                                     many=False)

    return reader


def change_reader(changed_reader):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    reader = base_worker.insert_data('update reader set (name, surname, phone, address) = (?, ?, ?, ?) where id=(?)',
                                     args=(changed_reader.name, changed_reader.surname, changed_reader.phone, changed_reader.address,changed_reader.id),
                                     many=False)

    return reader


def login(reader: Auth):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    query = "SELECT name FROM reader WHERE login = ? AND password = ?"
    name = base_worker.insert_data(query, (reader.login, reader.password), many=False)

    return name
