import json
import requests
# from langdetect import detect
from textblob import TextBlob
#from textblob_fr import PatternTagger, PatternAnalyzer
#from textblob_de import TextBlobDE
from textblob import TextBlob
import re


api_key = "Your API"


        #returner des donnees
def get_data(url: str):
    json_url = requests.get(url)
    data = json.loads(json_url.text)
    return data


        # returner les commentaires
def get_video_comments(id: str):
    api = "Your API"
    url_comments = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&textFormat=plainText&videoId={id}&key={api}"
    data = get_data(url_comments)
    comments = []
    while True:
        for item in data['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        if 'nextPageToken' in data:
            nextPageToken = data['nextPageToken']
            url_nextPage = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&pageToken={nextPageToken}&videoId={id}&key={api_key}"
            data = get_data(url_nextPage)
        else:
            break
    return comments


        # returner le titre de video
def get_video_title(id: str):
    api = "Your API"
    url_title = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api}"
    data = get_data(url_title)
    return data["items"][0]["snippet"]["title"]



def analyse(comments):
    
    allcomments = []
    polarity = []
    for comment in comments:
        try:
            allcomments.append(comment)
            text = TextBlob(comment)  
            x = text.sentiment.polarity
            polarity.append(x)
        except:
            pass
        
        
    return allcomments, polarity
        
def calcule(polarity):
    pos = neg = neu = 0
    for x in polarity:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            neu += 1
    return pos,neg,neu
