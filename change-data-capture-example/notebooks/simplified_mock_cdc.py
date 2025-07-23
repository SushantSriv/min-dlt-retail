
# Simplified Retail CDC Demo (Offline-Compatible for Community Edition)
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

# Mock dataset: 3 customer records
data = [
    ("1", "john@example.com", "John", "Doe", "Oslo"),
    ("2", "jane@example.com", "Jane", "Doe", "Bergen"),
    (None, "invalid@example.com", "Invalid", "User", "Trondheim")
]

# Schema
schema = StructType([
    StructField("customer_id", StringType(), True),
    StructField("email", StringType(), True),
    StructField("firstname", StringType(), True),
    StructField("lastname", StringType(), True),
    StructField("address", StringType(), True),
])

# Create DataFrame
raw_customers = spark.createDataFrame(data, schema)

# Display raw data (Bronze Layer)
print("🟫 Raw Customer Data (Simulated):")
display(raw_customers)

# Filter out rows with NULL customer_id (Silver Layer)
customers_cleaned = raw_customers.filter("customer_id IS NOT NULL")

# Display cleaned data
print("⬜ Cleaned Customer Data (Filtered):")
display(customers_cleaned)
