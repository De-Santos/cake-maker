import warnings

from setup.warnings import LoggerSetupWarning
from .exceptions import InvalidFilenameFileTypeException
from .exceptions import InvalidFilenameTypeException
from .exceptions import InvalidLoggingLevelTypeException
from .exceptions import InvalidLoggingTypeTypeException
from .exceptions import LoggingTypeDoesNotDefinedException


def get_log_level(handler_config) -> str:
    level = handler_config['level']
    if level is None:
        warnings.warn("'level' is not defined, using default logging level -> INFO", LoggerSetupWarning)
        return "INFO"  # default level
    elif not isinstance(level, str):
        warnings.warn("'level' must be a string")
        raise InvalidLoggingLevelTypeException()
    if str(level).islower():
        warnings.warn("'level' should be in uppercase", LoggerSetupWarning)
    return str(level).upper()


def get_log_type(handler_config) -> str:
    log_type = handler_config['type']
    if log_type is None:
        raise LoggingTypeDoesNotDefinedException()
    elif not isinstance(log_type, str):
        warnings.warn("'type' must be a string")
        raise InvalidLoggingTypeTypeException()
    if str(log_type).isupper():
        log_type = str(log_type).lower()
        warnings.warn("'type' should be in lowercase", LoggerSetupWarning)
    if log_type != 'console' and log_type != 'file':
        warnings.warn("'type' value could be only 'console' and 'file', other values will be ignored",
                      LoggerSetupWarning)
    return str(log_type).lower()


def get_filename(handler_config) -> str:
    filename = handler_config['filename']
    if filename is None:
        warnings.warn("'filename' is not defined, using default filename -> app.log", LoggerSetupWarning)
        return 'app.log'  # default filename
    elif not isinstance(filename, str):
        warnings.warn("'filename' must be a string")
        raise InvalidFilenameTypeException()
    if str(filename).endswith('.log'):
        return filename
    else:
        warnings.warn("'filename' file type must me '.log' for example: 'example.log'", LoggerSetupWarning)
        raise InvalidFilenameFileTypeException()
