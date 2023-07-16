import click

from constant import clog, build_config_path
from entities import Module
from parser import BuildParser

build_config = BuildParser(build_config_path)


@click.group()
def commands():
    pass


@click.command()
@click.argument("module", type=click.STRING, required=1)
@click.argument("command", type=click.STRING, required=1)
def run(module, command):
    module: Module = build_config.parse(module)
    module_command = module.commands.get(command)
    if module_command is None:
        clog.error(f"Command {command} not found")
        return
    print(f"Execute commands: {module_command}")


commands.add_command(run)
