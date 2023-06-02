# WSL-Friendly File Path Copier

This set of Python scripts for Windows gives you a few time-saving options for copying file paths when you right-click on a file or folder. You'll find them especially useful if you use WSL often.

This will give you the ability to quickly copy the file path of:

- A file or folder, in either Windows or Unix format
- The folder that contains the file/folder you're right-clicking on, in either Windows or Unix format

## A few reasons why I made this

1. When using WSL, I got tired of needing to manually edit the file paths I copied from Windows to the Ubuntu terminal. It struck me as something that shouldn't have to be manual.
2. Eagle.cool has spoiled me by providing an easy "Copy File Path" option when I right-click on an asset. I've used it so often that I began to miss it when working with files on my desktop.
3. I often speed up my workflow by copypasting file paths directly into the address bars of explorer windows and "Import File" dialogues, etc. But in many programs, pasting the exact file path in the address bar results in the file opening in its default program instead of getting imported into the one you're using. So I decided to take it further by adding the ability to copy the file path of the _folder that contains_ the item you're right-clicking on. (And of course, in your terminal, this can also help shave a few seconds off of cd'ing to the location of a file you have in front of you in an explorer window.)

## Installation

This is worded for someone at the experience level I was when I first started using WSL: "enthusiastic but bewildered beginner." 😁 If any part of this is confusing, feel free to open an issue and ask for it to be clearer. I'm here for that.

As a heads up, you'll need administrator access to your computer in order to use this, as it interacts with your Windows Registry. In simpler terms: if this computer belongs to you, you're almost definitely fine, but you might not be able to add this to your work computer yourself.

1. Make sure Python 3.7 or higher is installed on your computer. (If you're not sure, open your Command Prompt and type `python -v`. If it doesn't respond with a version number, go download and install it. If you do so, make sure to look out for the "add to your PATH" checkbox at the end of installation and make sure it's checkmarked.)

2. Install the `pyperclip` library: Open your Command Prompt and run the command `pip install pyperclip`.
   a) If you run into issues here, [this page](https://www.alphr.com/install-pip-windows/) is a great walkthrough for troubleshooting, and the steps should work for Windows 10 or 11.
   b) If anyone is curious why I used pyperclip instead of win32clipboard, pyperclip is cross-platform and the code is tidier.

3. Download this repository by clicking on that green "Code" button at the top of this page. If you download the .zip file, unzip it. It doesn't have to go in any specific folder, but it's best to put it where you want it to stay.`*`

4. Open "YourPythonPath.txt" with any text editor. This is where you'll paste the path to your Python executable. The easiest way to find this is with your command prompt - use the command `where python`. You'll get something like this:
   `C:\Users\smith\AppData\Local\Programs\Python\Python311\python.exe` (You're not done yet)
   Copypaste that into YourPythonPath.txt WITHOUT the "python.exe". Like so:
   `C:\Users\smith\AppData\Local\Programs\Python\Python311\` (👈👈👈 This version is correct)
   Note: It shouldn't be the file path of where you installed Python; this is different.

5. Okay, it's time to run the `RunMe.py` script!
   1. Open a new Command Prompt as Administrator. (If you start typing "command prompt" in your Start Menu, you should see the "Run as Administrator" option appear below it.) You can close the old Command Prompt, but you don't have to.
   2. Open up your FlexibleFilePathCopier folder (the one with RunMe.py inside).
   3. Click into the address bar (where the file path is). Copy that file path.
   4. Go back into your Command Prompt. Type `cd` and then paste the file path. You should see something like this - run it:
      `cd C:\Users\smith\Documents\FlexibleFilePathCopier`
   5. Now you're in the folder with the file you need to run. Run this command:
      `python RunMe.py`
   6. If it gives you success messages instead of error messages, you did it!

## Usage

Time to test it out! Right-click on any file or folder, and you should see the following new options in your context menu:

- Copy Path
- Copy Path of Containing Folder
- Copy Unix Path
- Copy Unix Path of Containing Folder

Select the option you need, and the path will be copied to your clipboard, ready to paste wherever you need it.

## Removal

If you no longer want these options in your context menu, just run the `Remove.py` script. This will remove the options and clean up the changes made to your registry.

## `*`Important note about where your files live:

Your Windows Registry will look for the file paths of the scripts that make this chooch. If you want to move the files around, make sure you run `Remove.py` first, then run `RunMe.py` again when they're at their new destination.

---

I hope this script is useful to you and saves you time! Please feel free to give me feedback or suggestions. And if you're happy enough to feel like buying me a beer via [my Ko-Fi page](https://ko-fi.com/gvguide), I'd appreciate it very much. -- Evie 🙂
