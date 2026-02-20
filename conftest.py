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
    headless = not request.config.getoption("--headed")
    browser = pw.chromium.launch(headless=headless)
    yield browser
    browser.close()

# Using a new browser context per test to ensure session isolation and prevent state leakage.
@pytest.fixture()
def context(browser):
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    yield context
    context.close()


@pytest.fixture()
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def base_url():
    return "https://practicesoftwaretesting.com"

"""
def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="true")
    parser.addoption("--slowmo", action="store", default="0")  # ms

"""




        