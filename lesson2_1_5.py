from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
    checkbox_robo = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox_robo.click()
    radiobutton_robo = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton_robo.click()
    buttin_submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    buttin_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()