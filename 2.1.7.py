"""Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
Но теперь значение переменной х спрятано в "сундуке", точнее,
значение хранится в атрибуте valuex у картинки с изображением сундука.
Ваша программа должна:
Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit"."""

from selenium import webdriver
import time
import math


# Функция расчета числа
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# ссылка на стартовую страницу
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # находим значение спрятанное в сундучке. Делаем расчет. Вставляем значение в поле
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('treasure').get_attribute('valuex')))
    # находим нужные айдишки. Кликаем
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_tag_name('button').click()
    # выводим значение всплывающего окна в консоль. Что бы потом без спешки его скопировать
    print(browser.switch_to.alert.text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
