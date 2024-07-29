#from django.shortcuts import render
from .models import Card
from store.forms import ContactForm
from django.shortcuts import render, redirect



# Create your views here.
def home(request):
    card =Card.objects.all().order_by('-id')

    context={
        "card":card
    }
    return render(request,'index.html',context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Replace '#home' with the appropriate URL or named URL pattern
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
    
def about(request):
    
    return render(request,'about.html')
