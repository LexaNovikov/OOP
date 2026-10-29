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
            ans += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return ans


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    #
    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)
    #
    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
    #
    # print(product3.name)
    # print(product3.description)
    # print(product3.price)
    # print(product3.quantity)

    smartphones = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(smartphones.name == "Смартфоны")
    print(smartphones.description)
    # print(len(smartphones.products))
    print(smartphones.category_count)
    print(smartphones.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    # print(len(category2.products))
    # print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
    product5 = Product.new_product({"name": "Имя", "description": "Описание", "price": 10.0, "quantity": 15})
    print(product5.name)
    print(product5.price)
    print(product5.description)
    print(product5.description)
    print(product5.description)
    print(product5.description)
    print(product5.description)
    print(product5.description)
    smartphones.add_product(product5)
    test = smartphones.products
    print(test)
    print(Category.get_all_categories())
    product6 = Product.new_product({"name": "Имя", "description": "Описание", "price": 5.0, "quantity": 15})
    print(smartphones.products)
