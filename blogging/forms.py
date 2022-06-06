from django.forms import ModelForm
from blogging.models import Post


class add_post(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
