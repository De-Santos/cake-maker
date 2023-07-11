import logging

import yaml
from colorlog import ColoredFormatter
from pythonjsonlogger import jsonlogger

from setup.warnings import LoggerSetupWarning
from utils.color_warnings import warnings
from . import log_config_parser


class LoggerSetup:
    formatter = jsonlogger.JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(pathname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.console_logger = logging.getLogger("console_logger")
        self.file_logger = logging.getLogger("file_logger")
        self.config = self._load_config_file()
        self.handlers_config = log_config_parser.parse_handler_config(self.config)

    def _load_config_file(self):
        try:
            with open(self.config_file_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            warnings.warn(f"Logging configuration file not found: {self.config_file_path}", LoggerSetupWarning)
            return dict()

    def setup_file_logging(self):
        self.file_logger.setLevel(logging.DEBUG)
        file_config = log_config_parser.get_handler_file_config(self.handlers_config)
        file_handler = logging.FileHandler(log_config_parser.get_log_filename(file_config))
        file_handler.setLevel(log_config_parser.get_file_log_level(file_config))
        file_handler.setFormatter(self.formatter)
        self.file_logger.addHandler(file_handler)
        return self.file_logger

    def setup_console_logging(self):
        self.console_logger.setLevel(logging.DEBUG)
        console_config = log_config_parser.get_handler_console_config(self.handlers_config)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_config_parser.get_console_log_level(console_config))
        formatter_config: tuple[str, str, dict] = log_config_parser.parse_log_config(self.config)
        color_formatter = ColoredFormatter(formatter_config[0], datefmt=formatter_config[1],
                                           log_colors=formatter_config[2])
        console_handler.setFormatter(color_formatter)
        self.console_logger.addHandler(console_handler)
        return self.console_logger
