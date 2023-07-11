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


class InvalidHandlerTypeException(Exception):
    def __init__(self, message: str = "'handlers' must be header, not an argument") -> None:
        super().__init__(message)


class InvalidConsoleLogLevelException(Exception):
    def __init__(self, message: str = "Invalid 'handlers:console:level', unknown log level") -> None:
        super().__init__(message)


class InvalidConsoleLogLevelTypeException(Exception):
    def __init__(self, message: str = "Invalid 'handlers:console:level' type, log level must be string") -> None:
        super().__init__(message)


class InvalidConsoleHandlerTypeException(Exception):
    def __init__(self, message: str = "'handlers:console' must be header, not argument") -> None:
        super().__init__(message)


class InvalidFileHandlerTypeException(Exception):
    def __init__(self, message: str = "'handlers:file' must be header, not argument") -> None:
        super().__init__(message)


class InvalidFileLogLevelTypeException(Exception):
    def __init__(self, message: str = "Invalid 'handlers:file:level' type, log level must be string") -> None:
        super().__init__(message)


class InvalidFileLogLevelException(Exception):
    def __init__(self, message: str = "Invalid 'handlers:file:level', unknown log level") -> None:
        super().__init__(message)
