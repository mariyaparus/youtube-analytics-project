import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')

    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.subscribers_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel_info["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, filename):
        """Cохраняет в файл значения атрибутов экземпляра"""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.__dict__, file, ensure_ascii=False)

    @property
    def channel_id(self):
        """Возвращает id канала"""
        return self.__channel_id
