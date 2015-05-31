# -*- coding: utf-8 -*-
import sys
import os
import shutil

def main(argv):
    #default working directory is pwd
    pwd = os.path.curdir
    out = pwd
    #check output directory
    if(len(argv) != 2):
        print "running with wrong arguments"
        print "usagea : "
        print "pythone renamer.py targetDirectory outputDirectory"
        print "default targetDirectory : pwd"
        print "default outputDirectory : pwd"

    #check start directory
    if(len(argv) == 0):
        print "not input root directory, process on pwd :" ,pwd
    else:
        if os.path.isdir(argv[0]) :
            print "start with path :",argv[0]
            pwd = argv[0]
        else:
            print argv[0],"is not a directory path, running with pwd"


    if(len(argv) >= 2) and os.path.isdir(argv[1]):
        out = argv[1]

    #get subpath
    studentsId = os.listdir(pwd)
    
    #get student's files
    for id in studentsId:
        if ".py" not in id:
            print id
            studentfile = os.listdir(pwd+"/"+id)
            print "\t", studentfile
            for filename in studentfile:
                if ".c" in filename:
                    src = os.path.join(pwd, id, filename)
                    des = os.path.join(out,(id+"_"+filename))
                    print "copy ", src,"to", des
                    shutil.copy2(src, des)
if __name__ == "__main__":
    main(sys.argv[1:])
