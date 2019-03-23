from django.shortcuts import render ,redirect
from .models import Entry
from .forms import Entryform

# Create your views here.
def index (request):
    entries = Entry.objects.order_by('-datePosted')

    context = {'entries' : entries}
    return render(request,'entries/index.html',context)


def add (request):
    if request.method == 'POST':
        form = Entryform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form= Entryform()

    context ={'form' : form}
    return render(request,'entries/add.html',context)
