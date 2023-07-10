class LoggingTypeDoesNotDefinedException(Exception):
    def __init__(self, message: str = "Logging type must be defined") -> None:
        super().__init__(message)


class InvalidLoggingLevelTypeException(Exception):
    def __init__(self, message: str = "Logging level must be string") -> None:
        super().__init__(message)


class InvalidLoggingTypeTypeException(Exception):
    def __init__(self, message: str = "Logging type must be string") -> None:
        super().__init__(message)


class InvalidFilenameTypeException(Exception):
    def __init__(self, message: str = "Invalid filename type, filename type must be string") -> None:
        super().__init__(message)


class InvalidFilenameFileTypeException(Exception):
    def __init__(self, message: str = "Filename file type must be '.log'") -> None:
        super().__init__(message)


class InvalidLogTypeException(Exception):
    def __init__(self, message: str = "'log' must be the header, not an argument") -> None:
        super().__init__(message)


class InvalidFormatTypeException(Exception):
    def __init__(self, message: str = "'format' must be the header, not an argument") -> None:
        super().__init__(message)


class InvalidColorTypeException(Exception):
    def __init__(self, message: str = "'color' must be the header, not an argument") -> None:
        super().__init__(message)


class InvalidMessageFormatTypeException(Exception):
    def __init__(self, message: str = "Invalid 'log:format:message' type, message format must be string") -> None:
        super().__init__(message)


class InvalidDateFormatTypeException(Exception):
    def __init__(self, message: str = "Invalid 'log:format:date' type, date format must be string") -> None:
        super().__init__(message)


class InvalidLogLevelException(Exception):
    def __init__(self, message: str = "Invalid log level") -> None:
        super().__init__(message)
