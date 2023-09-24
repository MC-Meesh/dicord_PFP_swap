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
import random
import base64
import autoit
from tkinter import Tk, Label, Entry, Button, StringVar


with open('credentials.json', 'r') as file:
    account_credentials = json.load(file)


# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
]
random_user_agent = random.choice(user_agents)

# Create Chrome options and set user agent header
chrome_options = Options()
chrome_options.add_argument(f"user-agent={random_user_agent}")
# chrome_options.add_argument("--headless")  # Run in headless mode (without a visible browser window)
driver = webdriver.Chrome(options=chrome_options)
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
        if len(auth_code) == 6:
            break
        else:
            print("Invalid auth code format. Please enter a valid code in the form '******'")

    backup_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="6-digit authentication code/8-digit backup code"]')))
    backup_input.send_keys(auth_code)
    backup_input.send_keys(Keys.RETURN)  
use_auth_code()

# Navigate to user Settings
settings_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="User Settings"]'))) 
settings_button.click()

# Wait for the app-mount div to be clickable and select
app_mount = wait.until(EC.element_to_be_clickable((By.ID, 'app-mount')))
app_mount.click()

# Get to user profile
actions = ActionChains(driver)
for _ in range(4):
    actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.click().perform()

# Navigate to avatar change
actions = ActionChains(driver)
for _ in range(8):
    actions.send_keys(Keys.TAB)
    time.sleep(.25)
    # Escape tab popup 
    if _ == 3:
        print("Escaping tab hell...")
        # okay_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button')))
        # okay_button.click()
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.click().perform()
    actions.perform()

actions.send_keys(Keys.ENTER).perform()

print("Popup loading...")
time.sleep(1) #Wait for popup to load << needs to be more robust tho ://

# actions.send_keys(Keys.TAB).perform()
# actions.click().perform()


print("Selecting image...")
# Select active element as file input and upload file
file_input = driver.find_element(By.CLASS_NAME, "file-input")
file_path = "C:/Users/chase/Desktop/KIRBY/kirby_w_sward2.jpg"
file_input.send_keys(file_path)

print("Uploading...")
time.sleep(3)

print("Accepting...")
skip = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[3]/div[3]/div/div/div[3]/button/div')
skip.click()


time.sleep(3)
print("Saving Changes...")
save = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/button[2]/div')
save.click()

driver.quit()