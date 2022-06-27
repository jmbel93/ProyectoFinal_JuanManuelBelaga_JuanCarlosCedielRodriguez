
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from rate.models import BookToRate

class BookToRateListView(ListView):
    model = BookToRate
    template_name = "rate/booktorate_list.html"


class BookToRateDetailView(DetailView):
    model = BookToRate
    template_name = "rate/booktorate_detail.html"
    fields = ['name', 'genre', 'rate_date', 'author', 'uploading_user', 'description']


class BookToRateCreateView(LoginRequiredMixin, CreateView):
    model = BookToRate
    success_url = reverse_lazy('rate:rate-list')
    fields = ['name', 'genre', 'author', 'uploading_user', 'description']


class BookToRateUpdateView(LoginRequiredMixin, UpdateView):
    model = BookToRate
    success_url = reverse_lazy('rate:rate-list')
    fields = ['name', 'genre', 'author', 'uploading_user', 'description']


class BookToRateDeleteView(LoginRequiredMixin, DeleteView):
    model = BookToRate
    success_url = reverse_lazy('rate:rate-list')