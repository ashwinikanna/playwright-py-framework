from pages.login_page import LoginPage


class LoginFlow:
    def __init__(self, page):
        self.login_page = LoginPage(page)

    """ 
    def login(self, base_url, email, password):
        self.login_page.goto(f"{base_url}/auth/login") 
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.submit()
    """

    def login(self, base_url, email, password): 
        self.login_page.goto(base_url) 
        self.login_page.open_sign_in() 
       # self.login_page.enter_email(email) 
       # self.login_page.enter_password(password) 
       # self.login_page.submit()