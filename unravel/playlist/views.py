from django.shortcuts import render
from apidata.views import search_result


def playlist(request):
    python = search_result('python', 'playlist')
    ml = search_result('machine learning', 'playlist')
    playlist = []
    playlist.append(ml)
    playlist.append(python)

    return render(request, 'playlist.html', {'playlist': playlist})
