from src.classes import Category, Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(
        f"product: {product1.name}\ndescription: {product1.description}\n"
        f"price: {product1.price}\nquantity: {product1.quantity}\n"
    )
    print(
        f"product: {product2.name}\ndescription: {product2.description}\n"
        f"price: {product2.price}\nquantity: {product2.quantity}\n"
    )
    print(
        f"product: {product3.name}\ndescription: {product3.description}\n"
        f"price: {product3.price}\nquantity: {product3.quantity}\n"
    )

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(
        f"category: {category1.name}\ndescription: {category1.description}\n"
        f"products: {len(category1.products)}\n-----\ncount_categories: {category1.category_count}\n"
        f"count_products: {category1.product_count}\n"
    )

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    print(
        f"product: {product4.name}\ndescription: {product4.description}\n"
        f"price: {product4.price}\nquantity: {product4.quantity}\n"
    )

    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(
        f"category: {category2.name}\ndescription: {category2.description}\n"
        f"products: {len(category2.products)}\n-----\ncount_categories: {category2.category_count}\n"
        f"count_products: {category2.product_count}\n"
    )
