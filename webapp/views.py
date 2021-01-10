from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        "author": "MamadouB",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "January 06, 2021"
    },
    {
        "author": "DayeB",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "January 07, 2021"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'webapp/home.html', context)

def about(request):
    return render(request, 'webapp/about.html')

# Create your views here.
