from django.shortcuts import render, redirect
from .form import *
from .models import *

# Create your views here.
def landing(request):
    if request.method == "POST":
        form = TestimoniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing')
    context = {}
    context['Berita'] = Berita.objects.all()
    context['Testimoni'] = Testimoni.objects.all()
    return render(request, "index.html", context)
