from googleapiclient.discovery import build
from django.shortcuts import render

DEVELOPER_KEY = "AIzaSyDy7uIm3_OBOibaOpe34voXfvMeQfJuSpw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class node:
   title = ''
   thumbnail = ''
   id = ''
   description = ''


def search_result(search_query, type):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(q=search_query,
                                            part="id,snippet",
                                            maxResults=50
                                            ).execute()
    video_list = []
    v_count = 1
    pl_count = 1
    for video in search_response.get("items", []):
        if video["id"]["kind"] == "youtube#video" and v_count<=9 and type == 'video':
            video_obj = node()
            video_obj.title = video["snippet"]["title"]
            video_obj.thumbnail = video["snippet"]["thumbnails"]["medium"]["url"]
            video_obj.id = video["id"]["videoId"]
            video_obj.description = video["snippet"]["description"]
            video_list.append(video_obj)
            v_count = v_count + 1

        elif(video["id"]["kind"] == "youtube#playlist" and pl_count<=9 and type == 'playlist'):

            video_obj = node()
            video_obj.title = video["snippet"]["title"]
            video_obj.thumbnail = video["snippet"]["thumbnails"]["medium"]["url"]
            video_obj.id = video["id"]["playlistId"]
            video_list.append(video_obj)
            pl_count = pl_count + 1

    return video_list


