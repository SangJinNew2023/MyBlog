from django import forms
from .models import PostModel, MyBlogComment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4})) # adjustment content input area height
    class Meta:
        model = PostModel
        fields = ['title', 'content']

class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here...'}))

    class Meta:
        model = MyBlogComment
        fields = ['content']