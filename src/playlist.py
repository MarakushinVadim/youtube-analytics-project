import datetime
from isodate import parse_duration
import json

from src.video import Video
from src.video import PLVideo

class PlayList(Video):


    def __init__(self, pl_id):
        self.pl_id = pl_id
        self.video_info = self.get_service().playlists().list(part='snippet, contentDetails', id=self.pl_id).execute()
        self.playlist_info = self.get_service().playlistItems().list(part='snippet, contentDetails', playlistId=self.pl_id).execute()
        self.url = f'https://www.youtube.com/playlist?list={self.pl_id}'
        self.title = self.video_info['items'][0]['snippet']['title']
        self.collection_video_id = []
        self.collection_video = []
        self.duration_video = []
        self.duration = datetime.timedelta(0, 0, 0)


    def show_best_video(self):
        for video in range(len(self.playlist_info)):
            self.collection_video_id.append(self.playlist_info['items'][video]['snippet']['resourceId']['videoId'])
        for video in self.collection_video_id:
            self.collection_video.append(PLVideo(video, 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'))
        max_like = 0
        for item in self.collection_video:
            if int(item.like_count) > int(max_like):
                max_like = item.like_count
                max_like_item = item
        return f'https://youtu.be/{max_like_item.video_id}'








    def total_duration(self):
        for item in self.collection_video:
            date_string = item.duration
            date = parse_duration(date_string)
            self.duration_video.append(date)
        for item in self.duration_video:
            print(item)
            print(self.duration)
            self.duration += item
        return self.duration









pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
#pl.collect_video_id()
#print(pl.playlist_info['items'][0]['snippet']['resourceId']['videoId'])
pl.show_best_video()
duration = pl.total_duration
print(pl.duration)
print(pl.total_duration())


#
#pl.collect_video_id()
##print(pl.collection_video_id['items'][0]['contentDetails']['duration'])
#
#var1 = PLVideo('feg3DYywNys', 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
#var1.print_info(var1.video_info)
##print(pl.collection_video[0].url)
#
#print(pl.collection_video[0].duration)
#
#pl.show_best_video()
##print(pl.show_best_video)