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
