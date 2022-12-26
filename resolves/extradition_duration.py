from models import Extradition_duration
from sql_base.base import BaseWorker


def get_extradition_duration(extradition_duration_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    extradition_duration = base_worker.insert_data('select * from extradition_duration where id=(?)', args=(int(extradition_duration_id),))
    return extradition_duration


def get_all_extradition_durations():
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    extradition_duration = base_worker.insert_data('select * from extradition_duration', args=(), many=True)
    return extradition_duration


def create_extradition_duration(new_extradition_duration):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    extradition_duration = base_worker.insert_data('insert into extradition_duration(date_start, date_end, book_id, reader_id) values(?, ?, ?, ?)',
                                     args=(new_extradition_duration.date_start,
                                           new_extradition_duration.date_end,
                                           new_extradition_duration.book_id,
                                           new_extradition_duration.reader_id),
                                     many=False)
    return extradition_duration


def delete_extradition_duration(extradition_duration_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    extradition_duration = base_worker.insert_data('delete from extradition_duration where id=(?)',
                                     args=(extradition_duration_id,),
                                     many=False)

    return extradition_duration


def change_extradition_duration(changed_extradition_duration):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    extradition_duration = base_worker.insert_data('update extradition_duration set (date_start, date_end, book_id, reader_id) = (?, ?, ?, ?) where id=(?)',
                                     args=(changed_extradition_duration.date_start, changed_extradition_duration.date_end, changed_extradition_duration.book_id, changed_extradition_duration.reader_id,changed_extradition_duration.id),
                                     many=False)

    return extradition_duration