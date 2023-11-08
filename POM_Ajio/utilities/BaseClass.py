import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass
