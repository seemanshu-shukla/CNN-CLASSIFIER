import os
import sys
import logging


logging_str="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s" ##Defining the format in which logs need to be stored

log_dir="logs"  ##Defining the dir that needs to be utilized for stroing the logs

os.makedirs(log_dir, exist_ok=True)  ##Creating directory for log_dir

log_filepath=os.path.join(log_dir,"running_logs.log") ##Creating path

##Using logging to wrap up/embed different features that logs will contain
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  ##FileHandler used for storing logs in some file
        logging.StreamHandler(sys.stdout)   ##StreamHandler used to display logs over terminal in runtime
    ]
                    )
logger=logging.getLogger("CNNClassfierLogger")  ##Finally using .getLogger to create a logger with a
                                          ##name "CNNClassiferLogger" which contain all the above
                                          ## defined logging features and stroring it in the variable
                                          ##logger. This logger variable can be then called wherever
                                          ##we wish to embed the logging mechanism after importing 
                                          ##this package 