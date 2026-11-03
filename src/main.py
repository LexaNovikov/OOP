class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"
    def __add__(self, other: Product) -> float | int:
        return self.price*self.quantity + other.price*other.quantity
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price > 0:
            self.__price = price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_dict: dict) -> Product:
        product = cls(
            product_dict["name"], product_dict["description"], product_dict["price"], product_dict["quantity"]
        )
        for category in Category.get_all_categories():
            for idx, product_from_list in enumerate(category._products):
                if product_from_list.name == product.name:
                    if product_from_list.price > product.price:
                        ans = input(
                            f"Новая цена {product.price} меньше предыдущей {product_from_list.price}\n"
                            f"Поменять цену на новую? (Y/n)"
                        )
                        while ans.lower().strip() not in ["", "y", "n"]:
                            print(
                                f"Некорректный ввод. Введите y или n\n"
                                f"Новая цена {product.price} меньше предыдущей {product_from_list.price}\n"
                                f"Поменять цену на новую? (Y/n)"
                            )
                            ans = input()
                        if ans.lower().strip() not in ["y", ""]:
                            product.price = product_from_list.price
                    product.quantity += product_from_list.quantity
                    category._products[idx] = product
        return product


class Category:
    name: str
    description: str
    _products: list
    category_count: int = 0
    product_count: int = 0
    __all_categories: list = []

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products = products
        Category.category_count += 1
        self.product_count = len(products)
        Category.__all_categories.append(self)
    def __str__(self):
        quantity = 0
        for product in self._products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."
    def add_product(self, product: Product) -> None:
        self._products.append(product)
        self.product_count += 1

    @classmethod
    def get_all_categories(cls) -> list:
        return Category.__all_categories
    @property
    def products(self) -> str:
        ans = ""
        for product in self._products:
            ans += product.__str__()
        return ans

class CategoryIter:
    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index+1 < len(self.category._products):
            self.index += 1
            return self.category._products[self.index]
        else:
            raise StopIteration
if __name__ == "__main__":
    if __name__ == '__main__':
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        print(str(product1))
        print(str(product2))
        print(str(product3))

        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3]
        )

        print(str(category1))

        print(category1.products)

        print(product1 + product2)
        print(product1 + product3)
        print(product2 + product3)
