import os


def env(key, default=None):
    try:
        return os.environ.get(key, default)
    except KeyError:
        return None
