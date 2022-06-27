from django.forms import *
from home.models import CatalogueBook

class CatalogueBookForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'   

    class Meta:
        model = CatalogueBook
        fields = '__all__'
        
