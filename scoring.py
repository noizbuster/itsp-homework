# -*- coding: utf-8 -*-
import sys
import os
import commands
num = "1"
input_file = ""
# input_file = "input.txt"
log_file = "log.txt"


def main(argv):
    alist = os.listdir(os.path.curdir)
    slist = []
    alist.sort()
    print alist

    for item in alist:
        if ".c" in item[-2:]:
            slist.append(item)
    print slist

    slist.sort()
    for item in slist:
        print item[0:-2]
        buildlog = commands.getoutput("gcc " + item + " -o " + item[0:-2]+"o")
        outputname = num + "output_" + item[0:-2] + ".txt"
        buildlogname = num + "buildlog_" + item[0:-2] + ".txt"
        output = commands.getoutput("./" + item[0:-2] + "o " + input_file)
        outputfile = open(outputname, "w")
        outputfile.write(output)
        outputfile.close()
        buildfile = open(buildlogname, "w")
        buildfile.write(buildlog)
        buildfile.close()
        print "finish " + item[0:-2]


if __name__ == "__main__":
    main(sys.argv[1:])
