from models import Publishing_house
from sql_base.base import BaseWorker


def get_publishing_house(publishing_house_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    publishing_house = base_worker.insert_data('select * from publishing_house where id=(?)', args=(int(publishing_house_id),))
    return publishing_house


def get_all_publishing_houses():
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    publishing_house = base_worker.insert_data('select * from publishing_house', args=(), many=True)
    return publishing_house


def create_publishing_house(new_publishing_house):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    publishing_house = base_worker.insert_data('insert into publishing_house (name) values(?)',
                                     args=(new_publishing_house.name),
                                     many=False)
    return publishing_house


def delete_publishing_house(publishing_house_id):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    publishing_house = base_worker.insert_data('delete from publishing_house where id=(?)',
                                     args=(publishing_house_id,),
                                     many=False)

    return publishing_house


def change_publishing_house(changed_publishing_house):
    base_worker = BaseWorker()
    base_worker.set_base_path('sql_base/base.db')
    publishing_house = base_worker.insert_data('update reader set (name) = (?) where id=(?)',
                                     args=(changed_publishing_house.name),
                                     many=False)

    return publishing_house