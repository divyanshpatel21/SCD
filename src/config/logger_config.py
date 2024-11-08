import logging
import os
from logging.handlers import TimedRotatingFileHandler

# Define the directory and log file path
log_directory = "SCD_logs"
os.makedirs(log_directory, exist_ok=True)  
log_file_path = os.path.join(log_directory, "SCD_log.log") 

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[              
        TimedRotatingFileHandler(log_file_path, when="midnight", interval=1, backupCount=10), 
        logging.StreamHandler()  
    ]
)

logger = logging.getLogger()
