from setup.warnings import LoggerSetupWarning
from utils.color_warnings import warnings
from .exceptions import (
    InvalidColorTypeException,
    InvalidDateFormatTypeException,
    InvalidFormatTypeException,
    InvalidLogLevelException,
    InvalidLogTypeException,
    InvalidMessageFormatTypeException,
    InvalidHandlerTypeException,
    InvalidConsoleLogLevelTypeException,
    InvalidConsoleLogLevelException,
    InvalidConsoleHandlerTypeException,
    InvalidFileHandlerTypeException,
    InvalidFileLogLevelTypeException,
    InvalidFileLogLevelException,
    InvalidFilenameTypeException,
    InvalidFilenameFileTypeException
)

default_log_settings: dict = {
    'log': {
        'format': {
            'message': '%(log_color)s%(levelname)s %(pathname)s %(message)s',
            'date': '%Y-%m-%d %H:%M:%S'
        },
        'color': {
            'debug': 'green',
            'info': 'blue',
            'warning': 'yellow',
            'error': 'red',
            'critical': 'bold_red'
        }
    }
}
log_levels: set = {'debug', 'info', 'warning', 'error', 'critical'}
example_log_settings: str = """
log:
  format:
    message: "%(log_color)s%(levelname)s %(pathname)s %(message)s"
    date: "%Y-%m-%d %H:%M:%S"
  color:
    debug: green
    info: blue
    warning: yellow
    error: red
    critical: bold_red
"""
default_handler_config: dict = {
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'filename': 'app.log',
        },
        'console': {
            'level': 'INFO',
        }
    }
}
example_handler_config: str = """
handlers:
  file:
    level: DEBUG
    filename: app.log
  console:
    level: INFO
"""


def _optional_parse_log(yaml: dict) -> dict:
    if yaml.get('log') is None:
        warnings.warn(f"'log' not configured, using default settings: {str(default_log_settings)}", LoggerSetupWarning)
        return default_log_settings.get('log')
    elif not isinstance(yaml.get('log'), dict):
        warnings.warn(f"'log' must be like: {example_log_settings}", LoggerSetupWarning)
        raise InvalidLogTypeException()
    return yaml.get('log')


def _optional_parse_log_format(log_config: dict) -> dict:
    if log_config.get('format') is None:
        default_log_format: dict = default_log_settings.get('log').get('format')
        warnings.warn(f"'log:format' not configured, using default settings: {str(default_log_format)}",
                      LoggerSetupWarning)
        return default_log_format
    elif not isinstance(log_config.get('format'), dict):
        warnings.warn(f"'format' must have signature like: \n{example_log_settings[8:112]}",
                      LoggerSetupWarning)  # Print format only
        raise InvalidFormatTypeException()
    return log_config.get('format')


def _optional_parse_log_color(log_config: dict) -> dict:
    if log_config.get('color') is None:
        default_log_color: dict = default_log_settings.get('log').get('color')
        warnings.warn(f"'log:color' not configured, using default settings: {str(default_log_color)}",
                      LoggerSetupWarning)
        return default_log_color
    elif not isinstance(log_config.get('color'), dict):
        warnings.warn(f"'color' must have signature like: \n{example_log_settings[115:]}",  # Print color only
                      LoggerSetupWarning)
        raise InvalidColorTypeException()
    return log_config.get('color')


def _parse_log_message_format(log_format: dict) -> str:
    if log_format.get('message') is None:
        default_log_message_format: str = str(default_log_settings.get('log').get('format').get('message'))
        warnings.warn(f"'log:format:message' not configured, using default settings: {default_log_message_format}",
                      LoggerSetupWarning)
        return default_log_message_format
    elif not isinstance(log_format.get('message'), str):
        warnings.warn(f"'message' must be a string", LoggerSetupWarning)
        raise InvalidMessageFormatTypeException()
    return log_format.get('message')


def _parse_log_date_format(log_format: dict) -> str:
    if log_format.get('date') is None:
        default_log_date_format: str = str(default_log_settings.get('log').get('format').get('date'))
        warnings.warn(f"'log:format:date' not configured, using default settings: {default_log_date_format}",
                      LoggerSetupWarning)
        return default_log_date_format
    elif not isinstance(log_format.get('date'), str):
        warnings.warn(f"'date' must be a string", LoggerSetupWarning)
        raise InvalidDateFormatTypeException()
    return log_format.get('date')


def _parse_log_level(log_level, color) -> dict:
    if log_level is None:
        warnings.warn(f"'color' has invalid data, it must be like: \n{example_log_settings[115:]}",  # Print color only
                      LoggerSetupWarning)
        raise InvalidLogLevelException()
    elif not isinstance(log_level, str):
        warnings.warn(f"'color' data must be in pattern: 'string: string', example: \n{example_log_settings[115:]}",
                      LoggerSetupWarning)
        raise InvalidLogLevelException()
    elif log_level not in log_levels:
        warnings.warn(f"level can only be one of: {str(log_levels)}", LoggerSetupWarning)
        raise InvalidLogLevelException()
    if color is None:
        warnings.warn(f"'color' has invalid data, it must be like: \n{example_log_settings[115:]}",  # Print color only
                      LoggerSetupWarning)
        raise InvalidLogLevelException()
    elif not isinstance(color, str):
        warnings.warn(f"'color' data must be in pattern: 'string: string', example: \n{example_log_settings[115:]}",
                      LoggerSetupWarning)
        raise InvalidLogLevelException()
    return {str(log_level).upper(): color}


def _parse_log_colors(log_colors: dict) -> dict:
    levels: set = set()
    result: dict = {}
    for log_level, color in log_colors.items():
        if log_level in levels:
            warnings.warn(f"level: {log_level} already defined, overriding it", LoggerSetupWarning)
        levels.add(log_level)
        result.update(_parse_log_level(log_level, color))
    return result


def parse_log_config(yaml: dict) -> (str, str, dict):
    log_config: dict = _optional_parse_log(yaml)
    log_format: dict = _optional_parse_log_format(log_config)
    log_color: dict = _optional_parse_log_color(log_config)
    log_message_format: str = _parse_log_message_format(log_format)
    log_date_format: str = _parse_log_date_format(log_format)
    level_colors: dict = _parse_log_colors(log_color)
    return log_message_format, log_date_format, level_colors


def parse_handler_config(yaml: dict) -> dict:
    if yaml.get('handlers') is None:
        warnings.warn(f"'handlers' not configured, using default settings: {str(default_handler_config)}",
                      LoggerSetupWarning)
        return default_handler_config.get('handlers')
    elif not isinstance(yaml.get('handlers'), dict):
        warnings.warn(f"'handlers' must be like: {example_handler_config}", LoggerSetupWarning)
        raise InvalidHandlerTypeException()
    return yaml.get('handlers')


def get_handler_console_config(handler_config: dict) -> dict:
    if handler_config.get('console') is None:
        console_config: dict = default_handler_config.get('handlers').get('console')
        warnings.warn(f"'handlers:console' not configured, using default settings: {str(console_config)}",
                      LoggerSetupWarning)
        return console_config
    elif not isinstance(handler_config.get('console'), dict):
        warnings.warn(f"'console' must be like: {example_handler_config}", LoggerSetupWarning)
        raise InvalidConsoleHandlerTypeException()
    return handler_config.get('console')


def get_console_log_level(console_config: dict) -> str:
    if console_config.get('level') is None:
        default_console_level: str = str(default_handler_config.get('handlers').get('console').get('level'))
        warnings.warn(f"'handlers:console:level' not configured, using default settings: {default_console_level}",
                      LoggerSetupWarning)
        return default_console_level
    elif not isinstance(console_config.get('level'), str):
        warnings.warn(f"'level' must be a string", LoggerSetupWarning)
        raise InvalidConsoleLogLevelTypeException()
    elif str(console_config.get('level')).lower() not in log_levels:
        warnings.warn(f"level can only be one of: {str(log_levels)}", LoggerSetupWarning)
        raise InvalidConsoleLogLevelException()
    return console_config.get('level')


def get_handler_file_config(handler_config: dict) -> dict:
    if handler_config.get('file') is None:
        file_config: dict = default_handler_config.get('handlers').get('file')
        warnings.warn(f"'handlers:file' not configured, using default settings: {str(file_config)}",
                      LoggerSetupWarning)
        return file_config
    elif not isinstance(handler_config.get('file'), dict):
        warnings.warn(f"'file' must be like: {example_handler_config}", LoggerSetupWarning)
        raise InvalidFileHandlerTypeException()
    return handler_config.get('file')


def get_file_log_level(file_config: dict) -> str:
    if file_config.get('level') is None:
        default_file_log_level: str = str(default_handler_config.get('handlers').get('file').get('level'))
        warnings.warn(f"'handlers:file:level' not configured, using default settings: {default_file_log_level}",
                      LoggerSetupWarning)
        return default_file_log_level
    elif not isinstance(file_config.get('level'), str):
        warnings.warn(f"'level' must be a string", LoggerSetupWarning)
        raise InvalidFileLogLevelTypeException()
    elif str(file_config.get('level')).lower() not in log_levels:
        warnings.warn(f"level can only be one of: {str(log_levels)}", LoggerSetupWarning)
        raise InvalidFileLogLevelException()
    return file_config.get('level')


def get_log_filename(file_config: dict) -> str:
    if file_config.get('filename') is None:
        default_filename: str = str(default_handler_config.get('handlers').get('file').get('filename'))
        warnings.warn(f"'handlers:file:filename' not configured, using default settings: {default_filename}",
                      LoggerSetupWarning)
        return default_filename
    elif not isinstance(file_config.get('filename'), str):
        warnings.warn(f"'filename' must be a string", LoggerSetupWarning)
        raise InvalidFilenameTypeException()
    elif not file_config.get('filename').endswith('.log'):
        warnings.warn(f"'filename' must end with '.log'", LoggerSetupWarning)
        raise InvalidFilenameFileTypeException()
    return file_config.get('filename')
