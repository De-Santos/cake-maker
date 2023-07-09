import os

from setup import LoggerSetup

# Get the absolute path to a file in the current directory
log_config_path = os.path.abspath("logging.yaml")

logger = LoggerSetup(log_config_path)
clog = logger.setup_console_logging()
flog = logger.setup_file_logging()
