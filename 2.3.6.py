"""Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и
решить в ней задачу.
Сценарий для реализации выглядит так:
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""
import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser.get(link)
    browser.find_element_by_class_name('trollface.btn.btn-primary').click()
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    browser.find_element_by_class_name('btn.btn-primary').click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(5)
    browser.quit()

