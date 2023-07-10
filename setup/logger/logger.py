import logging

import yaml
from colorlog import ColoredFormatter
from pythonjsonlogger import jsonlogger

from . import log_config_parser
from . import logger_utils


class LoggerSetup:
    formatter = jsonlogger.JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(pathname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.console_logger = logging.getLogger("console_logger")
        self.file_logger = logging.getLogger("file_logger")

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
        self.file_logger.addHandler(file_handler)
        return self.file_logger

    def _setup_console_handler(self, handler_config):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logger_utils.get_log_level(handler_config))
        # Create a ColorFormatter with custom color settings
        # color_formatter = ColoredFormatter(
        #     f"%(log_color)s%(asctime)s %(levelname)s %(pathname)s %(message)s",
        #     datefmt="%Y-%m-%d %H:%M:%S",
        #     log_colors={
        #         'DEBUG': 'green',
        #         'INFO': 'blue',
        #         'WARNING': 'yellow',
        #         'ERROR': 'red',
        #         'CRITICAL': 'bold_red',
        #     }
        # )
        formatter_config: tuple[str, str, dict] = log_config_parser.parse_log_settings(self._load_config_file())
        color_formatter = ColoredFormatter(formatter_config[0], datefmt=formatter_config[1],
                                           log_colors=formatter_config[2])
        console_handler.setFormatter(color_formatter)
        self.console_logger.addHandler(console_handler)
        return self.console_logger

    def setup_file_logging(self):
        config = self._load_config_file()
        self.file_logger.setLevel(logging.DEBUG)

        for handler_config in config['handlers']:
            handler_type = logger_utils.get_log_type(handler_config)

            if handler_type == 'file':
                return self._setup_file_handler(handler_config)

    def setup_console_logging(self):
        config = self._load_config_file()
        self.console_logger.setLevel(logging.DEBUG)

        for handler_config in config['handlers']:
            handler_type = logger_utils.get_log_type(handler_config)

            if handler_type == 'console':
                self._setup_console_handler(handler_config)
        return self.console_logger
