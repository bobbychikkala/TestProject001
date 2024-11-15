import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)

# # Set the logging level
        logger.setLevel(logging.DEBUG)

# Create a file handler
        file = os.path.abspath(os.curdir)+"\\logs\\Automation.log"
        handler = logging.FileHandler(file)

# Create a logging format
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

# Add the handlers to the logger
        logger.addHandler(handler)

        return logger



