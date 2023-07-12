from dotenv import load_dotenv
import os
import requests

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

MESSAGE = ";pokemon"

payload = {
    'content' : MESSAGE
}

header = {
    'authorization' : DISCORD_TOKEN
}

r = requests.post(f'https://discord.com/api/v9/channels/{DISCORD_CHANNEL_ID}/messages', data=payload, headers=header)