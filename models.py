from pydantic import BaseModel
from typing import Optional


class Reader (BaseModel):
    id: Optional[int]
    name:str
    surname:str
    phone:int
    address:str
    login: str
    password: str


class Book (BaseModel):
    id: Optional[int]
    name:str
    author_id:int
    year:str
    page_count:int
    publishing_house_id:int


class Staff (BaseModel):
    id: Optional[int]
    name: str
    surname: str
    phone: int
    post: str


class Author (BaseModel):
    id: Optional[int]
    name: str
    surname: str
    born_year: str
    dead_year: str


class Publishing_house (BaseModel):
    id: Optional[int]
    name: str


class Extradition_duration (BaseModel):
    id: Optional [int]
    date_start: str
    date_end: str
    book_id: int
    reader_id: int


class Auth(BaseModel):
    login: str
    password: str