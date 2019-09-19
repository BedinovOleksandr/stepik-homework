"""Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов,
то есть тест, являющийся простым для компьютера, но сложным для человека.
Ваша программа должна выполнить следующие шаги:
Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit."""

from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    #browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    #browser.find_element_by_id('robotCheckbox').click()
    #browser.find_element_by_id('robotsRule').click()
    #browser.find_element_by_tag_name('button').click()
    #print(browser.switch_to.alert.text)
    print(browser.find_element_by_id('robotsRule').get_attribute('checked'))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()