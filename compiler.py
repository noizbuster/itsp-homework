# -*- coding: utf-8 -*-
import sys
import os
import shutil
import commands
import time
compileOptions = " "
#compileOptions = " -lm"

def main(argv):
    pwd = os.path.curdir
    if(len(argv) >= 1) and os.path.isdir(argv[0]):
        pwd = argv[0] 
    
    print("start with : "+pwd)
    buildlog = open("buildlog"+str(int(time.time()))+".txt", "w")
    
    hwfiles = os.listdir(pwd)
    for hwfile in hwfiles:
        if ".c" in hwfile:
            buildlog.write("start build : "+ hwfile+"\n")
            buildlog.write(
                    "gcc " + str(os.path.join(pwd,hwfile)) + 
                    " -o " + str(os.path.join(pwd,(hwfile+".out"))) +
                    compileOptions + "\n")
            line = commands.getoutput(
                    "gcc " + str(os.path.join(pwd, hwfile)) +
                    " -o " + str(os.path.join(pwd, (hwfile+".out"))) +
                    compileOptions)
            print line
            buildlog.write(line+"\n")
            buildlog.write("\n\n")

    buildlog.close();

if __name__ == "__main__":
    main(sys.argv[1:])
