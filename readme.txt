NEXTEDIT BACKUP PYTHON SCRIPT - by Billy Howland -

This is a simple Python script that runs commands line 7zip to compress all *.nwd files and automatically generates the name of the file based on today's date.

Installation and running instructions:
1. Download Windows command line 7zip from 7zip's website.  Extract the 7za.exe file into the same directory as the compiled Python script
2. If you haven't already, compile the Python script into an executable.  Pyinstaller works best for this.
3. Run the compiled executable and it will run 7zip, assuming it is in the same directory and called 7za.exe, zip up all *.nwd files and create a zip file
called "nexteditbackup(today's date).zip"

