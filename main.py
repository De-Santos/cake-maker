from constant import flog
from setup import docker
from setup import kube

if __name__ == '__main__':
    flog.log("start application")
    print(docker.docker_client.version())
    print(kube.kubernetes_api.list_node())
    # print(kube.kubernetes_api.get_api_resources())
