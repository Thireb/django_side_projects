from django import forms


class contact(forms.Form):
    """contact definition."""

    # TODO: Define form fields here
    name = forms.CharField(label='Enter your Name', max_length=122,)
    permalink = forms.CharField(label='Enter your link address', max_length=122,)
    textBody = forms.CharField(widget=forms.Textarea)