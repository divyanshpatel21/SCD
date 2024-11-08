# IMPORTING NECESSARY MODULES

import requests
from pyspark.sql.functions import max
import sys
from config.spark_session import spark
from config.schema_config import user_post_schema
from utils.util import write_to_snowflake_scd1
from config.logger_config import logger 

# CREATING A SPARK SESSION
logger.info("Spark session created.........")

# Calling the API
logger.info("Calling the API.........")
try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()
    posts = response.json()
    logger.info("API response received successfully.")
except requests.exceptions.RequestException as e:
    logger.error(f"Failed to fetch data from the API: {str(e)}")
    sys.exit(1)  # Exit the script if API call fails

# Creating the DataFrame
logger.info("Creating the DataFrame.........")
try:
    df_posts = spark.createDataFrame(posts, user_post_schema)
    df_posts.show()
    logger.info("DataFrame created and displayed successfully.")
except Exception as e:
    logger.error(f"Error while creating DataFrame: {str(e)}")
    sys.exit(1)

# Writing to Snowflake
try:
    write_to_snowflake_scd1(df_posts)
    logger.info("Data successfully written to Snowflake.")
except Exception as e:
    logger.error(f"Failed to write data to Snowflake: {str(e)}")
    sys.exit(1)
