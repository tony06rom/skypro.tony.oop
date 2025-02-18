from src.classes import Product, Category
import pytest


def test_product_init():
    product = Product(name="Товар 1", description="Описание товара 1", price=100.50, quantity=10)
    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100.50
    assert product.quantity == 10


@pytest.fixture
def category():
    product1 = Product("Товар 1", "Описание товара 1", 100.00, 5)
    product2 = Product("Товар 2", "Описание товара 2", 200.00, 7)
    return Category("Категория 1", "Описание категории 1", [product1, product2])


def test_category_init(category):
    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert category.products == [category.products[0], category.products[1]]


def test_total_categories(category):
    assert Category.category_count == 2


def test_total_products(category):
    assert Category.product_count == 6
