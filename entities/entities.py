class Module:

    name: str
    path: str
    dockerfile_path: str
    commands: dict[str, list[str]]

    def __init__(self, name: str, path: str, dockerfile_path: str, commands: dict[str, list[str]]) -> None:
        self.name = name
        self.path = path
        self.dockerfile_path = dockerfile_path
        self.commands = commands
