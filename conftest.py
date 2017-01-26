# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
import config

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    test_env = request.config.getoption("--testenv")
    base_url = config.test_env[test_env]+config.admin_page
    print("base_url", base_url)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)
    fixture.session.login(username=config.admin['login'], password=config.admin['pwd'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop_app(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--testenv", action="store", default="localhost")
