import os
import json
import time
import random
from tkinter import Tk, Label, Entry, Button, StringVar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def random_file_path(directory):
    """
    Returns a random file path from the specified directory.
    """
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        raise ValueError("No files found in the specified directory.")
    return os.path.join(directory, random.choice(files))


def init_driver():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    ]
    random_user_agent = random.choice(user_agents)
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={random_user_agent}")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    return webdriver.Chrome(options=chrome_options)


def login_to_discord(driver, email, password, wait):
    driver.get('https://discord.com/login')
    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
    email_input.send_keys(email) 
    password_input.send_keys(password) 
    password_input.send_keys(Keys.RETURN)  


def get_auth_code_gui():
    def on_submit():
        auth_code_var.set(auth_code_entry.get())
        root.destroy()

    root = Tk()
    root.title("Enter Auth Code")
    Label(root, text="Enter your auth code:").pack(pady=10)
    auth_code_var = StringVar()
    auth_code_entry = Entry(root, textvariable=auth_code_var, width=25)
    auth_code_entry.pack(pady=5)
    auth_code_entry.bind('<Return>', lambda event=None: on_submit())  # Bind Enter key to on_submit
    Button(root, text="Submit", command=on_submit).pack(pady=10)
    root.mainloop()
    return auth_code_var.get()


def submit_auth_code(driver, auth_code, wait):
    backup_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="6-digit authentication code/8-digit backup code"]')))
    backup_input.send_keys(auth_code)
    backup_input.send_keys(Keys.RETURN)


def change_avatar(driver, directory_path, wait):
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
    time.sleep(1)

    print("Selecting image...")
    # Select active element as file input and upload file
    file_input = driver.find_element(By.CLASS_NAME, "file-input")
    file_path = "C:/Users/chase/Desktop/KIRBY/kirby_w_sward2.jpg"

    directory_path = "C:/Users/chase/Desktop/KIRBY"
    file_path = random_file_path(directory_path)

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


def main():
    #Define main credentials/paths
    with open('credentials.json', 'r') as file:
        account_credentials = json.load(file)

    #Init chrome driver and elements
    driver = init_driver()
    wait = WebDriverWait(driver, 10)

    #Preform actions
    login_to_discord(driver, account_credentials['email'], account_credentials['password'], wait)
    auth_code = get_auth_code_gui()
    submit_auth_code(driver, auth_code, wait)
    change_avatar(driver, account_credentials['directory_path'], wait)
    driver.quit()

if __name__ == '__main__':
    main()
