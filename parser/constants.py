example_project_not_config: str = """
project: False
"""
example_project_config: str = """
project:
    path: C:\\Example\\Path\\To\\Project\\Folder
    name: ExampleProjectName
"""
example_modules_config: str = """
modules:
  - module:
      name: user-service
      path: \\user-service # Relative path to the module folder
      dockerfile_path: \\user-service\\docker\\user-dockerfile
      local_push_commands: [
          "docker build -t localhost:5000/user-service -f user-dockerfile .",
          "docker push localhost:5000/user-service"
      ]
      cloud_push_commands: [
          "docker build -t could.registry/user-service -f user-dockerfile .",
          "docker push cloud.registry/user-service"
      ]
"""
