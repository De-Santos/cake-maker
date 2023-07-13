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


class ProjectNotFoundException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Project not found by path: {path}")


class InvalidProjectNameException(Exception):
    def __init__(self, message: str = "Invalid 'project:name' type, must be a string") -> None:
        super().__init__(message)


class InvalidProjectValue(Exception):
    def __init__(self, message: str = "Invalid 'project' value") -> None:
        super().__init__(message)


class ModulesNotDefinedException(Exception):
    def __init__(self, message: str = "'modules' not defined") -> None:
        super().__init__(message)


class InvalidModuleTypeException(Exception):
    def __init__(self, message: str = "Invalid 'module' type, must be a header") -> None:
        super().__init__(message)


class ModuleNameNotDefinedException(Exception):
    def __init__(self, message: str = "'module:name' must be defined") -> None:
        super().__init__(message)


class ModuleNameDuplicateException(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"'module:name' must be unique, duplicated name: {name}")


class InvalidModuleNameTypeException(Exception):
    def __init__(self, message: str = "Invalid 'module:name' type, must be a string") -> None:
        super().__init__(message)


class ModulePathNotDefinedException(Exception):
    def __init__(self, message: str = "'module:path' must be defined") -> None:
        super().__init__(message)


class InvalidModulePathTypeException(Exception):
    def __init__(self, message: str = "Invalid 'module:path' type, must be a string") -> None:
        super().__init__(message)


class ModuleNotFoundException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Module not found by path: {path}")


class ModuleNotADirectoryException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Module must be folder by path: {path}")


class ModuleDockerfilePathNotDefinedException(Exception):
    def __init__(self, message: str = "'module:dockerfile_path' must be defined") -> None:
        super().__init__(message)


class InvalidModuleDockerfilePathTypeException(Exception):
    def __init__(self, message: str = "Invalid 'module:dockerfile_path' type, must be a string") -> None:
        super().__init__(message)


class ModuleDockerfileNotFoundException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Module dockerfile not found by path: {path}")


class ModuleDockerfileNotAFileException(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Module dockerfile must be file by path: {path}")


class ModulePushCommandsNotDefinedException(Exception):
    def __init__(self, message: str = "'module:local_push_commands' must be defined") -> None:
        super().__init__(message)


class InvalidModulePushCommandsTypeException(Exception):
    def __init__(self,
                 message: str = "Invalid 'module:local_push_commands/cloud_push_commands' type, must be a list"
                 ) -> None:
        super().__init__(message)
