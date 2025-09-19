from domain.Category import Category
from repository.Category_Repository import Category_Repository


class Category_Service:


    def __init__(self):
        self.category = Category(None, None)
        self.category_repository = Category_Repository()

        description = input("Ingrese el nombre de la categoria a crear")
        self.category.description = description




    def create_category(self):
        self.category_repository.create_category_db(self.category)
