import json
import os

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = self.get_service().channels().list(id=self.channel_id, part='snippet, statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.url = self.channel_info['items'][0]['snippet']['thumbnails']['default']['url']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.subscribers_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        def printj(dict_to_print: dict) -> None:
            """Выводит словарь в json-подобном удобном формате с отступами"""
            print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
        printj(self.channel_info)


    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(f'''id = {self.channel_id}
            title : {self.title}
            url : {self.url}
            description : {self.description}
            subscribers_count : {self.subscribers_count}
            video_count : {self.video_count}
            view_count : {self.view_count}
            ''', file, ensure_ascii=False, indent=4)


    def __str__(self):
        return f'{self.title} ({self.url})'


    def __add__(self, other):
        return int(self.subscribers_count) + int(other.subscribers_count)


    def __sub__(self, other):
        return int(self.subscribers_count) - int(other.subscribers_count)


    def __gt__(self, other):
        return int(self.subscribers_count) > int(other.subscribers_count)


    def __ge__(self, other):
        return int(self.subscribers_count) >= int(other.subscribers_count)


    def __lt__(self, other):
        return int(self.subscribers_count) < int(other.subscribers_count)


    def __le__(self, other):
        return int(self.subscribers_count) <= int(other.subscribers_count)
