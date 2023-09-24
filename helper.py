import os
import random
import json

#2FA Code Use
def use_backup_code():
    # Read the JSON file
    with open('2FA_codes.json', 'r') as file:
        data = json.load(file)

    backup_codes = data['backup_codes']
    #used_code = backup_codes.pop(0)

    with open('2FA_codes.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    backup_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="6-digit authentication code/8-digit backup code"]')))
    backup_input.send_keys('TEST-1234')
    backup_input.send_keys(Keys.RETURN)  
use_backup_code()


def random_file_path(directory):
    """
    Returns a random file path from the specified directory.
    
    Parameters:
    - directory (str): The path to the directory.
    
    Returns:
    - str: The full path to a randomly selected file.
    """
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        raise ValueError("No files found in the specified directory.")
    
    return os.path.join(directory, random.choice(files))
