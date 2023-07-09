from kubernetes import config, client
from kubernetes.client.rest import ApiException
from kubernetes.config import ConfigException

from constant import clog, flog

_message: str = "Application failed to start:"
_config_exception_message: str = "Error occurred while configuring Kubernetes"
_create_api_client_exception_message: str = "Error occurred while creating the API client"

try:
    # Configure Kubernetes
    config.load_kube_config()

    # Create Kubernetes API client
    kubernetes_api = client.CoreV1Api()

except ConfigException as e:
    clog.critical(_config_exception_message)
    flog.critical(f"{_message} {_config_exception_message}: {str(e)}")
    exit()
except ApiException as e:
    clog.critical(_create_api_client_exception_message)
    flog.critical(f"{_message} {_create_api_client_exception_message}: {str(e)}")
    exit()
