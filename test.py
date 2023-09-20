# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
#
# driver.get(" http://suninjuly.github.io/get_attribute.html")
#
#
# val = driver.find_element(By.CSS_SELECTOR, "img[src='images/chest.png']")
#
# x = val.get_attribute("valuex")

#
# y = calc(x)
# #valuex="764"
# ans = driver.find_element(By.CSS_SELECTOR, "*[id=answer]")
# ans.send_keys(y)
# time.sleep(50)
str1 = "one"
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

