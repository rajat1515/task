from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Growth File Ques</h1>')