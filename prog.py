from seleniumbase import Driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = Driver(uc=True)

driver.get("https://chat.openai.com/")

# Find the input box where you can type your text
input_box = driver.find_element('xpath',"//textarea[@id='prompt-textarea']")

# Type your message into the input box
input_box.send_keys("Generate a list of trending topics")

click_button = driver.find_element('xpath',"//button[@data-testid='send-button']")
click_button.click()

driver.sleep(20)

input_box = driver.find_element('xpath',"//textarea[@id='prompt-textarea']")
input_box.send_keys("For each of these topics, generate a script of top 10 facts about it.")

click_button = driver.find_element('xpath',"//button[@data-testid='send-button']")
click_button.click()

# Send the message (press Enter)
#input_box.send_keys(Keys.ENTER)

driver.sleep(60)
