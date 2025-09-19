from repository.Conexion import conexion

class Category_Repository:


    def __init__(self,):
        self.db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        self.db.connect()


    def create_category_db(self,category):

        query =   "INSER INTO category (description) VALUES (%s)"
        values = (category.description,)
        self.db.execute_query(query, values)

