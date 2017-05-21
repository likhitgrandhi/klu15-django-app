from django import forms
from rango.models import *
from rango.choices import *



class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):

    title = forms.CharField(max_length=128, help_text="Enter the title of the link here.")
    url = forms.URLField(max_length=200, help_text="Enter the url of the notes/tutorial here.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        #If the url is not empty and it doesnot start with http:// we add it here
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)


class NoticeboardForm(forms.ModelForm):
    notice = forms.CharField( max_length=500, help_text='Enter the notice to be posted here.')
    post = forms.Textarea()

    class Meta:
        model = Noticeboard
        fields = ('notice',)

