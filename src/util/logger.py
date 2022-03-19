# importing module
import logging
import os
from datetime import datetime

def get_current_date():
    return datetime.now().strftime('%Y_%m_%d')

# Create and configure logger
logging.basicConfig(filename=(os.getcwd()+'/logs/'+get_current_date()+'.log'),
                    format='%(asctime)s  %(levelname)s: %(message)s',
                    filemode='a')
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

logger.debug("==================  This is a debug log  ==================")