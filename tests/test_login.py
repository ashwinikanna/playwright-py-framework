from flows.login_flow import LoginFlow
from pages.login_page import LoginPage


def test_invalid_login(page, base_url):
    flow = LoginFlow(page)
    flow.login(base_url, "fake@test.com", "wrongpass")
   # LoginPage(page).expect_login_error()


   

