from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from tablib import Dataset
from .resources import PersonResource
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Book


class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ProfilePageView(TemplateView):
    template_name = "profile.html"

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'import.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'import.html')

def list(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'list.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})

def displaybooks(request):
    Person.objects.all()
    info = Person.objects.all()
    info2 = Person.objects.all()
    print(info)
    bookdata = { "detail" : info, "details" : info2 }
    print(bookdata)
    resp =  render_to_response("displaybooks.html", bookdata, context_instance=Context(request))
    return resp
