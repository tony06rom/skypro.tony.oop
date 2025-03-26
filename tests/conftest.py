import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def category() -> Category:
    product1 = Product("Товар 1", "Описание товара 1", 100.00, 5)
    product2 = Product("Товар 2", "Описание товара 2", 200.00, 7)
    return Category("Категория 1", "Описание категории 1", [product1, product2])


@pytest.fixture
def category_2() -> Category:
    product3 = Product("Товар 3", "Описание товара 1", 70, 3)
    product4 = Product("Товар 4", "Описание товара 2", 335000, 6)
    return Category("Категория 2", "Описание категории 2", [product3, product4])


@pytest.fixture
def product1() -> Product:
    return Product(name="Товар 1", description="256GB, Описание товара 1", price=100.00, quantity=5)


@pytest.fixture
def product2() -> Product:
    return Product(name="Товар 2", description="Описание товара 2", price=200.00, quantity=7)


@pytest.fixture
def fix_lawn_grass():
    grass = LawnGrass("Grunt", "Clear black grass", 500, 30, "RUS", "1 month", "black")
    return grass


@pytest.fixture
def fix_smartphones():
    phone = Smartphone("iPhone", "Best", 79000, 5, "Apple", "15", "256Gb", "Blue")
    return phone
