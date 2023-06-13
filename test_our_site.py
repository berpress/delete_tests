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


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 1
driver.get(URL)
# 2
login_page_button = driver.find_element(By.ID, "login-link")
login_page_button.click()
# 3, 4, 5
input_login = driver.find_element(By.ID, "name")
input_password = driver.find_element(By.ID, "password")
start_button = driver.find_element(By.ID, "register")

input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)
start_button.click()
pass