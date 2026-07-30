from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    ascii_text = """\033[32m                                                    
 ___   ___    ___   __  __ __   __   __      __  ___   ___ 
| _ \ | _ \  / _ \  \ \/ / \ \ / /   \ \    / / | __| | _ )
|  _/ |   / | (_) |  >  <   \ V /     \ \/\/ /  | _|  | _ \\
|_|   |_|_\  \___/  /_/\_\   |_|       \_/\_/   |___| |___/\033[0m\033[34m
    By: d'range
    Discord: qc2n\033[0m
"""
    print(ascii_text)

    c_protocol = inquirer.select(
    message="Select a protocol:",
    choices=["http", "socks4", "socks5"]
    ).execute()

    c_anonymity = inquirer.select(
        message="Select a anonymity",
        choices=["elite", "anonymous", "transparent"]
    ).execute()

    c_timeout = inquirer.select(
        message="Select a timeout:",
        choices=["1000 ms", "2500 ms", "5000 ms"]
    ).execute()

    if c_timeout == "1000 ms":
        c_elif = 1000
    elif c_timeout == "2500 ms":
        c_elif = 2500
    elif c_timeout == "5000 ms":
        c_elif = 5000

    c_p = c_protocol
    c_a = c_anonymity
    c_t = c_elif

    return c_p, c_a, c_t

if __name__ == "__main__":
    main()