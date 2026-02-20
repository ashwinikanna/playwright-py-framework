from pages.base_page import BasePage

class LoginPage(BasePage):

#Locators 
    SIGN_IN_LINK = '[data-test="nav-sign-in"]'
    #EMAIL_INPUT = '#email'
    PASSWORD_INPUT = '[data-test="password"]'
    ERROR_MESSAGE = "text=Invalid email or password"

#Methods / Actions
    def open_sign_in(self):
        self.click(self.SIGN_IN_LINK)

    def enter_email(self, email: str):
        self.page.get_by_label("Email").fill(email)

    def enter_password(self, password: str):
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def submit(self):
        self.click_by_role("button", "Login")

    def expect_login_error(self):
        self.page.locator(self.ERROR_MESSAGE).wait_for(state="visible")
