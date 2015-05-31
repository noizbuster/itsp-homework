# -*- coding: utf-8 -*-
import sys
import os
import shutil
import commands
import time

def main(argv):
    pwd = os.path.curdir
    inputFileName = os.path.join(pwd, "input.txt")

    if(len(argv) >= 1) and os.path.isdir(argv[0]):
        pwd = argv[0]

    if(len(argv) >= 2) and os.path.isdir(argv[1]):
        inputFileName = argv[1]

    print("start to : "+pwd)
    executelog = open("executelog"+str(pwd)+str(int(time.time()))+".txt", "w")

    hwfiles = os.listdir(pwd)
    for hwfile in hwfiles:
        if ".out" in hwfile:
            print hwfile
            executelog.write("start execute : " + hwfile + "\n")
            ll = commands.getoutput(str(os.path.join(pwd, hwfile)) + " < " + inputFileName);
            print ll
            executelog.write(ll+"\n")
            executelog.write("\n\n")
    executelog.close();

if __name__ == "__main__":
    main(sys.argv[1:])
