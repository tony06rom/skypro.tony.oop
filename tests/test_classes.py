from src.classes import Category, Product


def test_product_init():
    product = Product(name="Товар 1", description="Описание товара 1", price=100.50, quantity=10)
    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100.50
    assert product.quantity == 10


def test_category_init(category):
    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert category.products == [category.products[0], category.products[1]]


def test_total_categories(category):
    assert Category.category_count == 2


def test_total_products(category):
    assert Category.product_count == 6
