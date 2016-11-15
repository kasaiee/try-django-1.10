from django.forms import ModelForm, Textarea
import models
from ckeditor.widgets import CKEditorWidget

class BlogForm(ModelForm):
    
    class Meta:
        model = models.Blog
        fields = ('title', 'image', 'content', 'attach_file')
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 2}),
        }
        