from seleniumbase import Driver
from seleniumbase.config import settings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = Driver(uc=True)

#driver.get("https://chat.openai.com/")

class bot:
    def __init__(self, options):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        
    def getLink(link):
        driver.get(link)
        
    def find_element(by, value):
        return driver.find_element(by, value)
    
    def find_elements(by, value):
        return driver.find_elements(by, value)
    
    def printText(texts):
        for text in texts:
            if (text.text != 'Sign up or log in' or text.text != 'Save your chat history, share chats, and personalize your experience.'):
                print(text.text)
                
    def printList(listitems):
        count = 0
        for listitem in listitems:
            count += 1
            if count == 10:
                count = 1
            print(count, ": ", listitem.text)
        
    
    
""""

# Find the input box where you can type your text
input_box = driver.find_element('xpath',"//textarea[@id='prompt-textarea']")

# Type your message into the input box
input_box.send_keys("Generate a list of trending topics")

click_button = driver.find_element('xpath',"//button[@data-testid='send-button']")
click_button.click()

driver.sleep(60)

input_box = driver.find_element('xpath',"//textarea[@id='prompt-textarea']")
input_box.send_keys("For each of these topics, generate a script of top 10 facts about it.")

click_button = driver.find_element('xpath',"//button[@data-testid='send-button']")
click_button.click()


#Can't figure out how to keep browser open indefinitely so this will do for now
driver.sleep(120)

texts = driver.find_elements('xpath',"//p")
listitems = driver.find_elements('xpath',"//li")

for text in texts:
    if (text.text != 'Sign up or log in' or text.text != 'Save your chat history, share chats, and personalize your experience.'):
        print(text.text)
    
count = 0

for listitem in listitems:
    count += 1
    if count == 10:
        count = 1
    print(count, ": ", listitem.text)

"""

driver.get("https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/%3Fhl%3Den-US&ec=GAZAmgQ")
input_box  = driver.find_element('xpath',"//input[@type='email']")
input_box.send_keys("ryan.mendozza@gmail.com")

click_button = driver.find_element('xpath',"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
click_button.click()

driver.sleep(5)

input_box = driver.find_element('xpath',"//input[@name='Passwd']")
input_box.send_keys("ryan#2003")

driver.sleep(5)
click_button = driver.find_element('xpath',"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
click_button.click()

driver.sleep(5)
click_button = driver.find_element('xpath',"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
click_button.click()

driver.sleep(3600)