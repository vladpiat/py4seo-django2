from  time import time


def timelog(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Time is: {round(t2-t1, 10)} sec ')
        return result
    return wrapper()

class Product:
    product = 'some product'
    __meta = 'Analytics signal'

    @timelog
    def add_to_cart(self, count):
        print(f'Add {count} products [{self.product}] to cart')

    def edit_description(self):
        print('Edit descr')

    def add_review(self, text):
        print(f'Add review {text}')


class Book(Product ):

    pages = 398
    author = 'author'

    @timelog
    def __init__(self, name, author, pages):
        self.name = self.product = name
        self.author = author
        self. pages = pages

    def __add__(self, other):
        return Book(
            name=f'{self.name} | {other.name}',
            author=f'{self.author} | {other.author}',
            pages=self.pages+other.pages
        )

    def get_pages(self):
        print(f'Pages count: {self.pages}')
