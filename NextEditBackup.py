from datetime import datetime
import subprocess
#import os.path
import os
#from shutil import make_archive
#import zipfile

#v1
#A simple Python script that can run 7zip's command line version and have it automatically zip up all of the NextEdit files
#in a folder.  It then creates a zipfile containing all those files with the date in the same folder.
#It has no error handling so we need to be careful with it, but 7zip seems to have some built in functionality to prevent
#it from error or otherwise overwriting a zipfile built in.
# - William Howland

#v2 7/2/2019
#New version now checks to see if the file exists already.  If it does, it checks to see if a version with a -2 after the name
#exists.  If it does, the program gives up and exits.  
#Future versions might attempt to remove the dependence on 7zip, but current attempts to add this functionality were unsuccesful.
# - William Howland


#Retrieves today's date using the datetime function.
todaysDate = datetime.now()
failed = 0;

#Creates the filename based on today's date and then prints out text saying what the file will be called.
nextEditZip = ("nexteditbackup"+str(todaysDate.month)+"-"+str(todaysDate.day)+"-"+str(todaysDate.year)+".zip")

#archive_name = os.path.join(os.getcwd(),str(nextEditZip))
#root_dir = os.path.join(os.getcwd())
checker = os.path.isfile(str(nextEditZip))
if checker == 1 :
    nextEditZip = ("2nexteditbackup"+str(todaysDate.month)+"-"+str(todaysDate.day)+"-"+str(todaysDate.year)+".zip")
    checker2 = os.path.isfile(str(nextEditZip))
    if checker2 == 1 :
        failed = 1;
    else:
        failed = 0;
        
#the checker variable is a remnant of the attempt to remove the need for 7zip, but it's still used to see if a file named
#the same as our created zipfile exists in this version of the program.
#print("Checker shows " + str(checker))

if failed == 0:
    print ("The file name will be: ")
    print (nextEditZip)
    #//filename = input("What should the filename be? ") + ".zip";

    # Runs the 7zA executable which needs to be in the same directory as this file to work.
    arguments = ('7za a ' + nextEditZip + ' *.nwd')
    p = subprocess.Popen(arguments, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #This commented code will produce the output from 7zip if it is necessary to verify the program is working.
    #for line in p.stdout.readlines():
    #    print (line)
    input("Press enter to exit the program..")
else:
    print ("The program attempted to make a file named " + str(nextEditZip) + " but failed due to the existence of another file with the same name.")
    input ("Press enter to exit the program..")
