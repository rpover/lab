import fastapi
import resolves.extradition_duration
from models import Extradition_duration

router = fastapi.APIRouter(prefix='/extradition_durations', tags=['extradition_durations'])


@router.get('/get_extradition_duration/{extradition_duration_id}')
def get_reader(extradition_duration_id):
    return resolves.extradition_duration.get_extradition_duration(extradition_duration_id)



@router.get('/get_all_extradition_durations')
def get_all_extradition_durations():
    return resolves.extradition_duration.get_all_extradition_durations()


@router.post('/create_extradition_duration')
def create_extradition_duration(new_extradition_duration: Extradition_duration):
    return resolves.extradition_duration.create_extradition_duration(new_extradition_duration)


@router.get('/delete_extradition_duration/{extradition_duration_id}')
def delete_extradition_duration(extradition_duration_id):
    resolves.extradition_duration.delete_extradition_duration(extradition_duration_id)


@router.put('/change')
def change_extradition_duration(changed_extradition_duration: Extradition_duration):
    resolves.extradition_duration.change_extradition_duration(changed_extradition_duration)