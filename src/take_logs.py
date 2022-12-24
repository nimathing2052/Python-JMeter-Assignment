from logging import (
    basicConfig,
    getLogger,
    DEBUG
)
from os.path import join, basename
from settings import (
    LOGGING_FORMAT, 
    LOGGING_FOLDER, 
    LOGGING_WRITE_PERM
)


__all__ = ["get_logger"]


def get_logger(file_name: str= ""):
    """ The logger has file name to the file that 
    called it in LOGGING FOLDER""" 
    
    # if file name is not equal given the 
    # take the calling filename as the log name
    # example:
    #   calling_file: main.py
    #   log_name: main.log
    if file_name == "":
        import inspect
        absolute_filepath = inspect.stack()[1].filename
        caller_filename = basename(absolute_filepath)[:-3] # take only the script name 
        file_name = caller_filename + ".log" # replacing .py extenction with .log 
    
    # initializing logger
    basicConfig(
        filename=join(LOGGING_FOLDER, file_name), 
        format= LOGGING_FORMAT, 
        filemode=LOGGING_WRITE_PERM
    ) 
    logger=getLogger() 
    logger.setLevel(DEBUG) 
    return logger

  
if __name__ == "__main__":
    logger = get_logger("apple.log")
    logger.debug("This is just a harmless debug message") 



