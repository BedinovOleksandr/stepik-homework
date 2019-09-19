"""Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit"."""

import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
browser.find_element_by_id('input_value')
browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
robotCheckbox = browser.find_element_by_id('robotCheckbox')
browser.execute_script("window.scrollBy(0, 100);")
robotCheckbox.click()
robotsRule = browser.find_element_by_id('robotsRule')
robotsRule.click()
button = browser.find_element_by_tag_name('button')
button.click()
