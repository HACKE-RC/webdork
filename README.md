# WebDork
 A Python tool to automate some dorking stuff to find information disclosures.
 Sugesstions and issues are welcome because i know codes can never be perfect.

### Note: Please do not use this tool for blackhat hacking purposes. I am not resposible for any damage caused by this tool.


### How to install?
This command is for Debian/Linux Based Shells.
```bash
git clone https://github.com/HACKE-RC/WebDork
cd WebDork
chmod +x *
sudo setup.py
```
For termux:
```bash
git clone https://github.com/HACKE-RC/WebDork
cd WebDork
chmod +x *
bash termux-setup.py
```

After running setup.py you can simply type webdork -h to see the help menu.

If you get any error while installing the tool you can create an issue or message me at twitter.com/coder_rc or If you are not able to run it after running the setup.py you can simply run ```sudo setup.py``` again to repair it.


### Requirements:
1. Python 3.x.x or greater.
2. sh based shell(Works fine in WSL, WSL2 and termux).

## How to use?
Just run the following command to see the help menu.
```bash
webdork -h
```
Example: Finding information diclosures in Trivago Company.
```bash
webdork -cn Trivago -v --show -bw -o out.txt
```

### Setup
[![asciicast](https://asciinema.org/a/BX9KgmIZ9cH93oa5D3e2rZ6fl.svg)](https://asciinema.org/a/BX9KgmIZ9cH93oa5D3e2rZ6fl)


#### Made with <3 by HACKE-RC commonly known as RC.
