import datetime
from isodate import parse_duration

from src.video import Video
from src.video import PLVideo

class PlayList(Video):


    def __init__(self, pl_id):
        self.pl_id = pl_id
        self.video_info = self.get_service().playlists().list(part='snippet, contentDetails', id=self.pl_id).execute()
        self.playlist_info = self.get_service().playlistItems().list(part='snippet, contentDetails', playlistId=self.pl_id).execute()
        self.url = f'https://www.youtube.com/playlist?list={self.pl_id}'
        self.title = self.video_info['items'][0]['snippet']['title']


    @property
    def collection_video_id(self):
        '''
        Возвращает список id Видео в плелисте
        '''
        collection_video_id = []
        for video in range(len(self.playlist_info)):
            collection_video_id.append(self.playlist_info['items'][video]['snippet']['resourceId']['videoId'])
        return collection_video_id


    @property
    def collection_video(self):
        '''
        создает список обьектов класс PLVideo для получения информации
        '''
        collection_video = []
        for video in self.collection_video_id:
            collection_video.append(PLVideo(video, 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'))
        return collection_video


    def show_best_video(self):
        '''
        берет количества лайков из обьекта PLVideo, выявляет наибольшее кол-во и возвращает ссылку на видео
        '''
        max_like = 0
        for item in self.collection_video:
            if int(item.like_count) > int(max_like):
                max_like = item.like_count
                max_like_item = item
        return f'https://youtu.be/{max_like_item.video_id}'


    @property
    def total_duration(self):
        '''
        возвращает общую продолжительность всех видео в плелисте
        '''
        total_duration = datetime.timedelta()
        duration_video = []
        for item in self.collection_video:
            date_string = item.duration
            date = parse_duration(date_string)
            duration_video.append(date)
        for item in duration_video:
            total_duration += item
        return total_duration



    def __str__(self):
        '''
        возвращает на печать общую продолжительность видео в формате str
        '''
        return f'{self.total_duration}'


