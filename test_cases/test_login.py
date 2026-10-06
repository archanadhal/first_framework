# #test case 1:-
# #Open browser
# #enter url
# #valid login credentials
#   # ---> un = standard_user
#   # --->pwdd = secret_sauce
# # expected result---> inventory page should be opened
#
#
# from pages.login_page import LoginPage
#
#
# def test_valid_credentials(driver):
#     lp=LoginPage(driver)
#     lp.enter_username("standard_user")
#     lp.enter_pwd("secret_sauce")
#     lp.click_log_btn()
#     expected_url='https://www.saucedemo.com/inventory.html'
#     assert driver.curent_url == expected_url,driver.save_screenshot("screenshots/test_case1.png")
#
# #test case 2:-
# #Open browser
# #enter url
# #Invalid username
#   # ---> un = wrong_user
#   # --->pwdd = secret_sauce
# # expected ---> inventory page should not get opened
#
# def test_invalid_username(driver):
#     lp = LoginPage(driver)
#     lp.enter_username("wrong_user")
#     lp.enter_pwd("secret_sauce")
#     lp.click_log_btn()
#     expected_url = 'https://www.saucedemo.com/'
#     assert driver.curent_url == expected_url, driver.save_screenshot("screenshots/test_case2.png")
#
#
# # testcase 3:-
# #Open browser
# #enter url
# #Invalid password
#   # ---> un = standard_user
#   # --->pwdd = wrong_password
# # expected ---> inventory page should not get opened
#
# def test_invalid_pwd(driver):
#     lp=LoginPage(driver)
#     lp.enter_username("standard_user")
#     lp.enter_pwd("wrong_password")
#     lp.click_log_btn()
#     expected_url = 'https://www.saucedemo.com/'
#     assert driver.curent_url == expected_url, driver.save_screenshot("screenshots/test_case3.png")
#
#
# # testcase 4:-
# #Open browser
# #enter url
# #Invalid credentials
#   # ---> un = wrong_user
#   # --->pwdd = wrong_password
# expected ---> inventory page should not get opened
#
# def test_invalid_credentials(driver):
#     lp=LoginPage(driver)
#     lp.enter_username("wrong_user")
#     lp.enter_pwd("wrong_password")
#     lp.click_log_btn()
#     expected_url = 'https://www.saucedemo.com/'
#     assert driver.curent_url == expected_url, driver.save_screenshot("screenshots/test_case4.png")
#
# # testcase 5:-
# #Open browser
# #enter url
# #Invalid username2
#   # ---> un =
#   # --->pwdd =
# expected ---> inventory page should not get opened
#
#
# def test_invalid_username2(driver):
#     lp=LoginPage(driver)
#     lp.enter_username("      ")
#     lp.enter_pwd("      ")
#     lp.click_log_btn()
#     expected_url = 'https://www.saucedemo.com'
#     assert driver.curent_url == expected_url, driver.save_screenshot("screenshots/test_case5.png")
#
#
#
#note - 2nd to 5th test cases are same so we put it into parametrize

import pytest

from pages.login_page import LoginPage
from utilities.read_login import get_test_data

@pytest.mark.parametrize("testcase,username,password",get_test_data())
def test_login(driver,testcase,username,password):
    lp = LoginPage(driver)
    lp.enter_username(username)
    lp.enter_pwd(password)
    lp.click_log_btn()
    expected_url = 'https://www.saucedemo.com/'
    assert driver.current_url == expected_url, driver.save_screenshot(f"screenshots/test_case{testcase}.png")

from utilities.read_login import get_testcase1_data
test_case,user_name,pwd = get_testcase1_data()

def test_valid_credentials(driver):
    lp=LoginPage(driver)
    lp.enter_username(user_name)
    lp.enter_pwd(pwd)
    lp.click_log_btn()
    expected_url='https://www.saucedemo.com/inventory.html'
    assert driver.current_url == expected_url,driver.save_screenshot(f"screenshots/test_case{test_case}.png")