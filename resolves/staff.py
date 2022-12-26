from models import Staff
from sql_base.base import BaseWorker


def get_staff(staff_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    staff = base_worker.insert_data('select * from staff where id=(?)', args=(int(staff_id),))
    return staff


def get_all_staffs():
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    staff = base_worker.insert_data('select * from staff', args=(), many=True)
    return staff


def create_staff(new_staff):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    staff = base_worker.insert_data('insert into staff(name, surname, phone, post) values(?, ?, ?, ?)',
                                     args=(new_staff.name,
                                           new_staff.surname,
                                           new_staff.phone,
                                           new_staff.post),
                                     many=False)
    return staff


def delete_staff(staff_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    staff = base_worker.insert_data('delete from staff where id=(?)',
                                     args=(staff_id,),
                                     many=False)

    return staff


def change_staff(changed_staff):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    staff = base_worker.insert_data('update staff set (name, surname, phone, post) = (?, ?, ?, ?) where id=(?)',
                                     args=(changed_staff.name, changed_staff.surname, changed_staff.phone, changed_staff.post,changed_staff.id),
                                     many=False)

    return staff