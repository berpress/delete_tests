from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 1. окрыть главную страницу
# 2. открыть страницу логин
# 3. заполнить поле email
# 4. заполнить поле password
# 5. нажать кнопку start

URL = 'https://berpress.github.io/react-shop/'
LOGIN = 'test@test.com'
PASSWORD = 'Password1'


def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def open_page(driver, url):
    driver.get(url)


def get_element_by_id(xpath, driver):
    element = driver.find_element(By.ID, xpath)
    return element

def element_click(xpath, driver):
    element = get_element_by_id(xpath=xpath, driver=driver)
    element.click()

def element_send_keys(xpath, driver, text):
    element = get_element_by_id(xpath=xpath, driver=driver)
    element.clear()
    element.send_keys(text)

# 1
driver = get_driver()
open_page(driver, URL)
element_click(xpath='login-link', driver=driver)
element_send_keys(xpath="name", driver=driver, text=LOGIN)
element_send_keys(xpath="password", driver=driver, text=PASSWORD)
element_click(xpath='register', driver=driver)
