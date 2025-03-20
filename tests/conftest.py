import pytest

from src.classes import Category, Product


@pytest.fixture
def category():
    product1 = Product("Товар 1", "Описание товара 1", 100.00, 5)
    product2 = Product("Товар 2", "Описание товара 2", 200.00, 7)
    return Category("Категория 1", "Описание категории 1", [product1, product2])
