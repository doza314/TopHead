from seleniumbase import Driver
from seleniumbase.config import settings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://chat.openai.com/")

"""links = driver.find_elements("xpath", "//a[@href]")

for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()"""


