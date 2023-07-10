import os

from setup import LoggerSetup

# Logger
log_config_path = os.path.abspath("logging.yaml")  # Get absolute path to the logging configuration file
logger = LoggerSetup(log_config_path)
clog = logger.setup_console_logging()
flog = logger.setup_file_logging()
