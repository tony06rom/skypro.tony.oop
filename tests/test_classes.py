import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


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


def test_category_str(category: Category) -> None:
    assert str(category) == "Категория 1, количество продуктов: 12 шт."


def test_product_str(product1: Product, product2: Product) -> None:
    assert str(product1) == "Товар 1, 100.0 руб. Остаток: 5 шт."
    assert str(product2) == "Товар 2, 200.0 руб. Остаток: 7 шт."


def test_product_add(product1: Product, product2: Product) -> None:
    assert product1.price == 100.0
    assert product2.price == 200.0
    assert product1.quantity == 5
    assert product2.quantity == 7
    cost_product1 = product1.price * product1.quantity
    cost_product2 = product2.price * product2.quantity
    total_cost = cost_product1 + cost_product2
    assert product1 + product2 == 1900.0
    assert product1 + product2 == total_cost


def test_smartphone(fix_smartphones) -> None:
    phone = fix_smartphones
    assert phone.name == "iPhone"
    assert phone.model == "15"
    assert phone.color == "Blue"
    assert issubclass(phone.__class__, Product)


def test_lawn_grass(fix_lawn_grass) -> None:
    grass = fix_lawn_grass
    assert grass.name == "Grunt"
    assert grass.description == "Clear black grass"
    assert grass.price == 500
    assert grass.quantity == 30
    assert grass.color == "black"
    assert issubclass(grass.__class__, Product)


def test_product_sum(fix_smartphones, fix_lawn_grass) -> None:
    phone = fix_smartphones
    grass = fix_lawn_grass
    with pytest.raises(TypeError):
        result = phone + grass
        return result
