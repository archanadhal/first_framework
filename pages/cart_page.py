from time import sleep

class CartPage:
    continue_shopping="id","continue-shopping"
    products="xpath","//div[@class='cart_item']"
    remove="id","remove-sauce-labs-backpack"
    checkout="id","checkout"

    def __init__(self,driver):
        self.driver=driver

    def click_continue_shopping(self):
        self.driver.find_element(*CartPage.continue_shopping).click()
        sleep(3)

    def product_displayed(self):
        return self.driver.find_element(*CartPage.products).is_displayed()

    def click_remove_btn(self):
        self.driver.find_element(*CartPage.remove).click()
        sleep(2)

    def click_checkout(self):
        self.driver.find_element(*CartPage.checkout).click()
        sleep(2)


