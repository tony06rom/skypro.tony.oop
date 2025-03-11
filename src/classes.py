from typing import Any, Union, Optional


class Product:
    """Содержит информацию о продуктах"""


    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self)-> float:
        return self.__price


    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("# Цена не должна быть нулевая или отрицательная")
        else:
            if value < self.__price:
                user_input = input("# Снизить цену? ['y'/'n']\n===> ")
                if user_input.lower() == "y":
                    self.__price = value
            else:
                self.__price = value


    @classmethod
    def new_product(cls, params: dict[str, Any], product_list: Optional[list['Product']] = None)\
                                                                                                        -> 'Product':
        if product_list is not None:
            for product in product_list:
                if product.name == params["name"]:
                    product.price += params["price"]
                    if product.price < params["price"]:
                        product.price = params["price"]
        return Product(params["name"], params["description"], params["price"], params["quantity"])


class Category:
    """Содержит информацию о категориях и продуктах из класса Products"""

    category_count = 0  # Счётчик кол-ва выведенных категорий (всего)
    product_count = 0  # Счётчик кол-ва выведенных продуктов (всего)

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        product_count = len(self.__products)
        Category.product_count += product_count

    @property
    def products(self) -> str:
        products_list = ""
        for product in self.__products:
            products_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_list

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise Exception
