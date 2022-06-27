from django.shortcuts import render


from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from message.models import Comentario

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class ComentarioListView(ListView):
    model = Comentario
    template_name = "message/comentario_list.html"
Comentario

class ComentarioDetailView(DetailView):
    model = Comentario
    template_name = "message/comentario_detail.html"
    fields = ['titulo_del_comentario', 'comment_date', 'comentario', 'autor_del_comentario', 'libro_comentado']


class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    success_url = reverse_lazy('comment:comment-list')
    fields = ['titulo_del_comentario', 'comentario', 'autor_del_comentario', 'libro_comentado']

class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    success_url = reverse_lazy('comment:comment-list')
    fields = ['titulo_del_comentario', 'comentario', 'libro_comentado']


class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    success_url = reverse_lazy('comment:comment-list')


