# Author : HACKE-RC commonly known as RC
# Description : WebDork by RC - A python tool some google dorking stuff to find information disclosures.
# Developer contact: @coder_rc on twitter. You can request new feature by tagging me on any of your tweet.

import webbrowser
from sys import exit
import argparse
import time
from urllib.parse import unquote
from googlesearch import search

dorkscontainer = []


class Scanner:
    @staticmethod
    def banner():
        print(r"""
\ \      / /__| |__ |  _ \  ___  _ __| | __
 \ \ /\ / / _ \ '_ \| | | |/ _ \| '__| |/ /
  \ V  V /  __/ |_) | |_| | (_) | |  |   < 
   \_/\_/ \___|_.__/|____/ \___/|_|  |_|\_\
                                           
        """)
        print("\t\t\t\t\tv1.0")
        print("------------ WebDork by RC ------------")
        print("----- github.com/HACKE-RC/WebDork -----")

    @staticmethod
    def createdork(prefix, site, args):
        fulldork = prefix + site + f'%20\"{args.company_name}\"'
        dorkscontainer.append(fulldork)
        if args.verbose:
            print(f"[v] Added the dork {unquote(fulldork)} to dorks list. [v]")

    @staticmethod
    def browseropen(args, dork):
        dork = f"https://www.google.com/search?q={dork}"
        if args.verbose:
            print(unquote(f"[v] Opening the dork {dork} results in browser. [v]"))
        webbrowser.open(dork)
        time.sleep(3)
        return


parser = argparse.ArgumentParser(description='A python tool to automatically dork on a given company\'s name.')
parser.add_argument('-cn', "--company-name", type=str,
                    metavar="Company name", help='Name of the company',
                    required=True)
parser.add_argument("-bw", '--browser', help="Search the dorks in browser.", action="store_true")
parser.add_argument("--show", help="Print results from the dorks.", action="store_true")
parser.add_argument("-o", metavar="Output", type=str, help="Output filename(default is dorkresults.txt).",
                    default="dorkresults.txt")
parser.add_argument("-v", "--verbose", help="Turn verbose mode on.", action="store_true")
parser.add_argument("-s", "--silent", help="Just save the results without printing anything.", action="store_true")
parser.add_argument("--no-save-output", help="Don\'t save the output in file.", action="store_true")
args = parser.parse_args()

if args.verbose and args.silent:
    print("[ ERR ] Verbose and Silent mode can\'t be turned on at same time. [ ERR ]\nTry:\n\tRemoving the -v "
          "/--verbose or -s/--silent switch.")
    exit(2)

prefix = "site%3A"

domains = ["codepad.co", "scribd.com", "npmjs.com", "npm.runkit.com", "libraries.io", "ycombinator.com", "coggle.it",
           "papaly.com", "trello.com", "prezi.com", "jsdelivr.net", "codepen.io", "codeshare.io", "sharecode.io",
           "pastebin.com", "repl.it", "productforums.google.com", "gitter.im", "bitbucket.org", "*.atlassian.net"]

dork1 = "inurl:gitlab"

if not args.silent:
    Scanner.banner()

if args.verbose:
    print("[v] Creating dorks... [v]")

for domain in domains:
    Scanner.createdork(prefix, domain, args)

output_file = open(args.o, "a")

for dork in dorkscontainer:
    if args.browser:
        Scanner.browseropen(args, dork)
    if args.show:
        if not args.verbose:
            pass
        else:
            if not args.silent:
                print(f"Getting the results from dork -> {unquote(dork)}")

    for j in search(unquote(dork), tld="co.in", num=10, stop=10, pause=2):
        if not args.silent:
            print(j)
        if not args.no_save_output:
            output_file.write(j+"\n")

output_file.close()
