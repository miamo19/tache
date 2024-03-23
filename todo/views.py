from django.shortcuts import render, redirect
from django.contrib import messages
 
# import todo form and models
 
from .forms import FomulaireTache
from .models import Tache
 
###############################################
 
 
def index(request):
 
    item_list = Tache.objects.order_by("-date")
    if request.method == "POST":
        form = FomulaireTache(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = FomulaireTache()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)
 
 
### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Tache.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')