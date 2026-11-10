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

    def __str__(self) -> str:
        quantity = 0
        for product in self._products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, product: Product) -> None:
        if issubclass(type(product), Product):
            self._products.append(product)
            self.product_count += 1
        else:
            raise TypeError("Объект не является продуктом")

    @classmethod
    def get_all_categories(cls) -> list:
        return Category.__all_categories

    @property
    def products(self) -> str:
        ans = ""
        for product in self._products:
            ans += product.__str__()
        return ans


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

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other: Product) -> float | int:
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Нельзя сложить стоимость продуктов разных категорий")

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
