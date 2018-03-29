from django.shortcuts import render
from apidata.views import search_result


def home(request):

    java = search_result('java', 'video')
    python = search_result('python', 'video')
    video_list ={
        'java': java,
        'python': python
    }
    return render(request, 'index.html', {'video_list': video_list})


def search_video(request):
    query = request.POST.get('qr')

    video_list = search_result(query, 'video')
    return render(request, 'search_video.html', {'video_list': video_list})


def watch_video(request):
    return render(request, 'watch_video.html', None)


def about_us(request):
    return render(request, 'about_me.html', None)