import requests
import cloudscraper
import json
import os
from colorama import *
from datetime import datetime
from fake_useragent import FakeUserAgent
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Boinkers:
    def __init__(self) -> None:
        self.scraper = cloudscraper.create_scraper()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'boink.boinkers.co',
            'Origin': 'https://boink.boinkers.co',
            'Pragma': 'no-cache',
            'Referer': 'https://boink.boinkers.co/sluts',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': FakeUserAgent().random
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Boinkers - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def load_liveOpId(self, retries=3):
        url = 'https://boink.boinkers.co/public/data/config?p=android'
        headers = {
            **self.headers,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.get(url, headers=headers, timeout=10)
                if response.status_code == 403:
                    return None

                response.raise_for_status()
                return response.json()['liveOps'][0]['_id']
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def users_login(self, query: str, retries=3):
        url = 'https://boink.boinkers.co/public/users/loginByTelegram?tgWebAppStartParam=boink1493482017&p=android'
        data = json.dumps({"initDataString":query, "sessionParams":{}})
        headers = {
            **self.headers,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, data=data, timeout=10)
                response.raise_for_status()
                return response.json()['token']
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def users_me(self, token: str, retries=3):
        url = 'https://boink.boinkers.co/api/users/me?p=android'
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def claim_booster(self, token: str, retries=3):
        url = 'https://boink.boinkers.co/api/boinkers/addShitBooster?p=android'
        data = json.dumps({'multiplier':2, 'optionNumber':1})
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, data=data, timeout=10)
                if response.status_code == 403:
                    return None

                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def claim_inbox(self, token: str, message_id: str, retries=3):
        url = 'https://boink.boinkers.co/api/inboxMessages/claimInboxMessagePrize?p=android'
        data = json.dumps({'inboxMessageId':message_id})
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, data=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def collect_friends(self, token: str, friend_id: str, retries=3):
        url = f'https://boink.boinkers.co/api/friends/claimFriendMoonBoinkerReward/{friend_id}?p=android'
        data = {}
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, json=data, timeout=10)
                if response.status_code in [403, 429]:
                    return None

                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def push_friends(self, token: str, friend_id: str, retries=3):
        url = f'https://boink.boinkers.co/api/friends/pushFriendToPlay/{friend_id}?p=android'
        data = {}
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, json=data, timeout=10)
                if response.status_code in [403, 429]:
                    return None

                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def tasks(self, token: str, retries=3):
        url = 'https://boink.boinkers.co/api/rewardedActions/getRewardedActionList?p=android'
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def start_tasks(self, token: str, name_id: str, retries=3):
        url = f'https://boink.boinkers.co/api/rewardedActions/rewardedActionClicked/{name_id}?p=android'
        data = {}
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        try:
            response = self.scraper.post(url, headers=headers, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, requests.Timeout, ValueError) as e:
            self.log(f"{Fore.RED + Style.BRIGHT}Error While Start Tasks: {str(e)}{Style.RESET_ALL}")
            return None
        
    def claim_tasks(self, token: str, name_id: str, retries=3):
        url = f'https://boink.boinkers.co/api/rewardedActions/claimRewardedAction/{name_id}?p=android'
        data = {}
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        try:
            response = self.scraper.post(url, headers=headers, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, requests.Timeout, ValueError) as e:
            self.log(f"{Fore.RED + Style.BRIGHT}Error While Claim Tasks: {str(e)}{Style.RESET_ALL}")
            return None
        
    def watch_ads(self, token: str, key: str, retries=3):
        url = 'https://boink.boinkers.co/api/rewardedActions/ad-watched?p=android'
        data = json.dumps({'adsForSpins':False, 'providerId':key})
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        try:
            response = self.scraper.post(url, headers=headers, data=data, timeout=10)
            response.raise_for_status()
            return True
        except (requests.RequestException, requests.Timeout, ValueError) as e:
            self.log(f"{Fore.RED + Style.BRIGHT}Error While Watch Ads: {str(e)}{Style.RESET_ALL}")
            return None
        
    def spin_wheel(self, token: str, game_type: str, liveOpId: str, multiplier: str, retries=3):
        url = f'https://boink.boinkers.co/api/play/spin{game_type.capitalize()}/{multiplier}?p=android'
        data = json.dumps({'liveOpId':liveOpId} if liveOpId else {})
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, data=data, timeout=10)
                if response.status_code == 403:
                    return None

                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def open_elevator(self, token: str, liveOpId: str, retries=3):
        url = 'https://boink.boinkers.co/api/play/openElevator?p=android'
        data = json.dumps({'liveOpId':liveOpId})
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, data=data, timeout=10)
                if response.status_code == 403:
                    return None

                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def quit_elevator(self, token: str, retries=3):
        url = 'https://boink.boinkers.co/api/play/quitAndCollect?p=android'
        data = {}
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, json=data, timeout=10)
                if response.status_code == 403:
                    return None

                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def upgrade_boinker(self, token: str, upgrade_type: str, retries=3):
        url = f'https://boink.boinkers.co/api/boinkers/{upgrade_type}?p=android'
        data = {}
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, json=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def raffle_data(self, token: str, retries=3):
        url = 'https://boink.boinkers.co/api/raffle/getRafflesData?p=android'
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def claim_raffle(self, token: str, retries=3):
        url = 'https://boink.boinkers.co/api/raffle/claimTicketForUser?p=android'
        data = {}
        headers = {
            **self.headers,
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                response = self.scraper.post(url, headers=headers, json=data, timeout=10)
                if response.status_code == 403:
                    return None

                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}{attempt+1}/{retries}{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def question(self):
        while True:
            collect_friends = input("Auto Push & Collect Friends? [y/n] -> ").strip().lower()
            if collect_friends in ["y", "n"]:
                collect_friends = collect_friends == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to push & collect or 'n' to skip.{Style.RESET_ALL}")
        
        # while True:
        #     complete_tasks = input("Auto Complete Tasks? [y/n] -> ").strip().lower()
        #     if complete_tasks in ["y", "n"]:
        #         complete_tasks = complete_tasks == "y"
        #         break
        #     else:
        #         print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to complete or 'n' to skip.{Style.RESET_ALL}")
        
        return collect_friends
        
    def process_query(self, query: str, liveOpId: str, collect_friends: bool):
        token = self.users_login(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Query Id Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if token:
            user = self.users_me(token)
            if user:
                gold = user.get('currencySoft', 0)
                shit = user.get('currencyCrypto', 0)
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['userName']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {gold} 🪙 {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT} -{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {shit:.4f} 💩 {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                claim_booster = self.claim_booster(token)
                if claim_booster:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Boost Mining{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Boost Mining{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                inbox = user['inboxMessages']
                if inbox:
                    completed = False
                    for message in inbox:
                        message_id = message['_id']
                        status = message['state']

                        if message and status != "claimed":
                            claim_inbox = self.claim_inbox(token, message_id)
                            if claim_inbox:
                                reward = claim_inbox['gottenPrize']['prizeValue']
                                reward_type = claim_inbox.get('gottenPrize', {}).get('prizeName', 'Gold')
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Inbox{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {message['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {reward} {reward_type} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Inbox{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {message['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                        else:
                            completed = True

                    if completed:
                        self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Inbox{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Clear {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Inbox{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Available Message {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                if collect_friends:
                    friends = user['friends']
                    if friends:
                        for friend in friends:
                            friend_id = friend['_id']

                            if friend is not None:
                                collect = self.collect_friends(token, friend_id)
                                if collect and collect['invitedFriendsData']:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Friend{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {friend['userName']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {collect['energyReward']} Spin Energy {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Friend{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {friend['userName']} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}No Availabe Reward to Claim{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                time.sleep(1)

                                push = self.push_friends(token, friend_id)
                                if push and push['invitedFriendsData']:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Friend{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {friend['userName']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Pushed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Friend{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {friend['userName']} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Not Time to Push{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                time.sleep(1)

                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Friend{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} No Available Friend {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Friend{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Push & Collect Is Skipped {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)              

                # if complete_tasks:
                #     claimed_tasks = user.get('rewardedActions', {})
                #     if not isinstance(claimed_tasks, dict):
                #         claimed_tasks = {}
                        
                #     tasks = self.tasks(token)
                #     if tasks:
                #         for task in tasks:
                #             name_id = task['nameId']
                #             reward = task['prizes'][0]['prizeValue']
                #             reward_type = task['prizes'][0]['prizeTypeName']
                #             task_type = task['type']
                #             delay = task['secondsToAllowClaim']

                #             if task_type == 'watch-ad':
                #                 start = self.start_tasks(token, name_id)
                #                 if start:
                #                     self.log(
                #                         f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #                         f"{Fore.WHITE + Style.BRIGHT} {task['text']} {Style.RESET_ALL}"
                #                         f"{Fore.GREEN + Style.BRIGHT}Is Started{Style.RESET_ALL}"
                #                         f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                #                     )
                #                     for remaining in range(delay, 0, -1):
                #                         print(
                #                             f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                #                             f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                #                             f"{Fore.MAGENTA + Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                #                             f"{Fore.YELLOW + Style.BRIGHT} {remaining} {Style.RESET_ALL}"
                #                             f"{Fore.WHITE + Style.BRIGHT}Seconds to Claim Reward{Style.RESET_ALL}"
                #                             f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}   ",
                #                             end="\r",
                #                             flush=True
                #                         )
                #                         time.sleep(1)

                #                     key = task['verification']['paramKey']
                #                     self.watch_ads(token, key)
                #                     claim = self.claim_tasks(token, name_id)
                #                     if claim and claim['newUserRewardedAction']['claimDateTime']:
                #                         self.log(
                #                             f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #                             f"{Fore.WHITE + Style.BRIGHT} {task['text']} {Style.RESET_ALL}"
                #                             f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                #                             f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                #                             f"{Fore.WHITE + Style.BRIGHT} {reward} {reward_type} {Style.RESET_ALL}"
                #                             f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                #                         )
                #                     else:
                #                         self.log(
                #                             f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #                             f"{Fore.WHITE + Style.BRIGHT} {task['text']} {Style.RESET_ALL}"
                #                             f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                #                             f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}            "
                #                         )
                #                     time.sleep(1)

                #             else:
                #                 if name_id in claimed_tasks.keys():
                #                     continue

                #                 if task_type == 'linkWithId' or delay == 172800:
                #                     continue

                #                 start = self.start_tasks(token, name_id)
                #                 if start:
                #                     started = start.get('clickDateTime', None)
                #                     claimed = start.get('claimDateTime', None)

                #                     if started and not claimed:
                #                         self.log(
                #                             f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #                             f"{Fore.WHITE + Style.BRIGHT} {task['text']} {Style.RESET_ALL}"
                #                             f"{Fore.GREEN + Style.BRIGHT}Is Started{Style.RESET_ALL}"
                #                             f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                #                         )
                #                         for remaining in range(delay, 0, -1):
                #                             print(
                #                                 f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                #                                 f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                #                                 f"{Fore.MAGENTA + Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                #                                 f"{Fore.YELLOW + Style.BRIGHT} {remaining} {Style.RESET_ALL}"
                #                                 f"{Fore.WHITE + Style.BRIGHT}Seconds to Claim Reward{Style.RESET_ALL}"
                #                                 f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}   ",
                #                                 end="\r",
                #                                 flush=True
                #                             )
                #                             time.sleep(1)

                #                         claim = self.claim_tasks(token, name_id)
                #                         if claim and claim['newUserRewardedAction']['claimDateTime']:
                #                             self.log(
                #                                 f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #                                 f"{Fore.WHITE + Style.BRIGHT} {task['text']} {Style.RESET_ALL}"
                #                                 f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                #                                 f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                #                                 f"{Fore.WHITE + Style.BRIGHT} {reward} {reward_type} {Style.RESET_ALL}"
                #                                 f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                #                             )
                #                         else:
                #                             self.log(
                #                                 f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #                                 f"{Fore.WHITE + Style.BRIGHT} {task['text']} {Style.RESET_ALL}"
                #                                 f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                #                                 f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}            "
                #                             )
                #                         time.sleep(1)

                #                     elif started and claimed:
                #                         self.log(
                #                             f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #                             f"{Fore.WHITE + Style.BRIGHT} {task['text']} {Style.RESET_ALL}"
                #                             f"{Fore.YELLOW + Style.BRIGHT}Is Already Claimed{Style.RESET_ALL}"
                #                             f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                #                         )

                #                 else:
                #                     self.log(
                #                         f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #                         f"{Fore.WHITE + Style.BRIGHT} {task['text']} {Style.RESET_ALL}"
                #                         f"{Fore.RED + Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                #                         f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                #                     )

                #     else:
                #         self.log(
                #             f"{Fore.MAGENTA+Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #             f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                #             f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                #         )
                # else:
                #     self.log(
                #         f"{Fore.MAGENTA+Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                #         f"{Fore.YELLOW+Style.BRIGHT} Completion is Skipped {Style.RESET_ALL}"
                #         f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                #     )
                # time.sleep(1)

                games_energy = user['gamesEnergy']
                if games_energy:
                    multipliers = [500, 150, 100, 50, 25, 10, 5, 3, 2, 1]

                    for game_type, details in games_energy.items():
                        if game_type in ['slotMachine', 'wheelOfFortune']:
                            energy = details['energy']

                            while energy > 0:
                                spin = None

                                for multiplier in multipliers:
                                    if energy >= multiplier:
                                        spin = self.spin_wheel(token, game_type, liveOpId, str(multiplier))
                                        if spin:
                                            energy = spin['userGameEnergy']['energy']
                                            reward = spin['prize']['prizeValue']
                                            reward_type = spin.get('prize', {}).get('prizeTypeName', 'Gae')
                                            get_type = reward_type
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} Type {game_type} {Style.RESET_ALL}"
                                                f"{Fore.GREEN+Style.BRIGHT}Is Success{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {reward} {get_type} {Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Energy{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {energy} Left {Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                            )
                                            break

                                        time.sleep(2)

                                if not spin:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} Type {game_type} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}No Available Energy{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                    break

                            if energy == 0:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Type {game_type} {Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT}No Available Energy{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            time.sleep(1)

                    free_spin = self.spin_wheel(token, 'WheelOfFortune', liveOpId, '1')
                    if free_spin:
                        energy = free_spin['userGameEnergy']['energy']
                        reward = free_spin['prize']['prizeValue']
                        reward_type = free_spin.get('prize', {}).get('prizeTypeName', 'Gae')
                        get_type = reward_type

                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} Type wheelOfFortune {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} Free {Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT}Is Success{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {reward} {get_type} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} Type wheelOfFortune {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} Free {Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT}Not Available{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                    time.sleep(1)

                    while True:
                        open = self.open_elevator(token, liveOpId)
                        if open:
                            reward = open['prize']['prizeValue']
                            reward_type = open['prize']['prizeTypeName']

                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Elevator{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Is Opened {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Result{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} You Win {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {reward} {reward_type} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Elevator{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} No Available Attempt {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                            break

                        time.sleep(2)

                    if not open:
                        self.quit_elevator(token)

                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"\
                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                boinkers = user['boinkers']
                if boinkers:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Boinker{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {boinkers['currentBoinkerProgression']['id']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} Level {boinkers['currentBoinkerProgression']['level']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
                    time.sleep(1)

                    upgrade_type = ['megaUpgradeBoinkers', 'upgradeBoinker']
                    while True:
                        for upgrade in upgrade_type:
                            upgrade_boinker = self.upgrade_boinker(token, upgrade_type=upgrade)
                            
                            if upgrade_boinker:
                                id = upgrade_boinker['userBoinkers']['currentBoinkerProgression']['id']
                                level = upgrade_boinker['userBoinkers']['currentBoinkerProgression']['level']
                                
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Boinker{Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT} Is Upgraded {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}] [{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {id} {Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} - Level {level} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                
                                if upgrade == 'megaUpgradeBoinkers':
                                    break

                            else:
                                if upgrade == 'megaUpgradeBoinkers':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Boinker{Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT} Mega Upgrade Failed {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Balance Not Enough {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Boinker{Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT} Isn't Upgraded {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Balance Not Enough {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )

                                break
                            
                            time.sleep(1)

                        else:
                            continue

                        break

                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Boinker{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                raffle = self.raffle_data(token)
                if raffle:
                    raffle_id = raffle.get('userRaffleData', {}).get('raffleId', None)
                    milestone = raffle.get('userRaffleData', {}).get('milestoneReached', 0)
                    ticket = raffle.get('userRaffleData', {}).get('tickets', 0)
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Raffle{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} ID {raffle_id} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Milestone{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {milestone} Reached {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {ticket} Ticket {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    time.sleep(1)

                    while True:
                        claim = self.claim_raffle(token)
                        if claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Raffle{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Ticket {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Milestone{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {claim['milestoneReached']} Reached {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {claim['tickets']} Ticket {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Raffle{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Ticket {Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT}Not Available to Claim{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                            break
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Raffle{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )

            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            collect_friends = self.question()

            while True:
                self.clear_terminal()

                liveOpId = self.load_liveOpId()
                if not liveOpId:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Boinkers{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Blocked By Cloudflare {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} Restart Again {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    return

                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, liveOpId, collect_friends)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Boinkers - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = Boinkers()
    bot.main()