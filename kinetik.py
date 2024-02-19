""" Every time you execute the script, remember to update the email at line 68 of the kinetik.py file """
# importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

# installing chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# opening the event scheduler page
driver.get('https://automationexercise.com')
time.sleep(3)
driver.maximize_window()

# Verify that home page is visible successfully
try:
    expected_url = 'https://automationexercise.com/'
    assert expected_url == driver.current_url
    print("Home page loaded successfully.")
except Exception as e:
    print("Failed to load home page:", e)
    print(expected_url, driver.current_url)

# add products to cart
men_tshirt = driver.find_element(by='xpath', value="(//a[contains(text(),'Add to cart')])[3]")

# Create an instance of ActionChains
actions = ActionChains(driver)

actions.move_to_element(men_tshirt).perform()
time.sleep(1)
men_tshirt_modal = driver.find_element(by='xpath', value="//div[3]//div[1]//div[1]//div[2]//div[1]//a[1]")
men_tshirt_modal.click()
time.sleep(2)

# view cart item 
view_cart = driver.find_element(by='xpath', value="//p[@class='text-center']//a")
view_cart.click()
time.sleep(2)

# verify cart page is displayed
try:
    expected_url = "https://automationexercise.com/view_cart"
    assert expected_url == driver.current_url
    print("Cart page is displayed successfully")
except Exception as e:
    print("Failed to display cart page:", e)
    print(expected_url, driver.current_url)

# proceed to checkout
checkout_button = driver.find_element(by='xpath', value="(//a[normalize-space()='Proceed To Checkout'])[1]")
checkout_button.click()
time.sleep(1)

# click Register/Login button
register_login_button = driver.find_element(by='xpath', value="//div[@class='modal-body']//a")
register_login_button.click()
time.sleep(2)

name_input = driver.find_element(by='xpath', value="(//input[@placeholder='Name'])[1]")
name_input.send_keys('rifat1')
time.sleep(1)

email_input = driver.find_element(by='xpath', value="(//input[@data-qa='signup-email'])[1]")
# Every time you execute the script, remember to update the email below
email_input.send_keys('rifat7@yopmail.com')
time.sleep(1)

signup_button = driver.find_element(by='xpath', value="(//button[normalize-space()='Signup'])[1]")
signup_button.click()
time.sleep(2)

title = driver.find_element(by='xpath', value="//label[normalize-space()='Mr.']")
title.click()
time.sleep(1)

password = driver.find_element(by='xpath', value="//input[@id='password']")
password.send_keys('Rifat1@yopmail')
time.sleep(1)

# day dob
day = driver.find_element(by='xpath', value="//select[@id='days']")
day_options = Select(day)
day_options.select_by_value("26")
time.sleep(1)

month = driver.find_element(by='xpath', value="//select[@id='months']")
month_options = Select(month)
month_options.select_by_visible_text("April")
time.sleep(1)

year = driver.find_element(by='xpath', value="//select[@id='years']")
year_options = Select(year)
year_options.select_by_visible_text("1997")
time.sleep(1)

driver.find_element(by='xpath', value="//input[@id='newsletter']").click()
driver.find_element(by='xpath', value="//input[@id='optin']").click()

first_name = driver.find_element(by='xpath', value="//input[@id='first_name']")
first_name.send_keys('rifat')
time.sleep(1)

last_name = driver.find_element(by='xpath', value="//input[@id='last_name']")
last_name.send_keys('taher')
time.sleep(1)

company = driver.find_element(by='xpath', value="//input[@id='company']")
company.send_keys('kinetik')
time.sleep(1)

address = driver.find_element(by='xpath', value="//input[@id='address1']")
address.send_keys('xyz')
time.sleep(1)

address2 = driver.find_element(by='xpath', value="//input[@id='address2']").send_keys('xyz2')

country = driver.find_element(by='xpath', value="//select[@id='country']")
country_options = Select(country)
country_options.select_by_visible_text("India")
time.sleep(1)

state = driver.find_element(by='xpath', value="//input[@id='state']")
state.send_keys('Maharashtra')
time.sleep(1)

city = driver.find_element(by='xpath', value="//input[@id='city']")
city.send_keys('Mumbai')
time.sleep(1)

zipcode = driver.find_element(by='xpath', value="//input[@id='zipcode']")
zipcode.send_keys('400001')
time.sleep(1)

mobile = driver.find_element(by='xpath', value="//input[@id='mobile_number']")
mobile.send_keys('01700000000')
time.sleep(1)

create_account_btn = driver.find_element(by='xpath', value="//button[normalize-space()='Create Account']")
create_account_btn.click()
time.sleep(3)

# verify account creation
try:
    expected_url = "https://automationexercise.com/account_created"
    assert expected_url == driver.current_url
    print("Account created successfully")
except Exception as e:
    print("Failed to create account", e)
    print(driver.current_url)

continue_to_profile = driver.find_element(by='xpath', value="//a[normalize-space()='Continue']").click()
time.sleep(2)

user_name = driver.find_element(by='xpath', value="//b[normalize-space()='rifat1']").text 

try:
    expected_user_name = "rifat1"
    assert expected_user_name == user_name
    print("User name matched successfully")
except Exception as e:
    print("Error occured while trying to match user name", e)
    print(user_name)

cart = driver.find_element(by='xpath', value="//header[@id='header']//li[3]/a").click()
time.sleep(2)

proceed_to_checkout = driver.find_element(by='xpath', value="//a[normalize-space()='Proceed To Checkout']").click()
time.sleep(2)

print('Verfied address & reviewed order')

driver.find_element(by='xpath', value="//textarea[@name='message']").send_keys("Order Comments allow customers to directly communicate with the merchant regarding a specific order")
time.sleep(1)

place_order = driver.find_element(by='xpath', value="//a[normalize-space()='Place Order']")
place_order.click()
time.sleep(2)

name_on_card = driver.find_element(by='xpath', value="//input[@name='name_on_card']")
name_on_card.send_keys('rifat taher')
time.sleep(1)

card_no = driver.find_element(by='xpath', value="//input[@name='card_number']")
card_no.send_keys('4105202085134839')
time.sleep(1)

cvc = driver.find_element(by='xpath', value="//input[@placeholder='ex. 311']").send_keys('786')
time.sleep(1)
expiration_month = driver.find_element(by='xpath', value="//input[@placeholder='MM']").send_keys('07')
time.sleep(1)
expiration_year = driver.find_element(by='xpath', value="//input[@placeholder='YYYY']").send_keys('2028')
time.sleep(1)

pay_and_confirm = driver.find_element(by='xpath', value="//button[@id='submit']").click()
time.sleep(1)

success_message = driver.find_element(by='xpath', value="//p[normalize-space()='Congratulations! Your order has been confirmed!']").text

try:
    expected_message = "Congratulations! Your order has been confirmed!"
    assert expected_message == success_message
    print("Congratulations! Your order has been confirmed!")
except Exception as e:
    print("Error occured while trying to", e)

time.sleep(5)

# closing the webdriver
driver.close()