from django import forms
from .models import *
  
class ProductForm(forms.ModelForm):
  
    class Meta:
        model = Product
        fields = ["name", "category", "tags", "description", "product_image"]
        