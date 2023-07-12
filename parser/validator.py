import os

from utils.color_warnings import warnings
from .exception import (
    ProjectPathNotDefinedException,
    InvalidProjectPathTypeException,
    ProjectNotADirectoryException,
    InvalidProjectNameException
)

example_project_config: str = """
project:
    path: C:\\Example\\Path\\To\\Project\\Folder
    name: ExampleProjectName
"""


def _validate_project_path(project: dict):
    path = project.get('path')
    if path is None:
        warnings.warn(f"Project path not configured, better to configure it like: {example_project_config}")
        raise ProjectPathNotDefinedException()
    elif not isinstance(path, str):
        warnings.warn(
            f"Invalid 'project:path' type, 'path' must be a string, example: {example_project_config}")
        raise InvalidProjectPathTypeException()
    else:
        if not os.path.exists(path):
            warnings.warn(f"Project not found by path: {path}")
            raise FileNotFoundError()
        if not os.path.isdir(path):
            warnings.warn(f"Project must be folder: {path}")
            raise ProjectNotADirectoryException()


def _validate_project_name(project: dict):
    name = project.get('name')
    if name is None:
        return
    if not isinstance(name, str):
        warnings.warn(f"Invalid 'project:name' type, 'name' must be a string, example: {example_project_config}")
        raise InvalidProjectNameException()


def validate_project(project: dict):
    _validate_project_path(project)
    _validate_project_name(project)
