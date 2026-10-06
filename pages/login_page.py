class LoginPage:
    username="id","user-name"
    pwd="id","password"
    login_btn="id","login-button"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.username).send_keys(username)

    def enter_pwd(self,pwd):
        self.driver.find_element(*LoginPage.pwd).send_keys(pwd)

    def click_log_btn(self):
        self.driver.find_element(*LoginPage.login_btn).click()