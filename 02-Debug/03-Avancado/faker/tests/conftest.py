import pytest

from faker import Faker


@pytest.fixture(scope="session")
def faker():
    return Faker()


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return "Trybe"


@pytest.fixture(scope="session", autouse=True)
def faker_locale():
    return "pt_BR"
