"""Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом"""
import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser.get(link)
    browser.find_element_by_class_name('btn.btn-primary').click()
    browser.switch_to.alert.accept()
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    browser.find_element_by_class_name('btn.btn-primary').click()
    print(browser.switch_to.alert.text)

  #  browser.
finally:
    time.sleep(5)
    browser.quit()

