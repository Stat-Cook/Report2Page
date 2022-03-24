import yaml

class ConfigParse:

    def __init__(self, path):
        self.path = path
        try:
            with open(path, "r") as f:
                self.config = yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"No config file found at {path}.  Please create one.")

    @property
    def paths(self):
        return self.config["paths"]




if __name__ == '__main__':
    cp = ConfigParse("config.yaml")

    print(cp.paths)
