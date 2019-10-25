from django.shortcuts import render

posts = [
    {
        'author': 'Stephen Bennett',
        'title': 'Welcome to our Project',
        'content': 'Alright looks like the due date for this project is 11/23.',
        'date_posted': 'October 25, 2019'
    },
    {
        'author': 'Kenny Cheng',
        'title': 'Ready to Roll',
        'content': 'Lets shoot for weekend dates to complete things.',
        'date_posted': 'October 24, 2019'
    },
    {
        'author': 'Cameron Mortus',
        'title': 'Lets Gooo!',
        'content': 'Can I vote for somewhere near food.',
        'date_posted': 'October 15, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'event/home.html', context)


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})
