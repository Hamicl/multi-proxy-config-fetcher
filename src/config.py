# config.py
import os

TELEGRAM_CHANNELS = [
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/V2ray_Alpha",
    "https://t.me/s/SvnV2ray",
    "https://t.me/s/RadixVPN"
]

SUPPORTED_PROTOCOLS = [
    "wireguard://",
    "hysteria2://",
    "vless://",
    "vmess://",
    "ss://",
    "trojan://"
]

MIN_CONFIGS_PER_CHANNEL = 2
MAX_CONFIG_AGE_DAYS = 2
OUTPUT_FILE = 'configs/proxy_configs.txt'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}