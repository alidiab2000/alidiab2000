from fastapi import FastAPI , Body
from pydantic import BaseModel
app = FastAPI()

class Book:
    id : int 
    title : str 
    author : str 
    description : str 
    rating : int

    def __init__(self , id , title ,author, description , rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description 
        self.rating = rating

class BookRequest(BaseModel):
    id : int 
    title : str 
    author : str 
    description : str 
    rating : int 


BOOKS = [
    Book(
        id = 1,
        title = "Copumter Science" ,
        author = "Shakespeare" ,
        description = "A book about Computer Science" ,
        rating = 5
        ),
    Book(
        id = 2,
        title = "The Lord of the Rings" ,
        author = "Tolkein" ,
        description = "A book about Lord of the Rings" ,
        rating = 4 
    ),
    Book(
        id = 3,
        title = "The Shining" ,
        author = "Stephen King" ,
        description ="A book about Horror" ,
        rating=3 
    ), 
    Book(
        id = 4,
        title = "The Hobbit" ,
        author ="Tolkien" ,
        description = "A book about adventure" ,
        rating= 2 
    )
]

@app.get("/books")
def read_all_books():
    return BOOKS

@app.post("/create_book" )
def craete_new_book(book_new :BookRequest):
        BOOKS.append(Book(**book_new.model_dump()))