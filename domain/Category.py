


class Category:


    def __init__(self, id_category, description):
        self.id_category = id_category
        self.description = description

    @staticmethod
    def from_row(row):
        return Category(row[0], row[1])

    def __str__(self):
        return f"Categoria: {self._id_category}, Descripción:  {self._description}"

    def __repr__(self):
        return self.__str__()

    @property
    def category(self):
        return self.id_category

    @category.setter
    def category(self, category):
        self.category = category


    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, description):
        self.description = description