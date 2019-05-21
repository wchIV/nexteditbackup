from datetime import datetime
import subprocess

#A simple Python script that can run 7zip's command line version and have it automatically zip up all of the NextEdit files
#in a folder.  It then creates a zipfile containing all those files with the date in the same folder.
#It has no error handling so we need to be careful with it, but 7zip seems to have some built in functionality to prevent
#it from error or otherwise overwriting a zipfile built in.
# - William Howland

#Retrieves today's date using the datetime function.
todaysDate = datetime.now()

#Creates the filename based on today's date and then prints out text saying what the file will be called.
nextEditZip = ("nexteditbackup"+str(todaysDate.month)+"-"+str(todaysDate.day)+"-"+str(todaysDate.year)+".zip")
print ("The file name will be: ")
print (nextEditZip)
#//filename = input("What should the filename be? ") + ".zip";
#print(filename)

# Runs the 7zA executable which needs to be in the same directory as this file to work.
arguments = ('7za a ' + nextEditZip + ' *.nwd')
p = subprocess.Popen(arguments, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#This commented code will produce the output from 7zip if it is necessary to verify the program is working.
#for line in p.stdout.readlines():
#    print (line)

input("Press enter to exit the program..")
