from django.forms import ModelForm, Form, IntegerField
from .models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['img', 'img_url', 'name']


class ImageEditForm(Form):
    height = IntegerField()
    width = IntegerField()
