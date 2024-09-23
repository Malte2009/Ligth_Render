import toml

def read():
    with open("./config.toml", "r") as f:
        return toml.load(f)