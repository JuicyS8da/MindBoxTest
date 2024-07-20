from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("PySpark_Task") \
    .getOrCreate()

categories_df = spark.createDataFrame(
    [
        (1, 'Fruits'),
        (2, 'Vegetables'),
        (3, 'Meat'),
        (4, 'Sweets'),
        (5, 'Dairy'),
        (6, 'Cereal'),
        (7, 'Bakery')
    ],
    ['category_id', 'category_name'],
)

products_df = spark.createDataFrame(
    [
        (1, 'Wheat'),
        (2, 'Oatmeal'),
        (3, 'Millet'),
        (4, 'Pearl-barley'),
        (5, 'Rice'),
        (6, 'Buckwheat'),
        (7, 'Flour'),
        (8, 'Salt'),
        (9, 'Dark chocolate'),
        (10, 'Milk Chocolate'),
        (11, 'Apples'),
        (12, 'Pears'),
        (13, 'Bananas'),
        (14, 'Cucumbers'),
        (15, 'Tomatoes'),
        (16, 'Lettuce'),
        (17, 'Bacon'),
        (18, 'Beef'),
        (19, 'Mutton'),
        (20, 'Biscuits'),
        (21, 'Cake'),
        (22, 'Donut')
    ],
    ['product_id', 'product_name']
)

products_categories_relation_df = spark.createDataFrame(
    [
        (1, 6),
        (2, 6),
        (3, 6),
        (4, 6),
        (5, 6),
        (6, 6),
        (7, None),
        (8, None),
        (9, 4),
        (10, 4),
        (11, 1),
        (12, 1),
        (13, 1),
        (14, 2),
        (15, 2),
        (16, 2),
        (17, 3),
        (18, 3),
        (19, 3),
        (20, 7),
        (21, 7),
        (22, 7),
    ],
    ['product_id', 'category_id']
)

product_category_joined_df = products_categories_relation_df.join(
    products_df,
    products_categories_relation_df.product_id == products_df.product_id,
    "right"
).join(
    categories_df,
    products_categories_relation_df.category_id == categories_df.category_id,
    "left"
).select(
    products_df.product_name,
    categories_df.category_name
)

products_no_category_df = product_category_joined_df.filter(col("category_name").isNull()).select("product_name").distinct()

product_category_joined_df = product_category_joined_df.na.fill({"category_name": "No Category"})

print("Пары 'Имя продукта – Имя категории':")
product_category_joined_df.show()

print("Продукты без категорий:")
products_no_category_df.show()