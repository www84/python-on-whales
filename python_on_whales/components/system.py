from python_on_whales.client_config import DockerCLICaller
from python_on_whales.utils import run


class SystemCLI(DockerCLICaller):
    def prune(self, all: bool = False, force: bool = False, volumes: bool = False):
        full_cmd = self.docker_cmd + ["system", "prune"]
        full_cmd.add_flag("--all", all)
        full_cmd.add_flag("--force", force)
        full_cmd.add_flag("--volumes", volumes)
        run(full_cmd)