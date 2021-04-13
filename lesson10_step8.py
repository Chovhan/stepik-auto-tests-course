import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome(executable_path="Files/chromedriver.exe")

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

browser.find_element_by_id("book").click()

value = browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(calc(int(value)))
browser.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(30)
browser.quit()