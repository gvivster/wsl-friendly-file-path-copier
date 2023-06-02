import os
import sys
import pyperclip


def copy_path_to_clipboard(file_path):
    containing_folder = os.path.dirname(file_path)
    pyperclip.copy(containing_folder)


if __name__ == "__main__":
    copy_path_to_clipboard(sys.argv[1])
