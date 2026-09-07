import os
import json
import requests
from datetime import datetime
from colorama import Fore, Style

def clear_screen():
    
    os.system('clear' if os.name == 'posix' else 'cls')

def save_to_file(data, filename=None):
    
    if filename is None:
        filename = f"ip_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("IP SPYDER - Scan Report\n")
            f.write("=" * 60 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            f.write(data)
        return True, filename
    except Exception as e:
        return False, str(e)

def validate_ip(ip):
    
    import re
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def get_public_ip():
    
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json().get('ip')
    except:
        return None