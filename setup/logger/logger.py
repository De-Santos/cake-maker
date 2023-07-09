import logging

import yaml
from pythonjsonlogger import jsonlogger

from . import logger_utils


class LoggerSetup:
    formatter = jsonlogger.JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(pathname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.logger = logging.getLogger()

    def _load_config_file(self):
        try:
            with open(self.config_file_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print("File with configuration not found")
            exit()

    def _setup_file_handler(self, handler_config):
        file_handler = logging.FileHandler(logger_utils.get_filename(handler_config))
        file_handler.setLevel(logger_utils.get_log_level(handler_config))
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)
        return self.logger

    def _setup_console_handler(self, handler_config):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logger_utils.get_log_level(handler_config))
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)
        return self.logger

    def setup_file_logging(self):
        config = self._load_config_file()
        self.logger.setLevel(logging.DEBUG)

        for handler_config in config['handlers']:
            handler_type = logger_utils.get_log_type(handler_config)

            if handler_type == 'file':
                return self._setup_file_handler(handler_config)

    def setup_console_logging(self):
        config = self._load_config_file()
        self.logger.setLevel(logging.DEBUG)

        for handler_config in config['handlers']:
            handler_type = logger_utils.get_log_type(handler_config)

            if handler_type == 'console':
                self._setup_console_handler(handler_config)
        return self.logger
