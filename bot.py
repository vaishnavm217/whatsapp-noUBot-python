from selenium import webdriver,common
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="D:/chromedriver.exe", )
contact = "Contact Name"
text = "Selenium Test 1"
driver.get("https://web.whatsapp.com")
actions = ActionChains(driver)
print("Scan QR Code, And then Enter")
input()
print("Logged In")
time.sleep(2)

def NoUBot(driver,contact,actions):
    input_box = driver.find_elements_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')[0]
    input_box.click()
    input_box.send_keys(Keys.BACK_SPACE*100)
    input_box.send_keys(contact+Keys.ENTER)
    time.sleep(3)
    message_input_box = driver.find_elements_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')[-1]
    message_input_box.click()
    time.sleep(2)
    while True:
        try:
            message_tile = driver.find_elements_by_xpath(f'//div[contains(@class,"focusable-list-item")]')
            css_value = message_tile[-1].value_of_css_property('align-items')
            if css_value == 'flex-start' and "nou" in message_tile[-1].text.replace(" ","").lower() :
                actions.double_click(message_tile[-1]).perform()
                time.sleep(0.25)
                message_input_box.send_keys("NO U"+Keys.ENTER)
        except common.exceptions.StaleElementReferenceException as E:
            actions = ActionChains(driver)
            message_input_box = driver.find_elements_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')[-1]
            print("Error, should get rectified automatically")
            time.sleep(3)
            continue
    

def profile_click(driver):
    element = driver.find_element_by_xpath('//img[@class="Qgzj8 gqwaM _3FXB1"]')
    element.click()
    time.sleep(2)

def about_click(driver):
    # element = driver.find_element_by_xpath("//div[@class='_1CRb5 _34vig _2phEY' and contains(text(),'About')]")
    pencil = driver.find_elements_by_xpath('//span[@data-icon="pencil"]')
    print(pencil)
    pencil[1].click()

def about_edit(driver,status):
    about_click(driver)
    input_box = driver.find_elements_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')[1]
    input_box.send_keys(Keys.BACK_SPACE*100)
    time.sleep(2)
    input_box.send_keys(status + Keys.ENTER)

def editAbout(status,driver):
    profile_click(driver)
    about_edit(driver,status)

NoUBot(driver,contact,actions)
