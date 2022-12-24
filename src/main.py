#!/usr/bin/python

from os.path import join, exists
from settings import (
    DATA_FOLDER,
    TASK_1_FILE,
    TASK_3_FILE, 
    TXT_DELIMITER, 
    CSV_DELIMITER,
    TASK_1_FILE,
    LOGGING_FOLDER,
    TASK_2_FILE
)
from take_logs import get_logger
import pandas as pd

   
# task 1 return boolean cause 
# task 2 and task3 runs with assumption
# that task 1 is successful
def task_1(file_name: str, logger) -> bool:
    """
    1.    Task1:
    a.    Convert the txt file to csv format.
    b.    Change the record delimiter from tab to comma delimited for each row.
    """    
    # only proceed if
    # 1. file exits 
    # 2. df is not empty
    if not exists(file_name):
        logger.error("% not found" % file_name)
        return False

    df = pd.read_csv(file_name, delimiter=TXT_DELIMITER)
    if df.empty:
        logger.error("data frame is empty for %s" % file_name)
        return False

    df.to_csv(TASK_1_FILE, index=False)
    return True
    

def task_2(file_name: str, logger) -> None:
    """
    2.    Task 2:
    a.    Count the number of rows in the csv file (excluding the header row)
    b.    Calculate the checksum of the csv file
    c.    Append the checksum and row count to the header and footer of the csv file.
    """
    # only proceed if
    # 1. file exits 
    # 2. df is not empty
    if not exists(file_name):
        logger.error("% not found" % file_name)
        return

    df = pd.read_csv(file_name, delimiter=TXT_DELIMITER)
    if df.empty:
        logger.error("data frame is empty for %s" % file_name)
        return

    df = pd.read_csv(file_name)
    length: int = len(df.index)

    from md5 import create_md5_checksum

    checksum: str = create_md5_checksum(file_name)

    # storing data in tempory file
    temp_file = join(LOGGING_FOLDER, "a.csv")
    df.to_csv(temp_file,  index=False)
    with open(temp_file) as reader:
        data = reader.read()
        with open(TASK_2_FILE, "w+") as f:
            # writing length and checksum to header
            f.write("length=%s, checksum=%s\n" % (length, checksum))
            f.write(data)
            # writing length and checksum to footer
            f.write("length=%s, checksum=%s\n" % (length, checksum))
            


def task_3(file_name: str, logger, length:int =5) -> None:
    """
    Using the csv file generated in task 
    1, create a JSON object array/file of the first 5 rows of data from the .csv file. 
    Here's the JSON object format:
    { 
       "Country": "Nepal", 
       "Product": "Carretera",    
        "DiscountBand": "None",    
        "UnitsSold": "1618.5",    
        "ManufacturingPrice": "$3.00",   
        "SalePrice": "$20.00",  
        "GrossSales": "$32",    
        "SalesQty": "370.00"
    }
    """
    # only proceed if
    # 1. file exits 
    # 2. df is not empty
    if not exists(file_name):
        logger.error("% not found" % file_name)
        return

    df = pd.read_csv(file_name, delimiter=TXT_DELIMITER)
    if df.empty:
        logger.error("data frame is empty for %s" % file_name)
        return

    df = pd.read_csv(file_name)
    columns = df.columns.values
    # taking only n number of rows corresponding with
    # {length} and converting the repsective row to json 
    # using dict comprehension 
    json_df = df.iloc[:length:, :].apply(
        lambda row: {key: value for key,value in  zip(columns, row)},
        axis=1
    )
    from json import dump
    # storing the data as json array in dict
    with open(TASK_3_FILE, "w+") as f:
        dump(
            [value for value in json_df],
            f,
            indent=4
        )


if __name__ == "__main__":
    from time import time
    from os import mkdir

    # creating logging folder if it doesnt exsits
    if not exists(LOGGING_FOLDER):
        mkdir(LOGGING_FOLDER)

    start_time = time()
    file_name: str = r"Python Script Task - File.txt"
    abolute_path: str = join(DATA_FOLDER, file_name)

    # logger
    logger = get_logger()
    success = task_1(abolute_path, logger) 

    if not success:
        print("converstion was failure. check logs")
    
    from check_integrity import check_integrity
    
    err_count = check_integrity(
        file_with_tabs=abolute_path,
        files_with_comma=TASK_1_FILE,
        logger=logger
    )
    # before procedding check if conversion is proper
    if err_count != 0:
        import sys
        print("cant proceed because the converstion didnt match for %d lines" % err_count)
        sys.exit(0)
    
    task_2(TASK_1_FILE, logger)
    task_3(TASK_1_FILE, logger)
    print("Process completed. files are present in data folder")
    print("total_time: %d" % (time() - start_time))
    