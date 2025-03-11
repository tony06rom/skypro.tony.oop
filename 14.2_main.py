from src.classes import Category, Product


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(f"1 принт: {category1.products}")
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(f"2 принт: {category1.products}")
    print(f"3 принт: {category1.product_count}")

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(f"4 принт: {new_product.name}")
    print(f"5 принт: {new_product.description}")
    print(f"6 принт: {new_product.price}")
    print(f"7 принт: {new_product.quantity}")

    new_product.price = 800
    print(f"8 принт: {new_product.price}")

    # new_product.price = -100
    # print(f"9 принт: {new_product.price}")
    # new_product.price = 0
    # print(f"10 принт: {new_product.price}")

    print(f"11 принт: {category1.products}")
