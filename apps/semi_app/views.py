from django.shortcuts import render, redirect
from .models import Show
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



def shows_create(request):
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