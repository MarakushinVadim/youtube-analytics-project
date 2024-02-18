import json
import os

from googleapiclient.discovery import build


class Video:


    def __init__(self, video_id):
        self.video_id = video_id
        self.video_info = self.get_service().videos().list(part='snippet, statistics', id=self.video_id).execute()

        try:
            self.title = self.video_info['items'][0]['snippet']['title']
            self.url = f'https://youtu.be/{self.video_id}'
            self.view_count = self.video_info['items'][0]['statistics']['viewCount']
            self.like_count = self.video_info['items'][0]['statistics']['likeCount']

        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None


    @classmethod
    def get_service(cls):
        api_key = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def print_info(self, dict_to_print):
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


    def __str__(self):
        return self.title


class PLVideo(Video):


    def __init__(self, video_id, pl_id):
        self.video_id = video_id
        self.pl_id = pl_id
        self.video_info = self.get_service().videos().list(part='snippet, statistics, contentDetails', id=self.video_id).execute()
        self.title = self.video_info['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.video_id}&list={pl_id}'
        self.view_count = self.video_info['items'][0]['statistics']['viewCount']
        self.like_count = self.video_info['items'][0]['statistics']['likeCount']
        self.duration = self.video_info['items'][0]['contentDetails']['duration']
