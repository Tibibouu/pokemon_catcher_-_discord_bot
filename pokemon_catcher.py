from dotenv import load_dotenv
import os
import requests

load_dotenv()

DISCORD_CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

# Token array
dToken = [os.getenv('DISCORD_TOKEN_1'), os.getenv('DISCORD_TOKEN_2')]


MESSAGE = ";pokemon"

# Send message to all channels
for i in range(dToken.__len__()):
    payload = {
        'content' : MESSAGE
    }

    header = {
        'authorization' : dToken[i]
    }

    r = requests.post(f'https://discord.com/api/v9/channels/{DISCORD_CHANNEL_ID}/messages', data=payload, headers=header)