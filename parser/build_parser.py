import os.path

import yaml

from utils.color_warnings import warnings
from .exception import (
    BuildConfigurationFileNotFoundException,
    InvalidProjectValue
)
from .validator import validate_project

example_project_not_config: str = """
project: False
"""


class BuildParser:

    def __init__(self, config_path: str) -> None:
        self._config = self._load_config_file(config_path)
        self._expect_full_path: bool = False
        self._project: dict = self._parse_project(self._config)
        self._modules: dict = self._parse_modules(self._config)

    @staticmethod
    def _load_config_file(path: str) -> dict:
        try:
            with open(path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise BuildConfigurationFileNotFoundException(path)

    def _parse_project(self, config: dict) -> dict:
        project = config.get('project')
        if project is None:
            warnings.warn(f"Project not configured, better to configure it like: {example_project_not_config}")
            self._expect_full_path = True
        elif isinstance(project, dict):
            validate_project(project)
            if project.get('name') is None:
                dir_name: str = os.path.basename(project.get('path'))
                warnings.warn(f"Project name not configured, using directory name as project name: '{dir_name}'")
                project['name'] = dir_name
                return project
            return project
        elif isinstance(project, bool):
            if project is False:
                self._expect_full_path = True
                return {}
            else:
                warnings.warn(f"Invalid 'project' value: {project}")
                raise InvalidProjectValue()

    def _parse_modules(self, config: dict) -> dict:
        # TODO: this method will parse modules
        warnings.warn("Method not implemented yet")
        pass

    def parse(self, module: str):
        # TODO: this method will parse modules and return module by name
        raise NotImplementedError()
