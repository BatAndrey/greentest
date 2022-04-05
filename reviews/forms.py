from.models import Reviews
from django.forms import ModelForm, TextInput, Textarea

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        #fields = ["reviews", "grade", "color"]
        fields = ["reviews"]
        widgets = {"reviews": Textarea(attrs={'class': 'form-control', 'placeholder': "Input reviews film"})}