import pytest

from src.classes import Category, Product


def test_product_init():
    product = Product(name="Товар 1", description="Описание товара 1", price=100.50, quantity=10)
    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100.50
    assert product.quantity == 10


def test_category_init(fix_category):
    assert fix_category.name == "Категория 1"
    assert fix_category.description == "Описание категории 1"
    assert fix_category.products == "Товар 1, 100.0 руб. Остаток: 5 шт.\nТовар 2, 200.0 руб. Остаток: 7 шт.\n"


def test_total_categories(fix_category):
    assert Category.category_count == 2


def test_total_products(fix_category):
    assert Category.product_count == 6


def test_price_setter_getter(capsys) -> None:
    product = Product("Xiaomi 30T", "Топ за свои деньги", 55000, 3)
    captured = capsys.readouterr()
    assert captured.out == "Product(Xiaomi 30T, Топ за свои деньги, 55000, 3)\n"
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


def test_category_str(fix_category: Category) -> None:
    assert str(fix_category) == "Категория 1, количество продуктов: 12 шт."


def test_product_str(fix_product1: Product, fix_product2: Product) -> None:
    assert str(fix_product1) == "Товар 1, 100.0 руб. Остаток: 5 шт."
    assert str(fix_product2) == "Товар 2, 200.0 руб. Остаток: 7 шт."


def test_product_add(fix_product1: Product, fix_product2: Product) -> None:
    assert fix_product1.price == 100.0
    assert fix_product2.price == 200.0
    assert fix_product1.quantity == 5
    assert fix_product2.quantity == 7
    cost_product1 = fix_product1.price * fix_product1.quantity
    cost_product2 = fix_product2.price * fix_product2.quantity
    total_cost = cost_product1 + cost_product2
    assert fix_product1 + fix_product2 == 1900.0
    assert fix_product1 + fix_product2 == total_cost


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


def test_print_mixinlog(capsys, fix_lawn_grass) -> None:
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Grunt, Clear black grass, 500, 30)"


def test_add_product_zero_quantity(capsys) -> None:
    with pytest.raises(ValueError):
        Product(name="Товар 1", description="256GB, Описание товара 1", price=100.00, quantity=0)
        message = capsys.readouterr()
        assert message.out.strip() == "Товар с нулевым количеством не может быть добавлен"


@pytest.fixture
def smartphones() -> Category:
    phone_1 = Product("Xiaomi 30T", "Топ за свои деньги", 55000, 3)
    phone_2 = Product("Samsung Galaxy S25", "Просто топ", 125000, 5)
    return Category("Смартфоны", "Описание", [phone_1, phone_2])


def test_middle_price(fix_category) -> None:
    empty_category = Category("Empty Category", "Empty description", [])
    not_empty_category = fix_category
    assert empty_category.middle_price() == 0
    assert not_empty_category.middle_price() == 25.0
