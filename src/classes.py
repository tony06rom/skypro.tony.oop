class Product:
    """Содержит информацию о продуктах"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Содержит информацию о категориях и продуктах из класса Products"""

    category_count = 0  # Счётчик кол-ва выведенных категорий (всего)
    product_count = 0  # Счётчик кол-ва выведенных продуктов (всего)

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        product_count = len(self.products)
        Category.product_count += product_count
