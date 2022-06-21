from django.shortcuts import render


from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from message.models import Message

class MessageListView(ListView):
    model = Message
    template_name = "message/message_list.html"


class MessageDetailView(DetailView):
    model = Message
    template_name = "message/message_detail.html"
    fields = ['nombre_del_mensaje', 'message_date', 'mensaje', 'destinatario']


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    success_url = reverse_lazy('message:message-list')
    fields = ['nombre_del_mensaje', 'mensaje', 'destinatario']


