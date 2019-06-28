import psutil
import os
import signal
def GetPross(prossname='JHOIS.FrameworkProvider'):
    pidLis=[]
    pids = psutil.pids()
    for pid in pids:
        # print(pid)
        p = psutil.Process(pid)
        # print(p.name)
        if(str(p.name()).startswith(prossname)):
            pidLis.append(pid)
        elif(p.name()==prossname):
            pidLis.append(pid)    
    return pidLis

def killPross(pidLis):
    for pid in pidLis:
        os.kill(pid,signal.SIGTERM)

processNmae=input("请输入线程名")
if processNmae :
    pidLis=GetPross(processNmae)
else:
    pidLis=GetPross()
killPross(pidLis)
input("任意键继续")