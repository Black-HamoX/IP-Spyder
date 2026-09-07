RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' 

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════╗"
echo "║                                                       ║"
echo "║  ${GREEN}IP SPYDER - Installation Script${BLUE}                    ║"
echo "║  ${YELLOW}OSINT Tool for IP Information${BLUE}                     ║"
echo "║                                                       ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo -e "${NC}"


if [ -z "$PREFIX" ]; then
    echo -e "${RED}[!] This script is designed for Termux only!${NC}"
    exit 1
fi

echo -e "${YELLOW}[*] Updating packages...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${YELLOW}[*] Installing required packages...${NC}"
pkg install -y python python-pip git

echo -e "${YELLOW}[*] Installing Python libraries...${NC}"
pip install -r requirements.txt

echo -e "${YELLOW}[*] Setting up permissions...${NC}"
chmod +x main.py

echo -e "${GREEN}[✓] Installation completed successfully!${NC}"
echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════╗"
echo "║                                                       ║"
echo "║  ${GREEN}Installation Complete!${BLUE}                             ║"
echo "║                                                       ║"
echo "║  ${YELLOW}To run the tool:${BLUE}                                   ║"
echo "║  ${WHITE}python main.py${BLUE}                                     ║"
echo "║                                                       ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo -e "${NC}"