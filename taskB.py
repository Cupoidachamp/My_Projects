from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, to_date

spark = SparkSession.builder.appName("taskB").getOrCreate()

input_path = "s3://smartgear-vs-dev/raw/smartgear_sales.csv"

df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

#print("RAW DATA")
#df.show(5)

#df.printSchema()

#-----------------Fix Data Types-----------------------------#

df = df.withColumn("OrderID", col("OrderID").cast("string")) \
       .withColumn("OrderDate", to_date(col("OrderDate"), "dd-MM-yyyy")) \
       .withColumn("Region", col("Region").cast("string")) \
       .withColumn("StoreID", col("StoreID").cast("string")) \
       .withColumn("Product", col("Product").cast("string")) \
       .withColumn("Quantity", col("Quantity").cast("int")) \
       .withColumn("UnitPrice", col("UnitPrice").cast("double"))

# Checking schema
df.printSchema()

#-----------------Removing Duplicate Records-----------------------------#

df = df.dropDuplicates(["OrderID"])

#-----------------Transform Data-----------------------------#

region_qty_df = df.groupBy("Region").agg(sum("Quantity").alias("Total_Quantity"))

# Show result
region_qty_df.show(10)

#-----------------Loading Data to Curated Folder-----------------------------#

output_path = "s3://smartgear-vs-dev/curated/region-qty_parquet/"
region_qty_df.write.mode("overwrite").parquet(output_path)

print("parquet written successfully")
