from pages.base_page import BasePage
from config.config import BASE_URL

class LoginPage(BasePage):

    def load(self):
        self.open(BASE_URL)

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")