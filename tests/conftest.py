def pytest_addoption(parser):
    parser.addoption("--real", action="store_true",
                     help="real request")
