from django import forms

class FeedbackForm(forms.Form):
    feedback = forms.CharField(max_length=500)