class ParseException(Exception):
    def __init__(self, place, message) -> None:
        super().__init__(message, place)


class BuildConfigurationFileNotFoundException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Build configuration file not found by path: {path}")


class ProjectPathNotDefinedException(ParseException):
    def __init__(self, project, message: str = "Project path not defined") -> None:
        super().__init__(project, message)


class InvalidProjectPathTypeException(ParseException):
    def __init__(self, project, message: str = "Invalid 'project:path' type, must be a string") -> None:
        super().__init__(project, message)


class ProjectNotADirectoryException(Exception):
    def __init__(self, message: str = "Project must be folder") -> None:
        super().__init__(message)


class ProjectNotFoundException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Project not found by path: {path}")


class InvalidProjectNameException(ParseException):
    def __init__(self, project, message: str = "Invalid 'project:name' type, must be a string") -> None:
        super().__init__(project, message)


class InvalidProjectValue(ParseException):
    def __init__(self, project, message: str = "Invalid 'project' value") -> None:
        super().__init__(project, message)


class ModulesNotDefinedException(Exception):
    def __init__(self, message: str = "'modules' not defined") -> None:
        super().__init__(message)


class InvalidModuleTypeException(ParseException):
    def __init__(self, module, message: str = "Invalid 'module' type, must be a header") -> None:
        super().__init__(module, message)


class ModuleNameNotDefinedException(ParseException):
    def __init__(self, module, message: str = "'module:name' must be defined") -> None:
        super().__init__(module, message)


class ModuleNameDuplicateException(ParseException):
    def __init__(self, module) -> None:
        super().__init__(module, f"'module:name' must be unique")


class InvalidModuleNameTypeException(ParseException):
    def __init__(self, module, message: str = "Invalid 'module:name' type, must be a string") -> None:
        super().__init__(module, message)


class ModulePathNotDefinedException(ParseException):
    def __init__(self, module, message: str = "'module:path' must be defined") -> None:
        super().__init__(module, message)


class InvalidModulePathTypeException(ParseException):
    def __init__(self, module, message: str = "Invalid 'module:path' type, must be a string") -> None:
        super().__init__(module, message)


class ModuleNotFoundException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Module not found by path: {path}")


class ModuleNotADirectoryException(ParseException):
    def __init__(self, module, path: str) -> None:
        super().__init__(module, f"Module must be folder by path: {path}")


class ModuleDockerfilePathNotDefinedException(ParseException):
    def __init__(self, module, message: str = "'module:dockerfile_path' must be defined") -> None:
        super().__init__(module, message)


class InvalidModuleDockerfilePathTypeException(ParseException):
    def __init__(self, module, message: str = "Invalid 'module:dockerfile_path' type, must be a string") -> None:
        super().__init__(module, message)


class ModuleDockerfileNotFoundException(ParseException):
    def __init__(self, module, path: str) -> None:
        super().__init__(module, f"Module dockerfile not found by path: {path}")


class ModuleDockerfileNotAFileException(ParseException):
    def __init__(self, module, path: str) -> None:
        super().__init__(module, f"Module dockerfile must be file by path: {path}")


class ModuleCommandsNotDefinedException(ParseException):
    def __init__(self, module, message: str = "'module:commands' must be defined") -> None:
        super().__init__(module, message)


class InvalidModuleCommandsTypeException(ParseException):
    def __init__(self, module, message: str = "Invalid 'module:commands' type, must be a list") -> None:
        super().__init__(module, message)


class InvalidModuleCommandTypeException(ParseException):
    def __init__(self, module,
                 message: str = "Invalid 'module:command:<generic>' type, must be a list or string") -> None:
        super().__init__(module, message)


class UnknownModuleException(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Unknown module: {name}")
