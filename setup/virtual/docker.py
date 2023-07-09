import docker
from docker.errors import DockerException

from constant import clog, flog

_message: str = "Application failed to start:"
_docker_exception_message: str = "Error occurred while creating docker client"

try:
    # Create Docker client
    docker_client = docker.from_env()

except DockerException as e:
    clog.critical(_docker_exception_message)
    flog.critical(f"{_message} {_docker_exception_message}: {str(e)}")
    exit()
