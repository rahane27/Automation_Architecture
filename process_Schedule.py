from apscheduler.schedulers.blocking import BlockingScheduler
import schedule
import subprocess
import os
import subprocess
import sys
#os.environ['JAVA_HOME'] = "set JAVA_HOME=C:\Program Files\Java\jdk1.8.0_191"


sched = BlockingScheduler()

value=["sourcecode","SAP_Do.sikuli"]
def scheduled_job():
    
    print('schedule job is running')

    if value[0] == 'sourcecode':
        path = os.path.join(os.getcwd(), value[1])
        sikulifolder=path#.replace(".py" , "",1)
        os.system("runsikulix.cmd -r "+sikulifolder)



sched.add_job(scheduled_job,'cron',id='my_cron_job1', hour=7,minute=50)
#sched.add_job(scheduled_job,'cron',id='my_cron_job2', hour=19,minute=16)
sched.start()





