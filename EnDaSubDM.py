#Import needed modules
from Modules.Style import *
import ipaddress

#Banner variable
banner = """
    ███████╗███╗   ██╗██████╗  █████╗     ███████╗██╗   ██╗██████╗ ██████╗ ███╗   ███╗     
    ██╔════╝████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██║   ██║██╔══██╗██╔══██╗████╗ ████║    
    █████╗  ██╔██╗ ██║██║  ██║███████║    ███████╗██║   ██║██████╔╝██║  ██║██╔████╔██║     
    ██╔══╝  ██║╚██╗██║██║  ██║██╔══██║    ╚════██║██║   ██║██╔══██╗██║  ██║██║╚██╔╝██║     
    ███████╗██║ ╚████║██████╔╝██║  ██║    ███████║╚██████╔╝██████╔╝██████╔╝██║ ╚═╝ ██║     
    ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     
"""

#Define a function which verifies if a host is on
def check_host(host):
    ok = 0
    try:
        host_ip = socket.gethostbyname(host)
        ok = 1
    except socket.error:
        ok = 0
    try:
        hostname = f"fnuwbfunnfnaionf.{host}"
        socket.gethostbyname(hostname)
        ok = 1
    except:
        ok = 0
    return not ok

#Define the main function of enumerating the subdomains
def enumerate_subdomains(filename, host,times=0.1):
    tries = 0
    finded = 0
    if os.name in ("dos","nt"):
        os.system(f"title EnDa SubDomain Finder ^| Tries : {tries} ^| Finded : {finded} ^| EnDaTeam on GITHUB")
    with open(filename, 'r') as file:
        for line in file:
            subdomain = line.strip()
            tries = tries + 1
            hostname = f"{subdomain}.{host}"
            print(f"    {Fore.WHITE}[{Fore.YELLOW}!{Fore.RESET}] >> Trying {hostname}                                                                       ",end="\r")
            time.sleep(float(times))
            try:
                socket.gethostbyname(hostname)
                print("    " + Fore.WHITE + "[" + Fore.LIGHTMAGENTA_EX + "+" + Fore.WHITE + "] >> " + Fore.LIGHTCYAN_EX + subdomain + Fore.LIGHTGREEN_EX + f".{host}" + Fore.LIGHTYELLOW_EX + " is available")
                finded = finded + 1
            except socket.gaierror:
                pass
            if os.name in ("dos","nt"):
                os.system(f"title EnDa SubDomain Finder ^| Tries : {tries} ^| Finded : {finded} ^| EnDaTeam on GITHUB")
    if finded == 0:
        print("",end="")
        print("    " + Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + "No subdomain was found!                       ")

#Create a start-up
clearConsole()
enter()
print(banner_color(banner,random.randint(1,5)))
enter()
print(Fore.LIGHTYELLOW_EX + "    [============================== " + Fore.WHITE + "Input the hostname" + Fore.LIGHTYELLOW_EX + " ==============================]     " + Fore.RESET)
print(Fore.LIGHTRED_EX + "    [========= " + Fore.LIGHTWHITE_EX + "Leave the inputs blank if you want to use the default values" + Fore.LIGHTRED_EX + " =========]" + Fore.RESET)
enter()
while True:
    try:
        if os.name in ("dos","nt"):
            os.system(f"title EnDa SubDomain Finder ^| Tries : 0 ^| Finded : 0 ^| EnDaTeam on GITHUB")
        hostinput = 1
        while hostinput:
            hostname = input(Fore.RESET + f"    [{Fore.LIGHTGREEN_EX}+{Fore.RESET}]" + Fore.LIGHTCYAN_EX + " Host" + Fore.RESET + " >> ")
            enter()
            if check_host(hostname):
                print(Fore.RESET + f"    [{Fore.GREEN}#{Fore.RESET}] >> {Fore.LIGHTGREEN_EX}The host '{hostname}' is online" + Fore.RESET)
                hostinput = 0
                enter()
            else:
                print(Fore.RESET + f"    [{Fore.RED}#{Fore.RESET}] >> {Fore.LIGHTRED_EX}The host '{hostname}' is offline, try another one!" + Fore.RESET)
                enter()
        timeinput = 1
        while timeinput:
            times = input(Fore.RESET + f"    [{Fore.LIGHTGREEN_EX}+{Fore.RESET}]" + Fore.LIGHTCYAN_EX + " Time" + Fore.RESET + " >> ")
            enter()
            if str(times).lower() in (""," "):
                times = 0.1
            try:
                float(times)
            except:
                print(Fore.RESET + f"    [{Fore.RED}#{Fore.RESET}] >> {Fore.LIGHTRED_EX}The inputed time is not available!" + Fore.RESET)
                enter()
            else:
                timeinput = 0
        wordlistinput = 1
        while wordlistinput:
            wordlist = input(Fore.RESET + f"    [{Fore.LIGHTGREEN_EX}+{Fore.RESET}]" + Fore.LIGHTCYAN_EX + " Wordlist file" + Fore.RESET + " >> ")
            enter()
            if str(wordlist).lower() in (""," "):
                wordlist = "./DefaultWordlist.txt"
            try:
                file = open(wordlist,"r")
            except:
                print(Fore.RESET + f"     [{Fore.RED}#{Fore.RESET}] >> {Fore.LIGHTRED_EX}The inputed file does not exist or can not be openned!" + Fore.RESET)
                enter()
            else:
                wordlistinput = 0
        enumerate_subdomains(wordlist,hostname,times)
        enter()
        another_scan = input(Fore.RESET + f"    [{Fore.LIGHTGREEN_EX}?{Fore.RESET}]" + Fore.LIGHTGREEN_EX + " Do you want to do another scan? (Y/N)" + Fore.RESET + " >> ")
        if str(another_scan).lower() in ("n","no","exit","quit"):
            enter()
            print("    " + Fore.WHITE + "[" + Fore.BLUE + "!" + Fore.BLUE + "]" + Fore.WHITE + " >> " + Fore.LIGHTBLUE_EX + "Roger that, exiting the EnDa SubDomanin Finder!" + Fore.RESET)
            time.sleep(2)
            exit()
        enter()
    except KeyboardInterrupt:
        enter(2)
        exiting = input(Fore.RESET + f"    [{Fore.RED}?{Fore.RESET}]" + Fore.LIGHTRED_EX + " Do you want to do exit the program? (Y/N)" + Fore.RESET + " >> ")
        if str(exiting).lower() not in ("n","no","exit","quit"):
            enter()
            print("    " + Fore.WHITE + "[" + Fore.BLUE + "!" + Fore.WHITE + "]" + Fore.WHITE + " >> " + Fore.LIGHTBLUE_EX + "Roger that, exiting the EnDa SubDomanin Finder!" + Fore.RESET)
            time.sleep(2)
            exit()
        enter()