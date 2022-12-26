import fastapi
import resolves.book
from models import Book


router = fastapi.APIRouter(prefix='/books', tags=['books'])

@router.get('/get_book/{book_id}')
def get_reader(book_id):
    return resolves.book.get_book(book_id)


@router.get('/get_all_books')
def get_all_books():
    return resolves.book.get_all_books()


@router.post('/create_book')
def create_Book(new_Book: Book):
    return resolves.book.create_book(new_book)


@router.get('/delete_book/{book_id}')
def delete_book(book_id):
    resolves.book.delete_book(book_id)


@router.put('/change')
def change_book(changed_book: Book):
    resolves.book.change_book(changed_book)
