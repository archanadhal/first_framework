from test_cases.test_inventory import login
from pages.inventory_page import InventoryPage
from time import sleep
from pages.cart_page import CartPage

def log(driver):
    login(driver)
    sleep(3)
    In=InventoryPage(driver)
    In.add_product_to_cart()
    In.click_cart()
    sleep(3)
    C= CartPage(driver)
    C.click_checkout()
    sleep(3)


# Testcase1:-
# login
# add product to cart thn click cart
# click on checkout
# enter valid firstname,lastname,zipcode
# click on continue
# expected result---> checkout step two page should display

from pages.checkout_stepone import Checkout_stepone
from utilities.read_login import get_row2
t,un,pwd,fname,lname,zipcode = get_row2()


def test_verify_correct_cred(driver):
    log(driver)
    Check = Checkout_stepone(driver)
    Check.enter_fname(fname)
    Check.enter_lname(lname)
    Check.enter_zcode(zipcode)
    Check.click_continue()
    sleep(3)

    assert driver.current_url=='https://www.saucedemo.com/checkout-step-two.html',driver.save_screenshot("screenshots/valid_credentials.png")



# Testcase2:-
# login
# add product to cart thn click cart
# click on checkout
# keep first name field empty,thn enter lastname,thn enter zipcode
# click on continue
# expected result---> same should display

from utilities.read_login import get_invalid_fname
fn,ln,zip_code = get_invalid_fname()

def test_incorrect_fname(driver):
    log(driver)
    Check = Checkout_stepone(driver)
    Check.enter_fname(fn)
    Check.enter_lname(ln)
    Check.enter_zcode(zip_code)
    Check.click_continue()
    sleep(3)

    assert driver.current_url=='https://www.saucedemo.com/checkout-step-one.html',driver.save_screenshot("screenshots/invalid_credentials.png")


# Testcase3:-
# login
# add product to cart thn click cart
# click on checkout
# click on cancel
# expected result----> previous page(cart page should display)

def test_cancel_btn(driver):
    log(driver)
    Check = Checkout_stepone(driver)
    Check.click_cancel()
    sleep(3)

    assert driver.current_url=='https://www.saucedemo.com/cart.html',driver.save_screenshot("screenshots/cancel.png")