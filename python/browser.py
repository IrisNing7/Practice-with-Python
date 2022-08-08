
# selenium browser for Google Chrome
# step1: install certifi package via terminal 
# Enter ' pip install certifi '
# OR Enter 'cd /Applications/Python\ 3.10/     '3.10' - python's version
#           ./Install\ Certificates'

# step2: install chromedriver
#        pip install chromedriver-binary




from selenium import webdriver
import chromedriver_binary
driver = webdriver.Chrome()
driver.get('https://automatetheboringstuff.com/')
elem = driver.find_element('css selector', 'body > div > main > div > ul:nth-child(19) > li:nth-child(1) > a')
elem
elem.click()

elems = driver.find_elements('css selector', 'p')
len(elems)

driver.back()
driver.forward()
driver.refresh()
driver.quit()


driver.get('https://automatetheboringstuff.com/')
elem = driver.find_element('css selector', 'body > div > main > div > p:nth-child(6)')
elem.text

elem = driver.find_element('css selector', 'html')
elem.text
