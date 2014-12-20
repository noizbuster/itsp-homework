# -*- coding: utf-8 -*-
import sys
import os
num = "1"
# input_file = ""
input_file = "input.txt"
log_file = num+"log.txt"
build_file = num+"build.txt"


def main(argv):
    alist = os.listdir(os.path.curdir)
    slist = []
    blist = []

    print alist

    for item in alist:
        if (num+"output_") in item[0:8]:
            slist.append(item)
    print slist

    log = open(log_file, "w")
    slist.sort()
    for item in slist:
        itemfile = open(item)
        log.write(item+"==================\n")
        output = itemfile.read()
        log.write(output+"\n")
        log.write(item+" end==================\n\n\n")

    log.close()

    for item in alist:
        if (num+"buildlog_") in item[0:10]:
            blist.append(item)
    print blist

    blist.sort()
    build = open(build_file, "w")
    for item in blist:
        itemfile = open(item)
        build.write(item+"==================\n")
        output = itemfile.read()
        build.write(output+"\n")
        build.write(item+" end==================\n\n\n")

    build.close()


if __name__ == "__main__":
    main(sys.argv[1:])
