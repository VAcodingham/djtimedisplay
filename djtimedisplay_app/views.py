from django.shortcuts import render
from time import localtime, strftime
import datetime
def timedisplay(request):
    
    context = {
        "datetime": strftime("%Y-%m-%d %H:%M %p", localtime())

    }
    return render(request, 'index.html', context)


