from config import Config
from pytest import fixture


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tsts against"
    )


@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg

# Reference: https://docs.python.org/3/library/argparse.html#action