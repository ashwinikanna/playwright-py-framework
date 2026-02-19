from playwright.sync_api import sync_playwright
import pytest

# initialize Playwright once per session to optimize execution speed.
@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p

#Each test gets a fresh browser instance
@pytest.fixture()
def browser(pw, request):
    headless = request.config.getoption("--headless").lower() == "true"
    slowmo = int(request.config.getoption("--slowmo"))

    browser = pw.chromium.launch(headless=headless, slow_mo=slowmo)
    yield browser
    browser.close()

# Using a new browser context per test to ensure session isolation and prevent state leakage.
@pytest.fixture()
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture()
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture()
def base_url():
    return "https://practicesoftwaretesting.com"


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="true")
    parser.addoption("--slowmo", action="store", default="0")  # ms



        