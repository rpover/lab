import fastapi
import resolves.reader
from models import Reader, Auth

router = fastapi.APIRouter(prefix='/readers', tags=['readers'])


@router.get('/get_reader/{reader_id}')
def get_reader(reader_id):
    return resolves.reader.get_reader(reader_id)



@router.get('/get_all_readers')
def get_all_readers():
    return resolves.reader.get_all_readers()


@router.post('/create_reader')
def create_reader(new_reader: Reader):
    return resolves.reader.create_reader(new_reader)


@router.get('/delete_reader/{reader_id}')
def delete_reader(reader_id):
    resolves.reader.delete_reader(reader_id)


@router.put('/change')
def change_reader(changed_reader: Reader):
    resolves.reader.change_reader(changed_reader)


@router.post('/login')
def reader_login(reader: Auth):
    return resolves.reader.login(reader)