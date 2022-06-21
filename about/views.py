from django.views.generic import CreateView, UpdateView, DeleteView,ListView
from .models import About
from django.urls import reverse_lazy
from .forms import AboutForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AboutListView(ListView):   
    model = About
    template_name = 'about/about.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add About'
        context['title_views'] = 'About'         
        return context
    
class AboutCreateView(LoginRequiredMixin,CreateView):
    model = About
    form_class = AboutForm    
    template_name= 'about/create.html'
    success_url = reverse_lazy('about:about_list')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add About'
        context['title_views'] = 'About'         
        return context
    
class AboutUpdateView(LoginRequiredMixin,UpdateView):
    model = About
    form_class = AboutForm    
    template_name= 'about/create.html'
    success_url = reverse_lazy('about:about_list')
    
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edd About'
        context['title_views'] = 'About'         
        return context
    
class AboutDeleteView(LoginRequiredMixin,DeleteView):
    model = About
    template_name= 'about/delete.html'    
    success_url = reverse_lazy('about:about_list')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edd About'
        context['title_views'] = 'About'         
        return context