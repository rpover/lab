from models import Staff
import fastapi

router = fastapi.APIRouter(prefix='/staff', tags=['staffs'])


@router.get('/get_staff/{staff_id}')
def get_staff(staff_id):
    return resolves.staff.get_staff(staff_id)



@router.get('/get_all_staff')
def get_all_staff():
    return resolves.staff.get_all_staffs()


@router.post('/create_staff')
def create_staff(new_staff: Staff):
    return resolves.staff.create_staff(new_staff)


@router.get('/delete_staff/{staff_id}')
def delete_staff(staff_id):
    resolves.staff.delete_staff(staff_id)


@router.put('/change')
def change_staff(changed_staff: Staff):
    resolves.staff.change_staff(changed_staff)