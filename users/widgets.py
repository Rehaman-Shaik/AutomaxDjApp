from django.utils.safestring import mark_safe
from django.forms import widgets


class CustomPictureImageFieldWidget(widgets.FileInput):
    def render(self,name,value,attrs=None,**kwargs):
        default_html = super().render(name,value,attrs=None,**kwargs)
        img_html=mark_safe(f'<img src="{value.url}" width="200" />')
        return f'{img_html} {default_html}'