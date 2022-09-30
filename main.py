from datetime import datetime as dt
import time

blocklink = [
    #girlfriends profile link goes here " "
    " "
]
hostfi = r"C:\Windows\System32\drivers\etc\hosts" #default hostfile location

def block_her(start, end):
    while True:
        if (dt(dt.now().year, dt.now().month, dt.now().day, start)
            < dt.now()
            < dt(dt.now().year, dt.now().month, dt.now().day, end)):
            with open(hostfi, "r+") as hostfile:
                hosts = hostfile.read()
                for link in blocklink:
                    if link not in hosts:
                        hostfile.write("127.0.0.1" + " " + link + "\n")
        else:
            with open(hostfi, "r+") as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(link in host for link in blocklink):
                        hostfile.write(host)
                hostfile.truncate()
        time.sleep(2)


if __name__ == "__main__":
    block_her(_,_) #time period to block her
