# Databricks notebook source

# COMMAND ----------

# Analysis notebook created on GitHub!

df = spark.createDataFrame(
    [(1, 100), (2, 200), (3, 300)],
    ["product_id", "sales"]
)

df.show()

# COMMAND ----------

summary = df.agg({"sales": "sum"}).collect()[0][0]
print(f"Total Sales: ${summary:,}")
