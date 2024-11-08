from config.database_config import SF_URL, SF_USER, SF_PASSWORD, SF_DATABASE, SF_SCHEMA, SF_WAREHOUSE, SF_ROLE
from pyspark.sql.functions import lit, current_timestamp

def write_to_snowflake_scd1(dataframe):
    """
    Write data to Snowflake using SCD Type 1 - overwrite mode with timestamps.
    """

    # Add BD_CREATE_DT_TM and BD_UPDATE_DT_TM columns with default timestamps if they do not exist
    if "BD_CREATE_DT_TM" not in dataframe.columns:
        dataframe = dataframe.withColumn("BD_CREATE_DT_TM", current_timestamp())
    if "BD_UPDATE_DT_TM" not in dataframe.columns:
        dataframe = dataframe.withColumn("BD_UPDATE_DT_TM", current_timestamp())
    
    # Set BD_UPDATE_DT_TM to the current timestamp (for SCD Type 1 update)
    dataframe = dataframe.withColumn("BD_UPDATE_DT_TM", current_timestamp())

    # Write the data to Snowflake
    dataframe.write \
        .format("snowflake") \
        .option("sfURL", SF_URL) \
        .option("sfUser", SF_USER) \
        .option("sfPassword", SF_PASSWORD) \
        .option("sfDatabase", SF_DATABASE) \
        .option("sfSchema", SF_SCHEMA) \
        .option("sfWarehouse", SF_WAREHOUSE) \
        .option("sfRole", SF_ROLE) \
        .option("dbtable", "user_posts") \
        .mode("overwrite") \
        .save()
