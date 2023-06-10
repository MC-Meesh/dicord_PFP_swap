from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

with open('credentials.json', 'r') as file:
    account_credentials = json.load(file)

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (without a visible browser window)
# driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)  # Replace with the actual path to chromedriver
driver = webdriver.Chrome()
driver.get('https://discord.com/login')

wait = WebDriverWait(driver, 10)


#Login to discord
email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
email_input.send_keys(account_credentials['email']) 
password_input.send_keys(account_credentials['password']) 
password_input.send_keys(Keys.RETURN)  

#2FA Code Use
def use_auth_code():
    while True:
        auth_code = input("Enter your auth code: ")
        if len(auth_code) == 7 and auth_code[3] == '-':
            break
        else:
            print("Invalid auth code format. Please enter a valid code in the form '***-***'")

    backup_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="6-digit authentication code/8-digit backup code"]')))
    backup_input.send_keys(auth_code)
    backup_input.send_keys(Keys.RETURN)  
use_auth_code()

#User Settings
settings_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="User Settings"]'))) 
settings_button.click()

# Wait for the app-mount div to be clickable
app_mount = wait.until(EC.element_to_be_clickable((By.ID, 'app-mount')))

# Click on the app-mount div
app_mount.click()

# Perform Tab key presses
actions = ActionChains(driver)
for _ in range(4):
    actions.send_keys(Keys.TAB)

# Press Enter after the 12 tabs
actions.send_keys(Keys.ENTER)

actions.click().perform()

# Perform tab key presses
actions = ActionChains(driver)
for _ in range(4):
    actions.send_keys(Keys.TAB)
    time.sleep(0.5)
    try:
        driver.switch_to.alert.accept()  # Dismiss the popup
    except:
        pass

actions.send_keys(Keys.ENTER)
actions.click().perform()

for _ in range(2):
    actions.send_keys(Keys.TAB)

actions.send_keys(Keys.ENTER)
actions.click().perform()

# # Locate and click the selected item
# selected_item = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='selected_item_id']"))
# )
# actions.click(selected_item)

# actions.perform()

time.sleep(5000)

driver.quit()