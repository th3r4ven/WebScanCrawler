#!/usr/bin/env python

#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

import argparse as arg
import sd_crawler as info
import downloader as down
import file_crawler as fcr
import re

print("[+]\tWeb crawler created by th3r4ven\n")


def get_arguments():
    opt = arg.ArgumentParser()
    opt.add_argument("-u", "--url", dest="url", help="Web site/page URL that is going to be downloaded/scanned.")
    opt.add_argument("-s", "--scanner", action="store_true", help="Will scan for sub-domains on specified URL.")
    opt.add_argument("-f", "--fileScanner", action="store_true", help="Will scan for files and directories on "
                                                                      "specified URL.")
    opt.add_argument("-d", "--download", action="store_true", help="Web page that is going to be downloaded.")
    options = opt.parse_args()

    if options.url == None:
        opt.error("[-]\tPlease, specify an valid url using http:// or https://, use --help for more info\n")
        exit()
    elif re.match(r"http://", options.url) or re.match(r"https://", options.url):
        if options.scanner or options.download or options.fileScanner:
            return options
        else:
            print("[-]\tPlease specify what module you want to run, scanner, download or both\n")
            opt.print_help()
            exit()
    else:
        print("[-]\tYour URL is incorrect, try using http:// or https://\n")
        opt.print_help()
        exit()


options = get_arguments()

if options.scanner:
    info.crawler(options.url)

if options.download:
    down.validrequest(options.url)

if options.fileScanner:
    fcr.file_scanner(options.url)
