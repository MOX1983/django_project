from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Artiles.objects.order_by('-data')
    return render(request, 'news/home.html', {'news': news})

def create(request):
    error =''
    if request.method == "POST":
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Не правеньно заполнена форма"

    form = ArtilesForm()
    date = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', date)

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details.html'
    context_object_name = "article"

class NewsUpdateiView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm

class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/delete.html'