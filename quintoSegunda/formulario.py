from django import forms
//njnkhbjhb
    from .models import Post

    class PostForm(forms.ModelForm):

        class Meta:
            model = PostForm
            fields = ('title', 'text',)
