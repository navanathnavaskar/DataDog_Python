
import os
from faker import Faker
from DataDogHandler import Logging

def main():
    os.environ['DD_API_KEY'] = "XXXXXXX"
    os.environ['DD_SITE'] ="datadoghq.com"
    os.environ['ENV'] = "TEST"
 
    logger = Logging(service_name='MyService', ddsource='ProgramSource', logger_name='myapp')
    for i in range(1, 2):
        _instance = Faker()
 
        _data = {
            "first_name": _instance.first_name()
        }
        logger.logger.info(_data)
        logger.logger.error("Error in getting data ")
 
main()
 