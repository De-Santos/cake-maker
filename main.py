from setup import docker
from setup import kube

if __name__ == '__main__':
    from constant import flog
    flog.log("start application")
    print(docker.docker_client.version())
    print(kube.kubernetes_api.list_node())
