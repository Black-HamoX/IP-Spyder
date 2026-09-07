from pyfiglet import Figlet
from termcolor import colored
from colorama import init, Fore, Back, Style

init(autoreset=True)

def generate_banner():
    
    
    f = Figlet(font='slant')
    banner_text = f.renderText('IP Spyder')
    
    
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_banner = ""
    
    
    for i, line in enumerate(banner_text.split('\n')):
        if line.strip():
            color = colors[i % len(colors)]
            colored_banner += colored(line, color, attrs=['bold', 'blink']) + '\n'
    
    
    border = colored('═' * 60, 'cyan', attrs=['bold'])
    title = colored('⚡ An Excellent OSINT Tool for IP Information ⚡', 'white', 'on_blue', attrs=['bold'])
    
    banner = f"""
{colored('┌' + '═' * 58 + '┐', 'cyan')}
{colored('│', 'cyan')} {title} {colored('│', 'cyan')}
{colored('├' + '═' * 58 + '┤', 'cyan')}
{colored_banner}
{colored('├' + '═' * 58 + '┤', 'cyan')}
{colored('│', 'cyan')} {colored('🔍 Developed by: @C5_72', 'green', attrs=['bold'])} {colored('│', 'cyan')}
{colored('│', 'cyan')} {colored('📡 Version: 1.0.0', 'yellow', attrs=['bold'])} {colored('│', 'cyan')}
{colored('└' + '═' * 58 + '┘', 'cyan')}
    """
    return banner

def print_banner():

    print(generate_banner())
    print(Fore.YELLOW + "=" * 60)
    print(Fore.CYAN + "[✓] Tool Loaded Successfully!" + Fore.GREEN + " Ready to Hunt IPs 🎯")
    print(Fore.YELLOW + "=" * 60 + "\n")