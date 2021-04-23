from django.shortcuts import render
# from time import gmtime, strftime
from datetime import datetime

# Learn platform method
# def index(request):
#     context = {
#         "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#     }
#     return render(request,'index.html', context)


time = datetime.now()
def index(request):
    return render(request, 'index.html', {'time': time})