from pyspark.sql.types import  StructType,StringType,IntegerType,StructField

user_post_schema = StructType([
    StructField("userId", IntegerType(), True),
    StructField("id", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("body", StringType(), True)
])