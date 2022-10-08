from django import forms
from feedbacks.models import FeedBack


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        exclude = ["author"]
