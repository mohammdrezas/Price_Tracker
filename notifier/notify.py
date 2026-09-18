import os
import requests
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})

def send_terminal(message):
    print(message)

SENDERS = {
    "terminal": send_terminal,
    "telegram": send_telegram,
}

def send_alerts(drops):
    if not drops:
        return
    for drop in drops:
        message = f"قیمت {drop['name']} افت کرد! الان {drop['latest']} تومان. اخیر {drop['average']} تومان"
        for sender in SENDERS.values():
            sender(message)

if __name__ == "__main__":
    sample = [
        {"name": "Test Game 1", "latest": 500000, "average": 700000},
        {"name": "Test Game 2", "latest": 1200000, "average": 1500000},
    ]
    send_alerts(sample)