import os

from googleapiclient.discovery import build


class Video:
    """Класс для ютуб-видео"""

    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')

    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.video_info = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        self.title = self.video_info['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.video_id}'
        self.view_count = self.video_info["items"][0]["statistics"]["viewCount"]
        self.like_count = self.video_info["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id
