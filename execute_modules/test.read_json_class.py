from src.classes import Category
from src.read_json_class import load_json_file_with_classes

categories = load_json_file_with_classes("products")

for category in categories:
    print(f"category: {category.name}")
    print(f"description: {category.description}")
    print("products:")
    for product in category.products:
        print(f"  - {product.name}: {product.description} (price: {product.price}, quantity: {product.quantity})")
    print()

print(f"count_categories: {Category.category_count}")
print(f"count_products: {Category.product_count}")
