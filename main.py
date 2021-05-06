# YouTube Analytics

from youtube_analyzer import YouTubeAnalyzer
from client import API_KEY, CHANNEL_ID

yta = YouTubeAnalyzer(API_KEY, CHANNEL_ID)

statistic = yta.get_statistic()

print("Просмотров: ", statistic.viewCount)
print("Подписчиков: ", statistic.subscriberCount)
print("Видеороликов на канале: ", statistic.videoCount)

input("Нажмите для выхода")