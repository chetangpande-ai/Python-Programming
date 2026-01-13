'''logger file to write logs for agentic AI project
1. Create new file for every new run
2. create file with date and time stamp
3. log every step of the process
4. log errors and exceptions
5. log start and end time of the process
6. log important variable values
7. log function entry and exit points
8. log performance metrics
9. log system information
10. log user actions
11. log configuration settings
12. log external API calls
13. log database queries
14. log file operations
15. log network requests
16. log security events
17. log debug information
18. log warnings
19. log info messages
20. log critical errors
'''
import logging
from datetime import datetime
import os


def setup_logger():
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create a logger
    logger = logging.getLogger('agentic_ai_logger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler with date and time stamp
    log_filename = datetime.now().strftime("logs/agentic_ai_%Y-%m-%d_%H-%M-%S.log")
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger




if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Logger setup complete.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
    logger.info("Logger test complete.")
