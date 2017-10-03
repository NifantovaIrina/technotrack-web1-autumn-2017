from django.shortcuts import render
from  django.shortcuts import HttpResponse
# Create your views here.
def postsList(request, id='100000'):
    return render(request, 'posts_list.html', {'id': id})

def post(request, id='0'):
    return render(request, 'post.html', {'id': id})

def userPage(request, id='100000'):
    return render(request, 'user_page.html', {'id': id})

def main(request):
    return render(request, 'main_page.html')

