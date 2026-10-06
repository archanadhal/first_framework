class Checkout_stepone:
    fname="id","first-name"
    lname="id","last-name"
    zcode="id","postal-code"
    cancel="id","cancel"
    continuee="id","continue"

    def __init__(self,driver):
        self.driver=driver


    def enter_fname(self,fn):
        self.driver.find_element(*Checkout_stepone.fname).send_keys(fn)

    def enter_lname(self,ln):
        self.driver.find_element(*Checkout_stepone.lname).send_keys(ln)

    def enter_zcode(self,zc):
        self.driver.find_element(*Checkout_stepone.zcode).send_keys(zc)

    def click_cancel(self):
        self.driver.find_element(*Checkout_stepone.cancel).click()

    def click_continue(self):
        self.driver.find_element(*Checkout_stepone.continuee).click()


