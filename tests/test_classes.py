import pytest

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
    assert category.products == "Товар 1, 100.0 руб. Остаток: 5 шт.\nТовар 2, 200.0 руб. Остаток: 7 шт.\n"


def test_total_categories(category):
    assert Category.category_count == 2


def test_total_products(category):
    assert Category.product_count == 6


def test_price_setter_getter(capsys) -> None:
    product = Product("Xiaomi 30T", "Топ за свои деньги", 55000, 3)
    product.price = 100000
    assert product.price == 100000
    product.price = 0
    captured = capsys.readouterr()
    assert captured.out == "# Цена не должна быть нулевая или отрицательная\n"


def test_new_product() -> None:
    product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0


def test_add_product() -> None:
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    category.add_product(product)
    assert category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    with pytest.raises(Exception):
        category.add_product(category)
