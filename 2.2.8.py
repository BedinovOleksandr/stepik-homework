"""Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.
Напишите скрипт, который будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"""
from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')


# ссылка на стартовую страницу
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # находим значение спрятанное в сундучке. Делаем расчет. Вставляем значение в поле
    browser.find_element_by_name('firstname').send_keys('Oleksandr')
    browser.find_element_by_name('lastname').send_keys('Bedinov')
    browser.find_element_by_name('email').send_keys('alekzzandr@gmail.com')
    # находим нужные айдишки. Кликаем
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_class_name('btn.btn-primary').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
