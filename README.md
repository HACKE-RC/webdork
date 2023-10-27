<h1 align="center">
  <br>
  WebDork
  <br>
</h1>

<p align="center">An open-source tool to find publicly available sensitive information about Companies and Organisations!</p>

# WebDork
A Python tool to automate search for information disclosures.

## Note:
> ## As a user of this tool you agree to the following terms:
> **I shall never use this tool for anything unethical.**  
> **I will not disclose any information found by this tool.**

**Not all results found by this tool are sensitive information. If you find any information using this tool you must verify it by yourself and check whether the information can really cause any major/minor harm.**

### Example finds:
- Backend related information.
- Company's or Orgnisation's internal plans, mindmaps, etc.
- Internal tools.

## Compatibility
Check your Python version by typing in
```bash
$ python --version
```
If you get the following
```bash
Python 3.9.0
```
or any version greater than or equal to 3.9, this script has been tested and confirmed to be supported.

## Installation

### For termux
```bash
pkg install git -y 
pkg install python -y 
git clone https://github.com/HACKE-RC/webdork
cd webdork
python termux-setup.py
```

### For iSH
```bash
apk add git
apk add python3
apk add py3-pip
git clone https://github.com/HACKE-RC/webdork
cd webdork
python setup.py
```

### For Debian-based GNU/Linux distributions
```bash
git clone https://github.com/HACKE-RC/webdork
cd webdork
sudo python3 setup.py
```

## Usage:
**Help menu of the tool**
```bash
webdork -h
usage: main.py [-h] -cn Company name [-bw] [--show] [-o Output] [-v] [-s] [--no-save-output]

A python tool to automatically dork on a given company\'s name.

optional arguments:
  -h, --help            show this help message and exit
  -cn Company name, --company-name Company name
                        Name of the company
  -bw, --browser        Search the dorks in browser.
  --show                Print results from the dorks.
  -o Output             Output filename(default is dorkresults.txt).
  -v, --verbose         Turn verbose mode on.
  -s, --silent          Just save the results without printing anything.
  --no-save-output      Don\'t save the output in file.
```

### Example usage:
```bash
webdork -cn Hackerone -bw --show -v -o output.txt
```

## Arguments :
- Company/Organisation name to search for : -cn
- Open the dorks in browser : -bw, --browser
- Show dork results in terminal : --show
- Output filename : -o
- Better output : -v, --verbose
- Directly save the results without printing anything : -s, --silent
- Do not save the result in any file : --no-save-output

### Shoutout :
- [Ahsan khan](https://twitter.com/hunter0x7) for [this tweet](https://twitter.com/hunter0x7/status/1334818003179933696?s=20).
- [TheSpeedX](https://twitter.com/The_SpeedX) for writing docs of Tbomb in such a amazing way!. I copied some stuff from his docs about TBomb.
- [Resethacker!](https://linktr.ee/RESETHACKER)
- [aks1337](https://github.com/aksl337) for pull request.
- [Akash Chhabra](https://github.com/hackingguy) for pull request.

**If you like my work consider contacting me on Twitter @rcx86 for donation related information.**

## Demonstrative Video:

- https://youtu.be/JCReY9O5oTk

