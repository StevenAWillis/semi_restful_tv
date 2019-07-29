from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def new_show(request):

    return render(request,'semi_app/new_show.html')

def all_shows(request):
    all_shows = Show.objects.all()
    context={
        'all_shows': all_shows
    }
    return render(request,'semi_app/all_shows.html', context)

def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    context ={
        'show': show
    }
    return render(request,'semi_app/edit_show.html', context)

def shows_id(request, show_id):
    show = Show.objects.get(id=show_id)
    context ={
        'show': show
    }
    return render(request,'semi_app/shows_id.html', context) 

def update_show(request, show_id):
    # errors = request
    errors = Show.objects.basic_validator(request.POST)

        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        print(errors)
        print(show_id)
        return redirect(f'/shows/{show_id}/edit')
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.description = request.POST['description']
        show.release_date = request.POST['date']
        show.save()
        context ={
            'show': show
        }
    
    return redirect(f'/shows/{show.id}')
    # return redirect(f'/shows')



def shows_create(request):
    # errors = request
    errors = Show.objects.basic_validator(request.POST)

        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        print(errors)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['date'],description=request.POST['description'])
        print(f'////////CREATE////////')
        show = Show.objects.last()
        show.save()
    return redirect(f'/shows/{show.id}')

def destroy_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    print(f'////////DELETE///////////')
    return redirect(f'/shows')