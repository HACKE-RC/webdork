from os import system
try:
    import bs4, requests
except:
    print("[i] Installing requirements.txt... [i]")
    system("pip3 install -r requirements.txt")

system("cp webdork.py /data/data/com.termux/files/usr/bin/webdork")
print("[i] The tool has been installed. [i]\n [i] Use the command webdork -h to Get started! [i]")
