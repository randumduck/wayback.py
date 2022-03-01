#!/usr/bin/python3
#python script to get all waybackURLS of any given domainlistas a file

import os
import argparse

parser=argparse.ArgumentParser(description="Waybackurls")
parser.add_argument("-f", type=str, required=True, help="insert the <target file> after scriptname and -f")

file=parser.parse_args()
f=open("{}".format(file.f), "r")
for i in f.readlines():
    print("\n[+] Target : {}\n".format(i))
    os.system("waybackurls {}".format(i))
