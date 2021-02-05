from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, NewsData
from django.views.generic import CreateView, ListView
data = None



def home(request):
    return render(request, "app1/home.html")


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            global data
            data = User.objects.filter(username=username, password=password)

            return render(request, "app1/home.html", {'data':data})
        except:
            messages.success(request, "Invalid Username and Password !.")
            return render(request, "app1/login.html")
    else:
        return render(request, "app1/login.html")


def news_upload(request):
    try:
        global data
        for i in data:
            author = i.author
        if author == "writer":
            if request.method == 'POST':
                title = request.POST["title"]
                content = request.POST["content"]
                image_url = request.POST["image_url"]
                NewsData(title=title, content=content, image_url=image_url).save()
                messages.success(request, "News added successfully.")
                return redirect('news_show')
            else:
                return render(request, 'app1/news_upload.html')
        else:
            messages.success(request, "For upload a news you have to login as a writer.")
            return redirect('news_show')
    except:
        messages.success(request, "You have to login first.")
        return redirect('login')




def news_show(request):
    global data
    if data is not None:
        object_list = NewsData.objects.all()
        return render(request, 'app1/news_list.html', {'object_list':object_list, })
    else:
        messages.success(request, "You have to login first.")
        return redirect('login')