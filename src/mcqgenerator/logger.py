import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   # strftime  format the datetime object into a string 
# with the specified format and .log is extension file

log_path=os.path.join(os.getcwd(),"logs")  #getcwd means current working directory joins to logs file. this is folder along with path

os.makedirs(log_path,exist_ok=True)    # create the directory specified by the log_path variable

LOG_FILEPATH=os.path.join(log_path, LOG_FILE)


logging.basicConfig(level=logging.INFO,    # only log messages with a severity level of INFO or higher will be processed.
        filename=LOG_FILEPATH,             #   file where the log messages will be written.
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)




















# import logging: Imports the logging module, which is used for logging messages.
# import os: Imports the os module, which provides functions for interacting with the operating system.
# from datetime import datetime: Imports the datetime class from the datetime module, which is used to get the current date
# and time.

#    