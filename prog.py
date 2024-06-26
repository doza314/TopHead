from seleniumbase import Driver
from seleniumbase.config import settings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = Driver(uc=True)



driver.get("https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAmgQ")

driver.sleep(3)

input_box1 = driver.find_element('xpath',"//input[@id='identifierId']")
input_box1.send_keys("wmoshe4185@gmail.com")

google_nextbutton= driver.find_element('xpath',"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
google_nextbutton.click()

driver.sleep(10)

input_box2 = driver.find_element('xpath',"//input[@name='Passwd']")
input_box2.send_keys("Angmax02")

driver.sleep(3)

google_nextbutton1 = driver.find_element('xpath',"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
google_nextbutton1.click()

driver.sleep(20)

driver.get("https://chat.openai.com/")

gpt_nextbutton = driver.find_element('xpath',"//button[@class='btn relative btn-secondary']")
gpt_nextbutton.click()

driver.sleep(3)

gpt_nextbutton1 = driver.find_element('xpath',"//button[@class='social-btn']")
gpt_nextbutton1.click()


# Find the input box where you can type your text
input_box = driver.find_element('xpath',"//textarea[@id='prompt-textarea']")

# Type your message into the input box
input_box.send_keys("Generate a list of 4 trending topics")

click_button = driver.find_element('xpath',"//button[@data-testid='send-button']")
click_button.click()

driver.sleep(60)

input_box = driver.find_element('xpath',"//textarea[@id='prompt-textarea']")
input_box.send_keys("For each of these topics, generate a script of top 5 facts about it.")

click_button = driver.find_element('xpath',"//button[@data-testid='send-button']")
click_button.click()


#Can't figure out how to keep browser open indefinitely so this will do for now
driver.sleep(60)

texts = driver.find_elements('xpath',"//p")
listitems = driver.find_elements('xpath',"//li")

for text in texts:
    print(text.text)
    
for listitem in listitems:
    print(listitem.text)