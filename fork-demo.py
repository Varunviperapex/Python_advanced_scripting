#!usr/bin/env python

import os

def child_process():
    print"I am the child process : %d" %os.getpid()

    print"The child is exiting"

def parent_process():

    print"I am in the parent process with PID :%d" %os.getpid()

    childpid = os.fork()

    if childpid == 0 :
        #we are inside the child"
        child_process()
    else :
        #we are inside the parent process
        print"We are inside the parent process"
        print"our child has the PID : %d"%childpid
    while True :
        pass

parent_process()
#note that the parent and child are exactly the same to the binary level
