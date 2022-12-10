from django import forms
from blog.models import Comments


class NewCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comment_content']
