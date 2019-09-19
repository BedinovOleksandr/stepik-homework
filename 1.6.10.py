"""Попробуем реализовать один из автотестов из предыдущего шага.
Вам дана страница с формой регистрации.
Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *:
First name, last name, email.
Текст для полей может быть любым.
Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!"
с текстом на странице, которая открывается после регистрации.
Для сравнения воспользуемся стандартной конструкцией assert из языка Python."""
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    reg_elem = browser.find_elements_by_xpath("/html/body/div/form/div[1]/div/input")
    #assert len(reg_elem) == 3, 'не достаточно полей'
    reg_elem[0].send_keys('Alex')
    reg_elem[1].send_keys('Bedinov')
    reg_elem[2].send_keys(r'alekzzandr@gmail.com')

    # Отправляем заполненную форм
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()