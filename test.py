# import json


# # Read the JSON file
# with open('test.json', 'r') as file:
#     data = json.load(file)

# # Access the backup codes
# backup_codes = data['backup_codes']

# # Use one backup code and remove it from the list
# used_code = backup_codes.pop(0)

# # Update the JSON file with the modified list of backup codes
# with open('test.json', 'w') as file:
#     json.dump(data, file, indent=4)

# # Print the used backup code
# print("Used Backup Code:", used_code)

with open('page_source.txt', 'r', encoding='utf-8') as file:
    page_source = file.read()

# Search for a substring within the page source
substring = 'Profile'
index = page_source.find(substring)

if index != -1:
    # Extract the HTML element containing the substring
    start_index = page_source.rfind('<', 0, index)  # Find the start index of the element
    end_index = page_source.find('>', index) + 1  # Find the end index of the element
    html_element = page_source[start_index:end_index]
    
    print("HTML element containing the substring:")
    print(html_element)
else:
    print("Substring not found in the page source.")