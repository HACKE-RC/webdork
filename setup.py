from os import system
try:
    import bs4, requests
except:
    print("[i] Installing requirements.txt... [i]")
    system("sudo pip3 install -r requirements.txt")

system("cp webdork.py /usr/bin/webdork && chmod 755 /usr/bin/webdork")
print("[i] The tool has been installed. [i]\n [i] Use the command webdork -h to Get started! [i]")
