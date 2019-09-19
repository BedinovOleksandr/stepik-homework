"""Задание: поиск элемента по XPath"""
from selenium import webdriver
import time


try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    link = r'http://suninjuly.github.io/find_xpath_form'
    browser.get(link)
    browser.find_element_by_tag_name('input[name="first_name"]').send_keys("Ivan")
    browser.find_element_by_name('last_name').send_keys("Petrov")
    browser.find_element_by_class_name('form-control.city').send_keys("Smolensk")
    browser.find_element_by_id('country').send_keys("Russia")
    browser.find_element_by_xpath('//button[@type="submit"]').click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

