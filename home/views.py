
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from home.models import CatalogueBook
from django.shortcuts import render
from django.db.models import Q
from user.models import Avatar
from message.models import Comentario

class CatalogueBookListView(ListView):
    model = CatalogueBook
    template_name = "home/cataloguebook_list.html"


class CatalogueBookDetailView(DetailView):
    model = CatalogueBook
    template_name = "home/cataloguebook_detail.html"
    fields = ['name', 'genre', 'publication_date', 'author', 'description', 'comment']


class CatalogueBookCreateView(LoginRequiredMixin, CreateView):
    model = CatalogueBook
    success_url = reverse_lazy('home:home-list')
    fields = ['name', 'genre', 'publication_date', 'author', 'description']


class CatalogueBookUpdateView(LoginRequiredMixin, UpdateView):
    model = CatalogueBook
    success_url = reverse_lazy('home:home-list')
    fields = ['name', 'genre', 'publication_date', 'author', 'description']


class CatalogueBookDeleteView(LoginRequiredMixin, DeleteView):
    model = CatalogueBook
    success_url = reverse_lazy('home:home-list')


def search(request):
	if request.GET['text_search']:
		search_param = request.GET['text_search']
		book_sell = CatalogueBook.objects.filter(name__contains=search_param)
		context_dict = {
            'book_sell': book_sell
        }
	return render(
        request=request,
        context=context_dict,
        template_name="home/cataloguebook_list.html",
    )



