from django import forms
from rango.models import *
from rango.choices import *



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
        exclude = ('course',)


class NoticeboardForm(forms.ModelForm):
    notice = forms.CharField( max_length=500, help_text='Enter the notice to be posted here.')
    post = forms.Textarea()

    class Meta:
        model = Noticeboard
        fields = ('notice',)


class DepartmentForm(forms.ModelForm):

    name = forms.CharField(max_length=100,)
    batch = forms.CharField(max_length=100,)

    class Meta:
        model = Department
        fields = ('name', 'batch',)

