#Testcase1:-
#Open browser
# login
# check whether products are displayed or not
# expected result---> products should be displayed

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.read_login import get_testcase1_data
t,u,p=get_testcase1_data()
from time import sleep

def login(driver):
    l=LoginPage(driver)
    l.enter_username(u)
    l.enter_pwd(p)
    l.click_log_btn()
    sleep(3)

def test_products_displayed(driver):
    login(driver)
    In = InventoryPage(driver)
    assert In.get_products(),driver.save_screenshot("screenshots/product_not_displayed.png")


# Testcase2:-
# Open browser
#login
#verify add to cart button is working or not
# expected result ---> product added to cart

def test_add_to_cart(driver):
    login(driver)
    In = InventoryPage(driver)
    In.add_product_to_cart()
    sleep(3)
    assert In.get_text_cart()=='1',driver.save_screenshot("screenshots/add_to_cart.png")
    sleep(3)


# Testcase3:-
# Open browser
#login
#add to cart
# click on cart
# verify cart page is opened or not
# expected result is cart page


def test_click_cart(driver):
    login(driver)
    In = InventoryPage(driver)
    In.click_cart()
    sleep(3)
    assert driver.current_url=='https://www.saucedemo.com/cart.html',driver.save_screenshot("screenshots/cart_page_not_opened.png")