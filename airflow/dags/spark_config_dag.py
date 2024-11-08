from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

# Define the DAG
with DAG(
    'run_pyspark_in_existing_container',
    default_args=default_args,
    schedule_interval=None,  # Trigger manually or set to a specific schedule
) as dag:

    # Task to run main.py inside the already running PySpark container using `docker exec`
    run_spark_task = BashOperator(
        task_id='run_pyspark_main_task',
        bash_command='docker exec spark-worker python /spark-data/src/SCD_pipeline.py',
        # Replace 'pyspark_scd' with the container name or ID of the running PySpark container
    )

    run_spark_task
# from airflow import DAG
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
# from airflow.utils.dates import days_ago

# # Define the default arguments for the DAG
# default_args = {
#     'owner': 'airflow',
#     'start_date': days_ago(1),
#     'retries': 1,
# }

# # Define the DAG
# with DAG(
#     dag_id='spark_job_dag',             # DAG ID
#     default_args=default_args,          # Default arguments
#     description='A simple DAG to run Spark job',
#     schedule_interval='@daily',         # Set to run daily
#     catchup=False,                      # Do not catch up on missed runs
# ) as dag:

#     # Define the SparkSubmitOperator to submit the Spark job
#     run_spark_job = SparkSubmitOperator(
#         task_id='run_spark_job',                     # Task ID
#         application='/opt/src/config/sparkconfig.py', # Path to the Spark application (Python file)
#         conn_id='spark_default',                      # Connection ID for Spark configured in Airflow
#         conf={                                        # Spark configurations
#             'spark.master': 'spark://spark-master:7077',  # Spark master URL
#         },
#         # Provide the directory path containing all the JARs
#         jars='/opt/jars/*',                           # Use wildcard (*) to include all JARs in the directory
#         verbose=True,                                 # Enable verbose output for logging
#         application_args=[],                          # Optional arguments for the Spark job
#         dag=dag,                                      # Assign the DAG to this task
#     )

#     run_spark_job  # Set the task to the DAG


# from airflow import DAG
# from airflow.providers.docker.operators.docker import DockerOperator
# from airflow.utils.dates import days_ago

# # Define the DAG
# with DAG(
#     dag_id='spark_job_dag',
#     default_args={
#         'owner': 'airflow',
#         'retries': 1,
#     },
#     description='A simple DAG to run Spark job',
#     schedule_interval='@daily',
#     start_date=days_ago(1),
#     catchup=False,
# ) as dag:

#     # Define the DockerOperator to run the Spark job
#     run_spark = DockerOperator(
#         task_id='run_spark_job',
#         image='bitnami/spark:latest',  # Use the Spark image
#         api_version='auto',
#         auto_remove=True,
#         command='spark-submit --master spark://spark-master:7077 /opt/src/config/sparkconfig.py',
#         mounts=[
#             {
#                 'source': 'D:/HistoriPy/src', 
#                 'target': '/opt/src', 
#                 'type': 'bind'
#             },
#             {
#                 'source': 'D:/HistoriPy/src/jars', 
#                 'target': '/opt/jars',  # Make sure this directory exists in the container
#                 'type': 'bind'
#             }
#         ],
#         dag=dag,
#     )

#     run_spark


# from airflow import DAG
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
# from airflow.utils.dates import days_ago

# # Default arguments for the DAG
# default_args = {
#     'owner': 'airflow',
#     'retries': 1,
# }

# # Define the DAG
# with DAG(
#     dag_id='spark_job_dag',
#     default_args=default_args,
#     description='A simple DAG to run Spark job',
#     schedule_interval='@daily',  # Adjust this as needed
#     start_date=days_ago(1),
#     catchup=False,
# ) as dag:

#     # Define the SparkSubmitOperator to run the Spark job
#     run_spark = SparkSubmitOperator(
#         task_id='run_spark_job',
#         application='/opt/src/spark_config.py',  # Path to your Spark job script
#         master='spark://spark-master:7077',      # Spark Master URL
#         dag=dag,
#     )

#     run_spark



# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.utils.dates import days_ago

# # Function to be executed in the DAG
# def print_message():
#     print("Hello, this is a test message from the Airflow DAG!")

# # Default arguments for the DAG
# default_args = {
#     'owner': 'airflow',
#     'retries': 1,
# }

# # Define the DAG
# with DAG(
#     dag_id='test_dag',
#     default_args=default_args,
#     description='A simple test DAG',
#     schedule_interval='@once',  # Run once for testing
#     start_date=days_ago(1),
#     catchup=False,
# ) as dag:

#     # Define the PythonOperator to run the print_message function
#     test_task = PythonOperator(
#         task_id='print_message_task',
#         python_callable=print_message,
#     )

#     test_task
