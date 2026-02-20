from pages.base_page import BasePage

class LoginPage(BasePage):

#Locators 
    SIGN_IN_LINK = '[data-test="nav-sign-in"]'
    EMAIL_INPUT = '[data-test="email"]'
    PASSWORD_INPUT = '[data-test="password"]'
    ERROR_MESSAGE = "text=Invalid email or password"

#Methods / Actions
    def open_sign_in_o(self):
        self.click_by_role("link", "Sign in")

    def open_sign_in(self):
        print("URL:", self.page.url)
        print("Sign-in count:", self.page.locator('a[data-test="nav-sign-in"]').count())
        self.page.locator('a[data-test="nav-sign-in"]').click()


    def enter_email(self, email: str):
        self.fill(self.EMAIL_INPUT, email)

    def enter_password(self, password: str):
        self.fill(self.PASSWORD_INPUT, password)

    def expect_login_error(self):
        self.page.locator(self.ERROR_MESSAGE).wait_for(state="visible")
