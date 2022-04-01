from ast import arg
import os
import argparse
import re

def check(file,reg):
    if(os.path.isdir(file)==True):
        if(os.listdir(file)):
            #checking if file is a folder
            entry =os.listdir(file)
            #creating list in which all files and folder
            for entries in entry:
                #recursive function to check directories
                check(file+'/'+entries,reg)
    else:
        f=open(file,'r').read()
        res=reg.search(f)
        if(res):
            print(res)
            print(file)
#Code Starting Here
if __name__=="__main__":
    par=argparse.ArgumentParser()
    par.add_argument('file')
    #file or directory path
    par.add_argument('re')
    #regex rule
    args=par.parse_args()
    reg=args.re
    file=args.file
    #accepting cmd arguments
    r=open(reg,'r')
    for lines in r:
        rege=re.compile(lines)
        print(rege)
        check(file,rege)