from abc import ABC, abstractmethod
from typing import Any, Optional


class MixinLog:
    """Выводит информацию об объекте в консоль"""

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        values = list(vars(self).values())
        return f"{self.__class__.__name__}({", ".join([str(item) for item in values])})"


class BaseProduct(ABC):
    """Абстрактный класс для Product (шаблон)"""

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> Any:
        pass


class Product(BaseProduct, MixinLog):
    """Содержит информацию о продуктах"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @property
    def price(self) -> float:
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
    def new_product(cls, params: dict[str, Any], product_list: Optional[list["Product"]] = None) -> "Product":
        if product_list is not None:
            for product in product_list:
                if product.name == params["name"]:
                    product.price += params["price"]
                    if product.price < params["price"]:
                        product.price = params["price"]
        return Product(params["name"], params["description"], params["price"], params["quantity"])

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        if type(self) is type(other):
            return self.price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError


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
        if isinstance(product, Product) or issubclass(self.__class__, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise TypeError

    def __str__(self) -> str:
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."


class CategoryIterNext:
    """Перебирает товары одной категории"""

    def __init__(self, category: Any):
        self.category = category
        self.num_product = 0

    def __iter__(self) -> "CategoryIterNext":
        self.num_product = 0
        return self

    def __next__(self) -> Any:
        if self.num_product <= len(self.category.products):
            product = self.category.products[self.num_product]
            self.num_product += 1
            return product
        else:
            raise StopIteration


class Smartphone(Product):
    """Расширение класса Product для смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Расширение класса Product для газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
