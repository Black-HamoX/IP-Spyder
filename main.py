import sys
import os
from colorama import init, Fore, Style
from modules.banner import print_banner
from modules.ip_fetcher import IPFetcher
from modules.utils import clear_screen, save_to_file, validate_ip, get_public_ip

init(autoreset=True)

def main_menu():

    clear_screen()
    print_banner()
    
    print(Fore.CYAN + "[1]" + Fore.WHITE + " Scan Specific IP")
    print(Fore.CYAN + "[2]" + Fore.WHITE + " Scan My Public IP")
    print(Fore.CYAN + "[3]" + Fore.WHITE + " About Tool")
    print(Fore.CYAN + "[4]" + Fore.WHITE + " Exit")
    print()
    
    choice = input(Fore.YELLOW + "[?] Select Option: " + Fore.WHITE)
    return choice

def scan_ip(ip_address):
    
    print(Fore.YELLOW + f"\n[⏳] Scanning IP: {ip_address} ...")
    print(Fore.CYAN + "─" * 50 + "\n")
    
    fetcher = IPFetcher()
    results = fetcher.get_info(ip_address)
    formatted_output = fetcher.format_output(results, ip_address)
    
    print(formatted_output)
    
    
    print(Fore.CYAN + "═" * 60)
    print(Fore.GREEN + "[✓] Scan Completed!")
    print(Fore.YELLOW + "[1] Save Results")
    print(Fore.YELLOW + "[2] Back to Menu")
    print(Fore.YELLOW + "[3] Exit")
    
    choice = input(Fore.WHITE + "\n[?] Choose: ")
    
    if choice == '1':
        success, result = save_to_file(formatted_output)
        if success:
            print(Fore.GREEN + f"[✓] Saved to: {result}")
        else:
            print(Fore.RED + f"[✗] Error: {result}")
        input(Fore.WHITE + "\nPress Enter to continue...")
    elif choice == '3':
        sys.exit(0)
    
    return choice != '2'

def about():
    
    clear_screen()
    print(Fore.CYAN + "═" * 60)
    print(Fore.YELLOW + "📌 IP Spyder Tool - Version 1.0.0")
    print(Fore.CYAN + "═" * 60)
    print(Fore.GREEN + """
    🔍 What is IP Spyder?
    An advanced OSINT tool for gathering information about IP addresses.
    
    ⚡ Features:
    • Multiple data sources for accuracy
    • Beautiful colored banner
    • Save results to file
    • Works perfectly on Termux
    • Easy installation process
    
    🛡️ Legal Disclaimer:
    This tool is for educational purposes only.
    Use it only on IPs you own or have permission to scan.
    
    👨‍💻 Devloper: @C5_72 
    📧 Telegram channel: https://t.me/rootaccess_7
    """)
    print(Fore.CYAN + "═" * 60)
    input(Fore.WHITE + "\nPress Enter to go back...")

def main():
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            clear_screen()
            print_banner()
            ip_input = input(Fore.GREEN + "[+] Enter IP Address: " + Fore.WHITE)
            
            if validate_ip(ip_input):
                scan_ip(ip_input)
            else:
                print(Fore.RED + "[✗] Invalid IP Address!")
                input(Fore.WHITE + "Press Enter to continue...")
                
        elif choice == '2':
            clear_screen()
            print_banner()
            public_ip = get_public_ip()
            if public_ip:
                print(Fore.GREEN + f"[✓] Your Public IP: {public_ip}")
                scan_ip(public_ip)
            else:
                print(Fore.RED + "[✗] Could not fetch public IP!")
                input(Fore.WHITE + "Press Enter to continue...")
                
        elif choice == '3':
            about()
            
        elif choice == '4':
            print(Fore.GREEN + "\n[✓] Goodbye! Stay safe and ethical! 🛡️")
            sys.exit(0)
            
        else:
            print(Fore.RED + "[✗] Invalid Option!")
            input(Fore.WHITE + "Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n[!] Interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\n[!] Unexpected Error: {e}")
        sys.exit(1)
