import fastapi
import resolves.publishing_house
from models import Publishing_house

router = fastapi.APIRouter(prefix='/publishing_houses', tags=['publishing_houses'])


@router.get('/get_publishing_house/{publishing_house_id}')
def get_publishing_house(publishing_house_id):
    return resolves.publishing_house.get_publishing_house(publishing_house_id)



@router.get('/get_all_publishing_houses')
def get_all_publishing_houses():
    return resolves.publishing_house.get_all_publishing_houses()


@router.post('/create_publishing_house')
def create_publishing_house(new_publishing_house: Publishing_house):
    return resolves.publishing_house.create_publishing_house(new_publishing_house)


@router.get('/delete_publishing_house/{publishing_house_id}')
def delete_publishing_house(publishing_house_id):
    resolves.publishing_house.delete_publishing_house(publishing_house_id)


@router.put('/change')
def change_publishing_house(changed_publishing_house: Publishing_house):
    resolves.publishing_house.change_publishing_house(changed_publishing_house)