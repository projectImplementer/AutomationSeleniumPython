from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

testing_website = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

firefox_browser = webdriver.Firefox(executable_path='C:/QASeleniumDrivers/geckodriver.exe')

firefox_browser.maximize_window()

firefox_browser.get(testing_website)

assert 'Selenium Easy Demo' in firefox_browser.title
show_message_button = firefox_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in firefox_browser.page_source

user_message = firefox_browser.find_element_by_id('user-message')

try:
    WebDriverWait(firefox_browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="at-cv-lightbox-close"]'))).click()
finally:
    print('Element was found')

user_message.clear()
user_message.send_keys('I AM EXTRA COOL')

show_message_button.click()

output_message = firefox_browser.find_element_by_id('display')

assert 'I AM EXTRA COOL' in output_message.text

firefox_browser.quit()

