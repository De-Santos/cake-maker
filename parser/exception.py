class BuildConfigurationFileNotFoundException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Build configuration file not found by path: {path}")


class ProjectPathNotDefinedException(Exception):
    def __init__(self, message: str = "Project path not defined") -> None:
        super().__init__(message)


class InvalidProjectPathTypeException(Exception):
    def __init__(self, message: str = "Invalid 'project:path' type, must be a string") -> None:
        super().__init__(message)


class ProjectNotADirectoryException(Exception):
    def __init__(self, message: str = "Project must be folder") -> None:
        super().__init__(message)


class InvalidProjectNameException(Exception):
    def __init__(self, message: str = "Invalid 'project:name' type, must be a string") -> None:
        super().__init__(message)


class InvalidProjectValue(Exception):
    def __init__(self, message: str = "Invalid 'project' value") -> None:
        super().__init__(message)
