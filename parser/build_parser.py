import os.path

import yaml

from utils.color_warnings import warnings
from . import validator
from .constants import example_project_not_config
from .exceptions import (
    BuildConfigurationFileNotFoundException,
    InvalidProjectValue,
)


class BuildParser:

    def __init__(self, config_path: str) -> None:
        self._config = self._load_config_file(config_path)
        self._expect_full_path: bool = False
        self._project: dict = self._parse_project()
        self._modules: dict = self._parse_modules()

    @staticmethod
    def _load_config_file(path: str) -> dict:
        try:
            with open(path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise BuildConfigurationFileNotFoundException(path)

    def _parse_project(self, ) -> dict:
        project: dict = self._config.get('project')
        if project is None:
            warnings.warn(f"Project not configured, better to configure it like: {example_project_not_config}")
            self._expect_full_path = True
        elif isinstance(project, dict):
            validator.validate_project(project)
            if project.get('name') is None:
                dir_name: str = os.path.basename(project.get('path'))
                warnings.warn(f"Project name not configured, using directory name as project name: '{dir_name}'")
                project['name'] = dir_name
                return project
            return project
        elif isinstance(project, bool):
            if project is False:
                self._expect_full_path = True
                return dict()
            else:
                warnings.warn(f"Invalid 'project' value: {project}")
                raise InvalidProjectValue()

    def _parse_modules(self) -> dict:
        modules: list[dict] = self._config.get('modules')
        validator.validate_modules(modules, self._project)
        return {module.get('name'): module for module in modules}

    def parse(self, module: str):
        # TODO: this method will parse modules and return module by name
        raise NotImplementedError()
