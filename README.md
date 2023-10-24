# Discord Profile Picture (PFP) Swap
This script is designed to automate the process of changing the user's avatar on Discord.
It utilizes the Selenium framework to navigate and interact with the web interface of Discord, and features a graphical user interface to accept two-factor authentication codes.

## Features
- Opens a headless browser instance to navigate through Discord's web interface.
- Automatically logs into Discord with the provided email and password.
- Shows a GUI to input the two-factor authentication code.
- Changes the avatar to a random image from a specified directory.

## Getting Started
### Prerequisites
Python 3.x
Selenium library for Python.
Google Chrome Browser.
ChromeDriver (compatible version with the installed Chrome Browser).

### Installation
1. Install Selenium: ```pip install selenium```
2. Download and install [ChromeDriver](https://sites.google.com/chromium.org/driver/) that's compatible with your version of Chrome.
3. Clone this repo

### Usage
1. Create a _credentials.json_ file in the scripts directory. **Do not store passwords on publicly accessible devices**
```
{
    "email": "YOUR_DISCORD_EMAIL",
    "password": "YOUR_DISCORD_PASSWORD",
    "directory_path": "PATH_TO_DIRECTORY_WITH_IMAGES"
}
```
2. Run the script to test it out. For daily use, set up a batch file and configure it with Windows Task Scheduler.
3. A GUI will appear prompting you to enter your Discord two-factor authentication code. Enter the code and press 'Submit'.
4. The script will change your Discord avatar to a random image from the directory specified in credentials.json.

### Notes
- Ensure that the directory_path in credentials.json is valid and contains images. The script will fail if there are no images in the directory.
- If you are not using two-factor authentication on your Discord account, you will need to remove or modify the parts of the script that handle the authentication code input.
- This script uses CSS selectors and XPaths which are subject to changes on the Discord platform. If Discord updates its web UI, this script may need updates to work correctly.

### Disclaimer
Automating interactions with web services, like Discord, can be against their terms of service. 
Use this script responsibly and understand the risks. Always review and ensure that you're not violating any terms of service or usage agreements.

## License
Discord Profile Picture Swap is released under the [MIT License](https://opensource.org/license/mit/).
