#!/usr/bin/python
__author__ = 'gang'

import pexpect
import time
import  os
import  sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def log(str):
    print "[changetodo]" + str

def IsFileChanged(path):
    return True


def Run(commond):
    pexpect.run(commond, logfile=sys.stdout)



class MySystemEventHandler(FileSystemEventHandler):
    def __init__(self, fun, commod):
        super(MySystemEventHandler, self).__init__()
        self.run = fun
        self.commond = commod

    def on_any_event(self, event):
        log("file has changed, begin make...")
        if not event.src_path.endswith("/"):
            print event.src_path
            self.run(self.commond)



def PareHandle(pares):
    if len(pares) == 0:
        print "the pares is too short,pleas input file and your make commond"
        exit(0)
    else:
        path = os.path.abspath(pares[1])
        commond = pares[2]
        return path,commond


def StartWatch(path, commod):
    observer = Observer()
    observer.schedule(MySystemEventHandler(Run, commod), path, recursive=True)
    observer.start()
    log("start to watch files in %s" % path)
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



def Main():
    path,commond = PareHandle(sys.argv)
    StartWatch(path, commond)

if __name__ == "__main__":
    Main()
    #while True:
    #    time.sleep(1)
   #     run()if IsFileChanged()