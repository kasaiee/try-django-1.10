from django import forms
import models
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget()),

    class Meta:
        model = models.Blog
        fields = ('title', 'image', 'content', 'attach_file')
        
