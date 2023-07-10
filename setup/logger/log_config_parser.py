from setup.warnings import LoggerSetupWarning
from utils.color_warnings import warnings
from .exceptions import (
    InvalidColorTypeException,
    InvalidDateFormatTypeException,
    InvalidFormatTypeException,
    InvalidLogLevelException,
    InvalidLogTypeException,
    InvalidMessageFormatTypeException
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


def _optional_parse_log(yaml: dict) -> dict:
    if yaml.get('log') is None:
        warnings.warn(f"'log' not configured, using default settings: {str(default_log_settings)}")
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
        warnings.warn(f"'color' data must be in pattern: 'string: string', example: \n{example_log_settings[115:]}")
        raise InvalidLogLevelException()
    elif log_level not in log_levels:
        warnings.warn(f"level can only be one of: {str(log_levels)}")
        raise InvalidLogLevelException()
    if color is None:
        warnings.warn(f"'color' has invalid data, it must be like: \n{example_log_settings[115:]}",  # Print color only
                      LoggerSetupWarning)
        raise InvalidLogLevelException()
    elif not isinstance(color, str):
        warnings.warn(f"'color' data must be in pattern: 'string: string', example: \n{example_log_settings[115:]}")
        raise InvalidLogLevelException()
    return {str(log_level).upper(): color}


def _parse_log_colors(log_colors: dict) -> dict:
    levels: set = set()
    result: dict = {}
    for log_level, color in log_colors.items():
        if log_level in levels:
            warnings.warn(f"level: {log_level} already defined, overriding it")
        levels.add(log_level)
        result.update(_parse_log_level(log_level, color))
    return result


def parse_log_settings(yaml: dict) -> (str, str, dict):
    log_config: dict = _optional_parse_log(yaml)
    log_format: dict = _optional_parse_log_format(log_config)
    log_color: dict = _optional_parse_log_color(log_config)
    log_message_format: str = _parse_log_message_format(log_format)
    log_date_format: str = _parse_log_date_format(log_format)
    level_colors: dict = _parse_log_colors(log_color)
    return log_message_format, log_date_format, level_colors
