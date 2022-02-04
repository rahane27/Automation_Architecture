import glob, os
import subprocess as sp
import time
import schedule
import time
import logging
from datetime import datetime

import shutil
import os
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

def scheduled_job():
    print("1st function")
    
    def job():
        print("I'm working...")
        logging.basicConfig(filename='process.log',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.DEBUG)


        value=["entrycheck"]

        os.chdir("//192.168.10.130//ocap")


        programName = "notepad.exe"
        programNamExcl = "C:/Program Files (x86)/Microsoft Office/Office14/1036/EXCEL.EXE"
        fileExcl = "C:/Users/cognos1.ESSELPROPACK/Desktop/oclf.xlsx"

        time.sleep(5)
        logging.debug("Reading one by one .txt file")
    
        for file in glob.glob("*.txt"):
            print(file)
            fileee=file[:-4]
            print(fileee)
   
            fileName=file
        
        
            dest="//192.168.10.130//ocap//backup//"+file
        
            print(fileName)
            logging.debug(" File  name is {file}, and path is {fileName}".format(file = file, fileName = fileName))

            os.startfile("C:/Users/cognos1.ESSELPROPACK/Desktop/oclf.xlsx")
            logging.debug("Reading Excel")

        
            sp.Popen([programName, fileName])
            cmd = "runsikulix.cmd -r E:\ShareData\entrycheck"
        
            os.chdir("E:\ShareData")
            logging.debug("Running Script for {customer}".format(customer=file))
            #os.system("runsikulix.cmd -r tettwe --args " +fileee) #apend log of sikuli into our process.log
            os.system("runsikulix.cmd -r entrycheckcopy --args " +fileee) #apend log of sikuli into our process.log

        
        #sp.call(cmd, shell=True)
        #os.chdir("D:/mydir")
            os.chdir("//192.168.10.130//ocap")

        
            time.sleep(10)
            os.system("TASKKILL /F /IM notepad.exe")
        
            time.sleep(4)
            os.system("TASKKILL /F /IM EXCEL.exe") #Popen("taskkill /F /IM EXCEL.EXE",shell=True)
            time.sleep(4)
            logging.debug("closing .txt file andd excel")
        
        #Popen("taskkill /F /IM EXCEL.EXE",shell=True)

            if os.path.exists(fileName):
            #os.remove(fileName)
                shutil.move(fileName,dest)
        
            
       
        
            time.sleep(10)
            job()

            logging.debug("Calling Next File")
    job()


sched.add_job(scheduled_job ,'interval',minutes=20)

sched.start()

