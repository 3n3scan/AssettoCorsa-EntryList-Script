import re
from os import system
import os
import time
import sys
import platform
import colorama
from colorama import Fore, init, Style
import win32ui
import requests


mytitle = "3n3scan's Assetto Corsa Entry List Script v1.0"


## Console Input Echos ##
ENTER_CHOICE_CONSOLE_ECHO = (f"""{Fore.BLUE}
╭─({Fore.RED}root@3n3scan{Fore.BLUE})-[{Style.RESET_ALL}~{Fore.BLUE}]
╰─{Fore.RED}#{Fore.LIGHTGREEN_EX} Enter the number of your choice:{Style.RESET_ALL} """)


FILE = 'entry_list.ini'


def sort_cars():
    try:
        with open(FILE, 'r') as file:
            data = file.read()

        cars = re.findall(r'\[CAR_\d+\].*?(?=\[CAR_\d+\]|\Z)', data, re.DOTALL)
        sorted_cars = sorted(cars, key=lambda car: int(re.search(r'\[CAR_(\d+)\]', car).group(1)))
        sorted_data = re.sub(r'\[CAR_\d+\].*?(?=\[CAR_\d+\]|\Z)', '', data, flags=re.DOTALL) + '\n'.join(sorted_cars)

        with open(FILE, 'w') as file:
            file.write(sorted_data)

        win32ui.MessageBox(f'Done. Resorted entry_list.ini. Please check the file.\nGoing to Main Page in 5 Seconds...\nThank you for using my little Script. :)', f"{mytitle}")
        time.sleep(5)
        main()

    except requests.RequestException as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(3)
        sys.exit()
        
    else:
        win32ui.MessageBox("Something went Wrong! Please Contact the Developer of this Script", f"{mytitle}")
        sys.exit()


def add_adan():
    try:
        with open(FILE, 'r') as file:
            lines = file.readlines()

        lines = [line.rstrip() + '/ADAn\n' if line.startswith('SKIN=') else line for line in lines]

        with open(FILE, 'w') as file:
            file.writelines(lines)

        win32ui.MessageBox(f'Done. Added "/ADAn" to every line starting with "SKIN=". Please check the file.\nGoing to Main Page in 5 Seconds...\nThank you for using my little Script. :)', f"{mytitle}")
        time.sleep(5)
        main()

    except requests.RequestException as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(3)
        sys.exit()
        
    else:
        win32ui.MessageBox("Something went Wrong! Please Contact the Developer of this Script", f"{mytitle}")
        sys.exit()
    

def add_ai():
    try:
        with open(FILE, 'r') as file:
            lines = file.readlines()

        with open(FILE, 'w') as file:
            for line in lines:
                file.write(line)
                if 'RESTRICTOR=0' in line:
                    file.write('AI=fixed\n')

        win32ui.MessageBox(f'Done. Added "AI=fixed" to every line with "RESTRICTOR=0". Please check the file.\nGoing to Main Page in 5 Seconds...\nThank you for using my little Script. :)', f"{mytitle}")
        time.sleep(5)
        main()

    except requests.RequestException as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(3)
        sys.exit()
        
    else:
        win32ui.MessageBox("Something went Wrong! Please Contact the Developer of this Script", f"{mytitle}")
        sys.exit()


def get_models():
    try:
        with open(FILE, 'r') as file:
            data = file.read()

        models = re.findall(r'MODEL=(.*?)\n', data)
        unique_models = list(set(models))
        other_models = [model for model in unique_models if 'traffic' not in model.lower()]
        traffic_models = [model for model in unique_models if 'traffic' in model.lower()]
        other_models.sort()
        traffic_models.sort()
        sorted_models = other_models + traffic_models

        print('Extracted all models:\n===============================')
        for model in sorted_models:
            print(f'{model};')
        print('===============================\n')

        win32ui.MessageBox(f"Done. Extracted all models.\nGoing to Main Page in 5 Seconds...\nThank you for using my little Script. :)", f"{mytitle}")
        time.sleep(5)
        main()

    except requests.RequestException as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(2)
        sys.exit()
        
    else:
        win32ui.MessageBox("Something went Wrong! Please Contact the Developer of this Script", f"{mytitle}")
        sys.exit()


def exit_script():
    system("cls")
    win32ui.MessageBox(f"Exiting... Thank you for using this script!", f"{mytitle}")
    sys.exit()
    

def main():
    system("title "+mytitle)
    os = platform.system()
    if os == "Windows":
        system("cls")
    else:
        system("clear")
        print(chr(27) + "[2J")
    print(f"""{Fore.CYAN}
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

 ▄▄▄        ██████   ██████ ▓█████▄▄▄█████▓▄▄▄█████▓ ▒█████       ██████  ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓
▒████▄    ▒██    ▒ ▒██    ▒ ▓█   ▀▓  ██▒ ▓▒▓  ██▒ ▓▒▒██▒  ██▒   ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒
▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒███  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░  ██▒   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░
░██▄▄▄▄██   ▒   ██▒  ▒   ██▒▒▓█  ▄░ ▓██▓ ░ ░ ▓██▓ ░ ▒██   ██░     ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░ 
 ▓█   ▓██▒▒██████▒▒▒██████▒▒░▒████▒ ▒██▒ ░   ▒██▒ ░ ░ ████▓▒░   ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ 
 ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒ ░░     ▒ ░░   ░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   
  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ░  ░   ░        ░      ░ ▒ ▒░    ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░    
  ░   ▒   ░  ░  ░  ░  ░  ░     ░    ░        ░      ░ ░ ░ ▒     ░  ░  ░  ░          ░░   ░  ▒ ░░░         ░      
      ░  ░      ░        ░     ░  ░                     ░ ░           ░  ░ ░         ░      ░                    
                                                                         ░                                       
                    {mytitle}
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{Style.RESET_ALL}
                                {Fore.MAGENTA} > Developed by: 3n3scan{Style.RESET_ALL}
                                
{Fore.CYAN}> Choose an option:{Style.RESET_ALL}
{Fore.GREEN}> [1] Sort Cars{Style.RESET_ALL}
{Fore.LIGHTBLUE_EX}> [2] Add /ADAn to SKIN lines{Style.RESET_ALL}
{Fore.LIGHTMAGENTA_EX}> [3] Add AI= lines{Style.RESET_ALL}
{Fore.YELLOW}> [4] Get all models listed{Style.RESET_ALL}
{Fore.RED}> [5] Exit Script{Style.RESET_ALL}
""")

    choice = input(ENTER_CHOICE_CONSOLE_ECHO)

    if choice == "1":
        sort_cars()
    elif choice == "2":
        add_adan()
    elif choice == "3":
        add_ai()
    elif choice == "4":
        get_models()
    elif choice == "5":
        exit_script()
    else:
        print(f"{Fore.RED}> Invalid choice. Please enter '{Fore.CYAN}1{Fore.RED}', '{Fore.CYAN}2{Fore.RED}', '{Fore.CYAN}3{Fore.RED}', '{Fore.CYAN}4{Fore.RED}' or '{Fore.CYAN}5{Fore.RED}' <{Style.RESET_ALL}")
        time.sleep(2)
        main()


if __name__ == "__main__":
    main()
