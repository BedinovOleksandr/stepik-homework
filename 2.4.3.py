"""Открыть страницу http://suninjuly.github.io/wait1.html
Нажать на кнопку "Verify"
Проверить, что появилась надпись "Verification was successful!"
"""
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)  # хороший способ.
browser.get("http://suninjuly.github.io/wait1.html")
# time.sleep(5) # Плохой способ
button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text