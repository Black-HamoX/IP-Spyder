import requests
import json
from datetime import datetime
from colorama import Fore, Style

class IPFetcher:
    
    
    def __init__(self):
        self.sources = {
            'ip_api': 'http://ip-api.com/json/{}?fields=status,message,country,regionName,city,isp,org,lat,lon,timezone,query,as,reverse',
            'ipinfo': 'https://ipinfo.io/{}/json'
        }
    
    def get_info(self, ip_address):
        
        results = {}
        
       
        try:
            url = self.sources['ip_api'].format(ip_address)
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if data.get('status') == 'success':
                results['ip_api'] = {
                    'IP': data.get('query', 'N/A'),
                    'Country': data.get('country', 'N/A'),
                    'Region': data.get('regionName', 'N/A'),
                    'City': data.get('city', 'N/A'),
                    'ISP': data.get('isp', 'N/A'),
                    'Organization': data.get('org', 'N/A'),
                    'AS': data.get('as', 'N/A'),
                    'Latitude': data.get('lat', 'N/A'),
                    'Longitude': data.get('lon', 'N/A'),
                    'Timezone': data.get('timezone', 'N/A'),
                    'Reverse DNS': data.get('reverse', 'N/A')
                }
            else:
                results['ip_api'] = {'error': data.get('message', 'Unknown error')}
        except Exception as e:
            results['ip_api'] = {'error': str(e)}
        
        
        try:
            url = self.sources['ipinfo'].format(ip_address)
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if 'bogon' not in data:
                results['ipinfo'] = {
                    'IP': data.get('ip', 'N/A'),
                    'Hostname': data.get('hostname', 'N/A'),
                    'City': data.get('city', 'N/A'),
                    'Region': data.get('region', 'N/A'),
                    'Country': data.get('country', 'N/A'),
                    'Location': data.get('loc', 'N/A'),
                    'Organization': data.get('org', 'N/A'),
                    'Postal Code': data.get('postal', 'N/A'),
                    'Timezone': data.get('timezone', 'N/A')
                }
            else:
                results['ipinfo'] = {'error': 'IP is bogon (private/reserved)'}
        except Exception as e:
            results['ipinfo'] = {'error': str(e)}
        
        return results
    
    def format_output(self, results, ip_address):
        
        output = []
        output.append(Fore.CYAN + "═" * 60)
        output.append(Fore.YELLOW + f"📊 IP Information Report: {ip_address}")
        output.append(Fore.CYAN + "═" * 60)
        output.append(Fore.GREEN + f"📅 Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output.append(Fore.CYAN + "═" * 60 + "\n")
        
        for source, data in results.items():
            if 'error' in data:
                output.append(Fore.RED + f"[✗] {source.upper()} Error: {data['error']}")
                continue
            
            output.append(Fore.MAGENTA + f"📡 Source: {source.upper()}")
            output.append(Fore.CYAN + "─" * 40)
            
            for key, value in data.items():
                if value != 'N/A':
                    output.append(Fore.WHITE + f"  {key}: " + Fore.GREEN + f"{value}")
            
            output.append("")
        
        return "\n".join(output)