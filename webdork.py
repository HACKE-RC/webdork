#!/usr/bin/env python3

# Author : HACKE-RC commonly known as RC;
# Description : WebDork by RC - A python tool to automate some google dorking stuff to find information disclosures.
# Developer contact: @coder_rc on twitter. You can request new feature by tagging me on any of your tweet.
# Proxy integration is by me (ka1hatsu)

#Importing modules
from os import access
import webbrowser
from sys import exit
import argparse
import time
from urllib.parse import unquote
from random import randint
import requests
from bs4 import BeautifulSoup

dorkscontainer = []
all_links = []

class Scanner:
    @staticmethod
    def banner() -> None:
        print(r"""
\ \      / /__| |__ |  _ \  ___  _ __| | __
 \ \ /\ / / _ \ '_ \| | | |/ _ \| '__| |/ /
  \ V  V /  __/ |_) | |_| | (_) | |  |   < 
   \_/\_/ \___|_.__/|____/ \___/|_|  |_|\_\
                                           
        """)
        print("\t\t\t\t\tv1.0")
        print("------------ WebDork by RC ------------")
        print("----- github.com/HACKE-RC/webdork -----")

    @staticmethod
    def createdork(prefix : str, site : str, args : argparse.Namespace) -> None:
        fulldork = prefix + site + f'%20\"{args.company_name}\"'
        dorkscontainer.append(fulldork)
        if args.verbose:
            print(f"[v] Added the dork {unquote(fulldork)} to dorks list. [v]")
            del fulldork
        return

    @staticmethod
    def browseropen(args : argparse.Namespace, dork : str) -> None:
        dork = f"https://www.google.com/search?q={dork}"
        if args.verbose:
            print(f"[v] Opening the dork {dork} results in browser. [v]")
        webbrowser.open(dork)
        time.sleep(4)
        return

    @staticmethod
    def getuseragent() -> int:
        """
        Returns a random useragent
        """
        all_agents = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       "https://developers.whatismybrowser.com/useragents/parse/16254-googlebot")
        return all_agents[randint(0, len(all_agents)-1)]
    
    @staticmethod
    def writeresults(list_name, filename : str):
        """
        Writes a file from a list, list or tuple
        """
        file = open(filename, "a")
        for item in list_name:
            if not item==":":
                file.write(item+"\n")
        return None
    
    @staticmethod
    def filtergoogle(url_list) -> list:
        """
        Takes a list and removes the garbage urls that are added in google results page.
        """
        actual_results = []
        for url in url_list:
            if ".google." in url:
                pass
            elif "://webcache." in url:
                if ":" == url:
                    pass
                else:
                    actual_results.append(url[url.index(":http")+1:] )
            else:
                if ":" == url:
                    pass
                else:
                    actual_results.append(url)
        return list(actual_results)

    @staticmethod
    def showresults(iterable_name) -> None:
        """
        Takes a iterable and prints all the items from it.
        """
        for item in iterable_name:
            if not item==":":
                print(item)

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
parser.add_argument("--proxy", type=str, help="Specify proxy address and port as <address>:<port>")
args = parser.parse_args()

results_file = open("dorkresults.txt", "a")

if args.verbose and args.silent:
    print("[ ERR ] Verbose and Silent mode can\'t be turned on at same time. [ ERR ]\nTry:\n\tRemoving the -v "
          "/--verbose or -s/--silent switch.")
    exit(2)
    
    proxies = None
if args.proxy:
    proxies = {
        'http': f'http://{args.proxy}',
        'https': f'https://{args.proxy}'
    }
    
siteprefix = "site:"

domains = ["codepad.co", "scribd.com", "npmjs.com", "npm.runkit.com", "libraries.io", "ycombinator.com", "coggle.it",
           "papaly.com", "trello.com", "prezi.com", "jsdelivr.net", "codepen.io", "codeshare.io", "sharecode.io",
           "pastebin.com", "repl.it", "productforums.google.com", "gitter.im", "bitbucket.org", "*.atlassian.net", "*.jira.com"]

inurlprefix = "inurl:"

#Keywords for inurl: dorks
inurlkeywords = ["gitlab"]


if not args.silent:
    Scanner.banner()

if args.verbose:
    print("[v] Creating dorks... [v]")

for domain in domains:
    Scanner.createdork(siteprefix, domain, args)

del siteprefix
del domains

for inurlkeyword in inurlkeywords:
    Scanner.createdork(inurlprefix, inurlkeyword, args)

del inurlprefix
del inurlkeywords

for dork in dorkscontainer:
    if args.browser:
        Scanner.browseropen(args, dork)
    if args.show:
        if not args.verbose:
            pass
        else:
            if not args.silent:
                print(f"Getting the results from dork -> {unquote(dork)}")
    headers = {'user-agent': Scanner.getuseragent()}
    dork = dork.replace(" ", "+").replace(":", r"%3A")
    url = f"https://www.google.com/search?q={dork}"
    r = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    anc = soup.find_all('a')
    for link in anc:
        try:
            link.get('href')
        except:
            pass
        if link.get('href') != "#":
            try:
                if link.get('href').startswith('http'):
                    _link = link.get('href')
                    all_links.append(_link)     
            except:
                pass
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
all_links = Scanner.filtergoogle(all_links)

if not args.no_save_output:
    Scanner.writeresults(all_links, args.o)

if args.show:
    Scanner.showresults(all_links)

del dorkscontainer
del all_links


