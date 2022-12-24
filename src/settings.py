#################################
# Imports
#################################
from os.path import join
from os import getcwd
#################################
# Logging 
#################################
__MAIN_FOLDER = getcwd()  
#################################
# Logging 
#################################
LOGGING_WRITE_PERM = "a+"
LOGGING_FORMAT = '%(asctime)s %(message)s'
LOGGING_FOLDER =  join(__MAIN_FOLDER, "logs")
#################################
# DATA
#################################
DATA_FOLDER = join(__MAIN_FOLDER, "data")
TXT_DELIMITER= "	"
CSV_DELIMITER = ","
#################################
# TASK
#################################
TASK_1_FILE = join(DATA_FOLDER, "TASK-1.csv")
TASK_2_FILE = join(DATA_FOLDER, "TASK-2.csv")
TASK_3_FILE = join(DATA_FOLDER, "TASK-3.json")
#################################


