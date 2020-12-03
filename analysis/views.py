from django.shortcuts import render
from .utilis import get_video_comments, analyse, calcule, get_video_title
import re
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def home(request):
    if request.method == 'POST':
        try:
            video_url = request.POST['video_id']
            x1 = re.search(r"^youtube.com/.*\w$", video_url)
            x2 = re.search(r"^youtu.be/.*\w$", video_url)

            if (x1):
                video_id = video_url.rsplit("=", 1)[1]
            if (x2):
                video_id = video_url.rsplit("/", 1)[1]
            else:
                video_id = video_url
            
            title = get_video_title(video_id)
            comments = get_video_comments(video_id)
            length = comments.__len__
            allcomments, polarity = analyse(comments)
            mylist = zip(allcomments, polarity)
            pos, neg, neu = calcule(polarity)
            context = {"comments":mylist, "length": length, "pos":pos, "neg":neg, "neu":neu, "title":title}
        except:
            context = {"title":0, "comments":0, "error": True}
    else:
        context = {"title":"", "comments":""}
    
    return render(request, 'home.html', context)