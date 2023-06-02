import sys
import pyperclip


def copy_path_to_clipboard(file_path):
    pyperclip.copy(file_path)


if __name__ == "__main__":
    copy_path_to_clipboard(sys.argv[1])
