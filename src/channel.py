import json
import os

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        def printj(dict_to_print: dict) -> None:
            """Выводит словарь в json-подобном удобном формате с отступами"""
            print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
        printj(self.channel)


    @property
    def title(self):
        video_title: str = self.channel_dict['items'][0]['snippet']['title']
        return video_title

    @property
    def url(self):
        channel_link: str = self.channel_dict['items'][0]['snippet']['thumbnails']['default']['url']
        return channel_link

    @property
    def channel_description(self):
        channel_description: str = self.channel_dict['items'][0]['snippet']['description']
        return channel_description

    @property
    def channel(self):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel


    @property
    def subscribers_count(self):
        subscribers_count: str = self.channel_dict['items'][0]['statistics']['subscriberCount']
        return subscribers_count


    @property
    def video_count(self):
        video_count: str = self.channel_dict['items'][0]['statistics']['videoCount']
        return video_count


    @property
    def view_count(self):
        view_count: str = self.channel_dict['items'][0]['statistics']['viewCount']
        return view_count

    @property
    def channel_dict(self):
        channel_dict: dict = self.channel
        return channel_dict

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def to_json(self, file_name):
        pass
