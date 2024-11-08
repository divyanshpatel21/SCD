from pyspark.sql import SparkSession
from .logger_config import logger
# Start logging the process of Spark session creation
logger.info("Initializing Spark session with Snowflake JDBC and Spark Snowflake connector.")

try:
    # Create Spark session and specify necessary configurations
    logger.info("Setting up Spark session configurations.")
    spark = SparkSession.builder.appName("HistoriPy").config("spark.jars", "/spark-data/jars/snowflake-jdbc-3.13.14.jar,/spark-data/jars/spark-snowflake_2.12-2.16.0-spark_3.4.jar").getOrCreate()

    # Log success message
    logger.info("Spark session successfully created with app name 'HistoriPy'.")

except Exception as e:
    # Log the error if something goes wrong
    logger.error(f"Failed to create Spark session. Error: {str(e)}")
    raise e

# Log completion of Spark session setup
logger.info("Spark session setup completed.")
