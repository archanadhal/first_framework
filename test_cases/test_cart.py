from test_cases.test_inventory import login
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from time import sleep

# Testcase1:
# open browser
# login urself
# add to cart product
# verify continue shopping working or not
# expected result ---> inventory page url should display


def test_verify_continue_shopping(driver):
    login(driver)
    sleep(3)
    Inv=InventoryPage(driver)
    Inv.add_product_to_cart()
    sleep(2)
    Inv.click_cart()
    sleep(2)
    cp=CartPage(driver)
    cp.click_continue_shopping()
    sleep(3)

    assert driver.current_url=='https://www.saucedemo.com/inventory.html',driver.save_screenshot("screenshots/continue_shopping.png")


# Testcase2:-
# open browser
# login urself
# add to cart product
# verify product is displayed or not
# expected result---> product should display


def test_verify_products_displayed(driver):
    login(driver)
    sleep(2)
    Inv = InventoryPage(driver)
    Inv.add_product_to_cart()
    sleep(2)
    Inv.click_cart()
    sleep(2)
    cp = CartPage(driver)

    assert cp.product_displayed(),driver.save_screenshot("screenshots/product_not_displayed")
    sleep(2)


# Testcase3:-
# open browser
# login urself
# add to cart product
# click checkout
# expected result ---> checkout page should display

def test_checkout_btn(driver):
    login(driver)
    sleep(3)
    In= InventoryPage(driver)
    In.add_product_to_cart()
    In.click_cart()
    sleep(3)
    c = CartPage(driver)
    c.click_checkout()
    sleep(3)

    assert driver.current_url=='https://www.saucedemo.com/checkout-step-one.html',driver.save_screenshot("screesnhots/checkout_btn.png")



# TestCase4:
# open browser
# login urself
# add to cart product
# click remove
# expected result ----> product should not display

'''def test_remove_btn(driver):
    login(driver)
    sleep(3)
    In= InventoryPage(driver)
    In.add_product_to_cart()
    In.click_cart()
    c = CartPage(driver)
    c.click_remove_btn()
    sleep(3)

    assert c.product_displayed(),driver.save_screenshot("screesnhots/remove_btn.png")'''

