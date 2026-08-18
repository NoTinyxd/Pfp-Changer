import token

import curl_cffi.requests as requests
from modules.helpers.header import Config,ua_builder
from modules.helpers.avatar import get_pfps
from pathlib import Path
import os
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
config = Config(BASE_DIR / "Input" / "config.json")

def clear_terminal():
    if os.name == "nt":
        os.system("cls")     
    else:
        os.system("clear")
        
class Changer():
    
    def __init__(self, config_path, token_path):
        self.config=config_path
        self.ua=(self.config.get("useragent"))
        self.token_path = token_path
        self.token = self.tokens_load()
        self.v = ua_builder(self.ua)
        self.headers = self.build_headers()
        self.session = requests.Session(impersonate="chrome145")
    def tokens_load(self):
        with open(self.token_path,'r') as token_file:
            token = token_file.read().strip()
            return token

    def build_headers(self):
        return {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.5",
            "authorization": self.token,
            "content-type": "application/json",
            "origin": "https://discord.com",
            "referer": "https://discord.com/channels/@me",
            "user-agent": self.ua,
            "x-discord-locale": "en-US",
            "x-discord-timezone": "Asia/Karachi",
            "x-installation-id": self.v.installation_id(),
            "x-super-properties": self.v.sup_prop(),
            "sec-ch-ua": self.v.sec_ch_ua(),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": self.v.sec_ch_ua_platform(),
        }

    def update_avatar(self):
        data_uri, pfp_name = get_pfps()

        avatar_description = (
            f"{pfp_name}, added "
            f"{datetime.now().strftime('%B %-d, %Y at %-I:%M %p')}"
        )

        payload = {
            "avatar": data_uri,
            "avatar_description": avatar_description,
        }
        
        response = self.session.patch(
            "https://discord.com/api/v9/users/@me",
            headers=self.headers,
            json=payload,
        )

        return response

def main():
    clear_terminal()
    
    client = Changer(config, "Input/token.txt")

    response = client.update_avatar()

    print(response.status_code)
    print(response.text)
    if response.status_code==200:
        print(f"Changed Avatar of {token[:10]}, status_code={response.status_code}")
    elif response.status_code==400:
        print(f"Hcaptcha occured, {response.text},{response.status_code}")

