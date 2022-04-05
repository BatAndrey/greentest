from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ReviewsForm
from .models import Reviews

# Create your views here.

def index(request):
    reviews = Reviews.objects.all()
    # name = Reviews.objects.all()
    # color = Reviews.objects.all()
    # grade = Reviews.objects.all()
    #name = Reviews.objects.all()
    return render(request, "reviews/index.html", {'title': "Main page site", 'reviews': reviews})


def add(request):
    error = ''
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'form was nor correct'
    form = ReviewsForm()
    context = {'form': form, 'error': error}
    return render(request, "reviews/add.html", context)
