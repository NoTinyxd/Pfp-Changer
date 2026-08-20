
import curl_cffi.requests as requests
from modules.header import Config,ua_builder
from modules.avatar import get_pfps
from pathlib import Path
import os
from datetime import datetime
from time import perf_counter
from modules.log import *
proxy = "" 
BASE_DIR = Path(__file__).resolve().parent
config = Config(BASE_DIR / "Input" / "config.json")

def clear_terminal():
    if os.name == "nt":
        os.system("cls")     
    else:
        os.system("clear")
        
class Changer():
    
    def __init__(self, config_path, token):
        self.config=config_path
        self.ua=(self.config.get("useragent"))
        self.token = token
        self.v = ua_builder(self.ua)
        self.headers = self.build_headers()
        self.session = requests.Session(impersonate="chrome145")

    @staticmethod
    def tokens_load(token_path):
        tokens = []
        with open(token_path, 'r') as token_file:
            for line in token_file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(':')
                if len(parts) == 3:
                    tokens.append(parts[2])
                elif len(parts) == 1:
                    tokens.append(parts[0])
        return tokens

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
def logs():
    timestamp=[{datetime.now().strftime('%H:%M:%S')}]
    
def main():
    clear_terminal()
    
    tokens = Changer.tokens_load("Input/token.txt")
    stars = "*" * 45
    for token in tokens:
        try:
            start = perf_counter() # or put this outside i just keep it here to calculate for each token
            client = Changer(config, token)
            response = client.update_avatar()


            elapsed = perf_counter() - start
            if response.status_code==200:
                success(f"Avatar updated successfully | token={token[:34]}{stars}, status_code={response.status_code}, took={elapsed:.2f}s")
            elif response.status_code==400:
                warning(f"response={response.text}, status_code={response.status_code}") #maybe ratelimit,hcap ,or unknown session
            else:
                error(f"response={response.text}, status_code={response.status_code}")
        except Exception as e:
            print(f"Failed exception={e}")
if __name__ == "__main__":
    main()
