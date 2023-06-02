import os
import sys
import pyperclip
import re


def escape_unix_path(path):
    # Define a regular expression pattern for special characters that need to be escaped
    pattern = r"([\s!\"#$&'()*,:;<=>?\\\[\]^{|}~])"

    # Use the re.sub function to replace each occurrence of a special character with a backslash followed by that character
    escaped_path = re.sub(pattern, r'\\\1', path)

    return escaped_path


def windows_path_to_unix(path):
    drive, path = os.path.splitdrive(path)
    path = escape_unix_path(path.replace('\\', '/'))
    return '/mnt/' + drive.lower().replace(':', '') + path


def set_clipboard(text):
    pyperclip.copy(text)


if __name__ == "__main__":
    path = sys.argv[1]
    unix_path = windows_path_to_unix(path)
    set_clipboard(unix_path)
