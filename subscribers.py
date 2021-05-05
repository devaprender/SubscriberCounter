import requests
from datetime import datetime
import time


# Insira sua API key aqui
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'


def get_subscriber_count(channel_id):
    subscriber_count = requests.get(
        f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}')

    return subscriber_count.json()['items'][0]['statistics']['subscriberCount']


def get_channel_title(channel_id):
    title = requests.get(
        f'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}')
    return title.json()['items'][0]['snippet']['title']


def update_every_minute(channel_id, window):
    while True:
        total = get_subscriber_count(channel_id)
        print(total, datetime.now())
        window['sub_count'].Update(str(total))
        time.sleep(60)


if __name__ == '__main__':
    get_subscriber_count(channel_id)
    get_channel_title(channel_id)
