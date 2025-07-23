
# Retail CDC Example - Simplified for Databricks Community Edition
# Author: Adapted by ChatGPT

from pyspark.sql.functions import *
from pyspark.sql.types import *

# Define the path to raw customer data
source_path = "/databricks-datasets/retail-org/customers/"

# Step 1: Load raw data (Bronze Layer equivalent)
raw_customers = (
    spark.read
    .format("json")
    .load(source_path)
)

# Register as temp view for SQL use (optional)
raw_customers.createOrReplaceTempView("raw_customers")

# Display raw data
print("🟫 Raw Customer Data (Bronze Layer):")
display(raw_customers)

# Step 2: Clean and transform data (Silver Layer equivalent)
customers_cleaned = raw_customers.filter("customer_id IS NOT NULL")

# Show result
print("⬜ Cleaned Customer Data (Silver Layer):")
display(customers_cleaned)

# Optional: Save to Delta table (uncomment to use)
# customers_cleaned.write.format("delta").mode("overwrite").save("/tmp/customer_silver")

# You can now create dashboards or queries on 'customers_cleaned' dataframe.
