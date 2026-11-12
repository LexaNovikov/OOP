from src.classes import Category


class CategoryIter:
    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = -1

    def __iter__(self) -> CategoryIter:
        return self

    def __next__(self):
        if self.index + 1 < len(self.category._products):
            self.index += 1
            return self.category._products[self.index]
        else:
            raise StopIteration
