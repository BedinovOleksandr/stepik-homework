"""Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота,
чтобы он справился с новым заданием.
Напишите код, который реализует следующий сценарий:
Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"""

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# ссылка на стартовую страницу


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # находим сумму
    sum_for_search = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum_for_search))
    browser.find_element_by_tag_name('button').click()
    print(browser.switch_to.alert.text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
