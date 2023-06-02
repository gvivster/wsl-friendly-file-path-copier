import winreg

# List of script names
scripts = [
    ('Copy Path'),
    ('Copy Path of Containing Folder'),
    ('Copy Unix Path'),
    ('Copy Unix Path of Containing Folder'),
]

# Base key paths
base_key_paths = [r'Software\Classes\*\shell',
                  r'Software\Classes\Directory\shell']

# Loop through each key path
for base_key_path in base_key_paths:
    # Loop through each script and delete the registry key
    for script_name in scripts:
        key_path = base_key_path + '\\' + script_name
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path + '\\command')
            winreg.DeleteKeyEx(winreg.HKEY_CURRENT_USER, key_path)
            print(f'Successfully deleted {key_path}')
        except FileNotFoundError:
            print(f'The key {key_path} does not exist.')
        except PermissionError:
            print(f'Permission denied when deleting the key {key_path}.')
        except Exception as e:
            print(
                f'An unexpected error occurred while deleting {key_path}: {e}')
