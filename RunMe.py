import os
import winreg

# Read Python path from YourPythonPath.txt and add quotation marks
with open('YourPythonPath.txt', 'r') as file:
    python_path = f'"{file.read().strip()}"'

# Check if the Python path is valid
if not os.path.exists(python_path.strip('\"')):
    print("It looks like there's an issue with your Python path. See the ReadMe for help.")
    exit()

# script folder path is automatically determined
script_folder_path = os.path.dirname(os.path.realpath(__file__))

# List of script paths
scripts = [
    ('Copy Path', 'scripts\copypath_win_file.py'),
    ('Copy Path of Containing Folder', 'scripts\copypath_win_folder.py'),
    ('Copy Unix Path', 'scripts\copypath_unix_file.py'),
    ('Copy Unix Path of Containing Folder', 'scripts\copypath_unix_folder.py'),
]

# Base key paths
base_key_paths = [r'Software\Classes\*\shell',
                  r'Software\Classes\Directory\shell']

# Loop through each key path
for base_key_path in base_key_paths:
    # Loop through each script and create a registry key for it
    for script_name, script_path in scripts:
        key_path = base_key_path + '\\' + script_name + '\\command'
        command = python_path + ' "' + \
            os.path.join(script_folder_path, script_path) + '" "%1"'
        try:
            key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,
                                     key_path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, '', 0, winreg.REG_SZ, command)
            winreg.CloseKey(key)
            print(f'Successfully created {key_path}')
        except Exception as e:
            print(f'An error occurred while creating {key_path}: {e}')
