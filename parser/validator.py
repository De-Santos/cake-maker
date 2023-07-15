import os

from utils.color_warnings import warnings
from .constants import example_modules_config
from .constants import example_project_config
from .exceptions import (
    ProjectPathNotDefinedException,
    InvalidProjectPathTypeException,
    ProjectNotADirectoryException,
    InvalidProjectNameException,
    InvalidModuleTypeException,
    InvalidModuleNameTypeException,
    ModuleNameNotDefinedException,
    ModulePathNotDefinedException,
    InvalidModulePathTypeException,
    ProjectNotFoundException,
    ModuleNotFoundException,
    ModuleNotADirectoryException,
    ModuleDockerfilePathNotDefinedException,
    InvalidModuleDockerfilePathTypeException,
    ModuleDockerfileNotFoundException,
    ModuleDockerfileNotAFileException,
    ModulesNotDefinedException,
    ModuleNameDuplicateException,
    ModuleCommandsNotDefinedException,
    InvalidModuleCommandsTypeException,
    InvalidModuleCommandTypeException
)


def _validate_project_path(project: dict):
    path = project.get('path')
    if path is None:
        warnings.warn(f"Project path not configured, better to configure it like: {example_project_config}")
        raise ProjectPathNotDefinedException(project)
    elif not isinstance(path, str):
        warnings.warn(
            f"Invalid 'project:path' type, 'path' must be a string, example: {example_project_config}")
        raise InvalidProjectPathTypeException(project)
    else:
        if not os.path.exists(path):
            warnings.warn(f"Project not found by path: {path}")
            raise ProjectNotFoundException(path)
        if not os.path.isdir(path):
            warnings.warn(f"Project must be folder: {path}")
            raise ProjectNotADirectoryException()


def _validate_module_name(module: dict, exist_module_names: set):
    if module.get('name') is None:
        warnings.warn(f"'module:name' not defined, example: {example_modules_config}")
        raise ModuleNameNotDefinedException(module)
    elif not isinstance(module.get('name'), str):
        warnings.warn(f"Invalid 'module:name' type, 'name' must be a string, example: {example_modules_config}")
        raise InvalidModuleNameTypeException(module)
    elif module.get('name') in exist_module_names:
        warnings.warn("'module:name' must be unique")
        raise ModuleNameDuplicateException(module)
    else:
        exist_module_names.add(module.get('name'))


def _validate_module_path(module: dict, project_path: str):
    path = module.get('path')
    if path is None:
        warnings.warn(f"'module:path' not defined, example: {example_modules_config}")
        raise ModulePathNotDefinedException(module)
    elif not isinstance(path, str):
        warnings.warn(f"Invalid 'module:path' type, 'path' must be a string, example: {example_modules_config}")
        raise InvalidModulePathTypeException(module)
    else:
        if not os.path.isabs(path):
            path = os.path.join(project_path, path)
        if not os.path.exists(path):
            warnings.warn(f"Module not found by path: {path}")
            raise ModuleNotFoundException(path)
        if not os.path.isdir(path):
            warnings.warn(f"Module must be folder: {path}")
            raise ModuleNotADirectoryException(module, path)


def _validate_dockerfile_path(module: dict):
    path = module.get('dockerfile_path')
    if path is None:
        warnings.warn(f"'module:dockerfile_path' not defined, example: {example_modules_config}")
        raise ModuleDockerfilePathNotDefinedException(module)
    elif not isinstance(path, str):
        warnings.warn(
            f"Invalid 'module:dockerfile_path' type, 'dockerfile_path' must be a string, \
            example: {example_modules_config}")
        raise InvalidModuleDockerfilePathTypeException(module)
    else:
        if not os.path.exists(path):
            warnings.warn(f"Module dockerfile not found by path: {path} P.S. Full path required")
            raise ModuleDockerfileNotFoundException(module, path)
        if not os.path.isfile(path):
            warnings.warn("Module dockerfile must be file")
            raise ModuleDockerfileNotAFileException(module, path)


def _validate_commands(module: dict):
    commands = module.get('commands')
    if commands is None:
        warnings.warn(f"'module:commands' not defined, example: {example_modules_config}")
        raise ModuleCommandsNotDefinedException(module)
    elif not isinstance(commands, dict):
        warnings.warn(
            f"Invalid 'module:commands' type, 'commands' must be a list or string, \
            example: {example_modules_config}")
        raise InvalidModuleCommandsTypeException(module)
    for command in dict(commands).values():
        if not isinstance(command, str) and not isinstance(command, list):
            warnings.warn(
                f"Invalid 'module:commands' type, 'commands' must be a list or string, \
                example: {example_modules_config}")
            raise InvalidModuleCommandTypeException(module)


def _validate_project_name(project: dict):
    name = project.get('name')
    if name is None:
        return
    if not isinstance(name, str):
        warnings.warn(f"Invalid 'project:name' type, 'name' must be a string, example: {example_project_config}")
        raise InvalidProjectNameException(project)


def validate_project(project: dict):
    _validate_project_path(project)
    _validate_project_name(project)


def validate_modules(modules: list, project: dict, expect_full_path: bool):
    if modules is None:
        warnings.warn(f"Modules must be defined, example: {example_modules_config}")
        raise ModulesNotDefinedException()
    elif isinstance(modules, list):
        module_names: set = set()
        for module in modules:
            if not isinstance(module, dict):
                warnings.warn(f"Invalid 'module' type, 'module' must be a dict, example: {example_modules_config}")
                raise InvalidModuleTypeException(module)
            else:
                _validate_module_name(module, module_names)
                if expect_full_path:
                    _validate_module_path(module, "")
                else:
                    _validate_module_path(module, project.get('path'))
                _validate_dockerfile_path(module)
                _validate_commands(module)
