import fastapi
import resolves.author
from models import Author

router = fastapi.APIRouter(prefix='/authors', tags=['authors'])


@router.get('/get_author/{author_id}')
def get_rauthor(author_id):
    return resolves.author.get_author(author_id)



@router.get('/get_all_author')
def get_all_authors():
    return resolves.author.get_all_authors()


@router.post('/create_author')
def create_author(new_author: Author):
    return resolves.author.create_author(new_author)


@router.get('/delete_author/{author_id}')
def delete_author(author_id):
    resolves.author.delete_author(author_id)


@router.put('/change')
def change_author(changed_author: Author):
    resolves.author.change_author(changed_author)
