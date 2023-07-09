import os

import docker
from kubernetes import client, config

from setup import LoggerSetup

# Configure Kubernetes
config.load_kube_config()

# Create Kubernetes API client
kubernetes_api = client.CoreV1Api()

# Create Docker client
docker_client = docker.from_env()

# Get the absolute path to a file in the current directory
log_config_path = os.path.abspath("logging.yaml")

logger = LoggerSetup(log_config_path).setup_file_logging()

if __name__ == '__main__':
    logger.error("first python log")
